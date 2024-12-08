import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from warnings import filterwarnings
import xgboost as xgb
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import optuna


filterwarnings('ignore')
file_path = 'C:/Users/lyoshaa/Downloads/all_v2.csv'

df = pd.read_csv(file_path)
for col in df.columns:
    pct_missing = np.mean(df[col].isna())
    print(f'{col} - {round(pct_missing * 100)}%')

MIN_AREA = 20
MAX_AREA = 200
MIN_KITCHEN = 6
MAX_KITCHEN = 30
MIN_PRICE = 1_500_000
MAX_PRICE = 50_000_000

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df.drop('time', axis=1, inplace=True, errors='ignore')
    df['date'] = pd.to_datetime(df['date'])
    df['rooms'] = df['rooms'].apply(lambda x: 0 if x < 0 else x)
    df['price'] = df['price'].abs()
    df = df[(df['area'] <= MAX_AREA) & (df['area'] >= MIN_AREA)]
    df = df[(df['price'] <= MAX_PRICE) & (df['price'] >= MIN_PRICE)]
    df.loc[(df['kitchen_area'] >= MAX_KITCHEN) | (df['area'] <= MIN_AREA), 'kitchen_area'] = 0
    area_mean, kitchen_mean = df[['area', 'kitchen_area']].quantile(0.5)
    kitchen_share = kitchen_mean / area_mean
    df.loc[(df['kitchen_area'] == 0) & (df['rooms'] != 0), 'kitchen_area'] = \
        df.loc[(df['kitchen_area'] == 0) & (df['rooms'] != 0), 'area'] * kitchen_share
    return df

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df.drop('date', axis=1, inplace=True, errors='ignore')
    df['level_to_levels'] = df['level'] / df['levels']
    df['area_to_rooms'] = (df['area'] / df['rooms']).abs()
    df.loc[df['area_to_rooms'] == np.inf, 'area_to_rooms'] = df.loc[df['area_to_rooms'] == np.inf, 'area']
    return df

df = df.pipe(clean_data)
df = df.pipe(add_features)

# KHMAO == 2484
df = df.loc[df['region'] == 2484]

plt.hist(df['price'], bins=20)
plt.axvline(df['price'].mean(), label='Mean Price', color='green')
plt.axvline(df['price'].median(), label='Median Price', color='red')
plt.legend()
plt.xlabel('Apartment Price, Rubles')
plt.title('Price Distribution')
plt.show()
plt.figure(figsize=(15, 10))
sns.heatmap(df.corr(), center=0, cmap='mako', annot=True)
plt.title('Correlation Matrix')
plt.show()
X, y = df.drop('price', axis=1), df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True, random_state=1)

model = xgb.XGBRegressor()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(f'R^2 score: {r2_score(y_test, predictions):.3f}')

def objective(trial):
    params = {
        'tree_method': 'gpu_hist',
        'lambda': trial.suggest_loguniform('lambda', 1e-2, 1e2),
        'alpha': trial.suggest_loguniform('alpha', 1e-2, 1e2),
        'learning_rate': trial.suggest_float('learning_rate', 1e-3, 1.0),
        'n_estimators': trial.suggest_int('n_estimators', 100, 1000),
        'max_depth': trial.suggest_int('max_depth', 3, 10),
        'subsample': trial.suggest_float('subsample', 0.5, 1.0)
    }
    model = xgb.XGBRegressor(**params)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    return r2_score(y_test, predictions)

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=25)

best_params = study.best_params
final_model = xgb.XGBRegressor(**best_params)
final_model.fit(X_train, y_train)
final_predictions = final_model.predict(X_test)
print(f'Final R^2 score: {r2_score(y_test, final_predictions):.3f}')

mean_price = df['price'].mean()
median_price = df['price'].median()
print(f"Средняя цена квартир: {mean_price:.2f} рублей")
print(f"Медианная цена квартир: {median_price:.2f} рублей")