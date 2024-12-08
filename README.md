# prog-term-project
Курсовая работа за первый курс, основанная на следующих статьях: 
[Habr](https://habr.com/ru/articles/710000/), 
[Kaggle](https://www.kaggle.com/code/khazovaalexandra/nn-in-real-russian-estate/notebook)


## Задание
    Провести анализ данных о недвижимости в ХМАО, посторить модель прогнозирования цен квартир, визуализировать корреляции.

## Описание проделанной работы
1. Скачал [датасет](https://www.kaggle.com/datasets/mrdaniilak/russia-real-estate-20182021?resource=download) с данными о доступной к продаже недвижимости на российском рынке за 2018-2021 год.
2. Провел первичную обработку данных:
   * Удалены квартиры которые:
     * Не соответствуют диапазону цен 1.5 - 50 млн. рублей
     * Не соответствуют диапазону площади пола 20 - 200 м^2
     * Не соответствуют диапазону площади кухни 6 - 30 м^2
   * Преобразованы отрицательные значения в данных:
     * Неверные значения в колонке с количеством комнат были заменены на 0 (для студий)
     * Отрицательные значения цен заменены на их абсолютные значения
3. Расчитал среднюю и медианную цены квартир. __pnglink__
4. Построил гистограмму распределения цен, в которой:
   * Ось абсцисс отвечат за цену квартир, в млн. рублей
   * Ось ординат отвевчает за количество квартир в определённом ценовом диапазоне
   * Зеленая вертикальная линия показывает среднюю цену квартир
   * Красная вертикальная линия показывает медианную цену квартир
5. Построил карту корреляции.
6. Используя XGBoost построил модель для предспредсказания цены квартиры, основываясь на её характеристиках, а именно:
     1. date - дата публикации объявления
     2. time – время публикации
     3. geo_lon - широта
     4. geo_lat - долгота
     5. region - регион
     6. building_type - 0 - Другой. 1 - Панельный. 2 - Монолитный. 3 - Кирпичный. 4 - Блочный. 5 - Деревянный
     7. object_type - Тип квартиры. 1 - Вторичный рынок недвижимости; 2 - Новостройка
     8. level - этаж квартиры
     9. levels - количество этажей в доме
     10. rooms - количество жилых комнат
     11. area - общая площадь квартиры
     12. kitchen_area - площадь кухни
     13. price - цена в рублях
  `В этой модели R^2 (коэффициент детерминации) - статистический показатель, который оценивает, насколько хорошо предсказания модели соответствуют реальным данным.`
7. Оптимизировал эту модель с помощью Optuna
   * Это должно привести к оптимизации коэффицента R^2. Я провел 8 запусков программы с первоначальным значение 0.819. По результатам всех запусков я выбрал один с самым оптимизированным значением R^2. Вот результаты отпимизации для всех 8 запусков:
      * 0,819 -> 0,839
      * 0,819 -> 0,841
      * 0,819 -> 0,827
      * 0,819 -> 0,835
      * 0,819 -> 0,837
      * 0,819 -> 0,832
      * 0,819 -> 0,839
      * **0,819 -> 0,843**

## Вывод программы
~~~~~
price - 0%
date - 0%
time - 0%
geo_lat - 0%
geo_lon - 0%
region - 0%
building_type - 0%
level - 0%
levels - 0%
rooms - 0%
area - 0%
kitchen_area - 0%
object_type - 0%
[I 2024-12-08 10:55:28,811] A new study created in memory with name: no-name-2a22e02a-10d4-4fb3-9b33-f01799b0bf6a
R^2 score: 0.819
[I 2024-12-08 10:55:33,547] Trial 0 finished with value: 0.7872419953346252 and parameters: {'lambda': 2.1205635047248586, 'alpha': 0.03229322419046218, 'learning_rate': 0.688318126318722, 'n_estimators': 884, 'max_depth': 8, 'subsample': 0.9957411406702905}. Best is trial 0 with value: 0.7872419953346252.
[I 2024-12-08 10:55:39,307] Trial 1 finished with value: 0.8237187266349792 and parameters: {'lambda': 47.08020323349768, 'alpha': 3.21818059923711, 'learning_rate': 0.2774449799928935, 'n_estimators': 584, 'max_depth': 10, 'subsample': 0.7937021029116473}. Best is trial 1 with value: 0.8237187266349792.
[I 2024-12-08 10:55:41,103] Trial 2 finished with value: 0.6797677278518677 and parameters: {'lambda': 0.05390525794368786, 'alpha': 8.208221466603371, 'learning_rate': 0.6073163000911415, 'n_estimators': 361, 'max_depth': 8, 'subsample': 0.6224040289167507}. Best is trial 1 with value: 0.8237187266349792.
[I 2024-12-08 10:55:43,613] Trial 3 finished with value: 0.8374608755111694 and parameters: {'lambda': 0.0698323995081403, 'alpha': 1.6958941210769467, 'learning_rate': 0.045136089408391804, 'n_estimators': 904, 'max_depth': 6, 'subsample': 0.9703596922654811}. Best is trial 3 with value: 0.8374608755111694.
[I 2024-12-08 10:55:44,998] Trial 4 finished with value: 0.6783204078674316 and parameters: {'lambda': 1.1499403609809793, 'alpha': 28.74363149462471, 'learning_rate': 0.9313009412812963, 'n_estimators': 520, 'max_depth': 6, 'subsample': 0.6271828211874071}. Best is trial 3 with value: 0.8374608755111694.
[I 2024-12-08 10:55:46,796] Trial 5 finished with value: 0.6063790321350098 and parameters: {'lambda': 0.029014837209003757, 'alpha': 13.473545629812913, 'learning_rate': 0.9343379896563848, 'n_estimators': 298, 'max_depth': 9, 'subsample': 0.7822832161576683}. Best is trial 3 with value: 0.8374608755111694.
[I 2024-12-08 10:55:47,388] Trial 6 finished with value: 0.8353977203369141 and parameters: {'lambda': 10.824677153493997, 'alpha': 82.16040504110418, 'learning_rate': 0.38268516136867264, 'n_estimators': 331, 'max_depth': 4, 'subsample': 0.7889191706106566}. Best is trial 3 with value: 0.8374608755111694.
[I 2024-12-08 10:55:47,814] Trial 7 finished with value: 0.8215509057044983 and parameters: {'lambda': 16.58265403027751, 'alpha': 6.36222384312773, 'learning_rate': 0.32091719061625557, 'n_estimators': 100, 'max_depth': 7, 'subsample': 0.6734487512389901}. Best is trial 3 with value: 0.8374608755111694.
[I 2024-12-08 10:55:50,994] Trial 8 finished with value: 0.795045793056488 and parameters: {'lambda': 1.2218749904957817, 'alpha': 0.31505305590986876, 'learning_rate': 0.5547452751803971, 'n_estimators': 451, 'max_depth': 9, 'subsample': 0.8415541392182748}. Best is trial 3 with value: 0.8374608755111694.
[I 2024-12-08 10:55:51,712] Trial 9 finished with value: 0.8192490935325623 and parameters: {'lambda': 10.347757065364563, 'alpha': 0.021073559260416756, 'learning_rate': 0.5050318048126503, 'n_estimators': 426, 'max_depth': 4, 'subsample': 0.8836646788806528}. Best is trial 3 with value: 0.8374608755111694.
[I 2024-12-08 10:55:53,609] Trial 10 finished with value: 0.8415966033935547 and parameters: {'lambda': 0.14330716850688224, 'alpha': 0.8040118988310787, 'learning_rate': 0.011636107852168065, 'n_estimators': 928, 'max_depth': 5, 'subsample': 0.5026583311714448}. Best is trial 10 with value: 0.8415966033935547.
[I 2024-12-08 10:55:55,718] Trial 11 finished with value: 0.8454287052154541 and parameters: {'lambda': 0.13718108837230847, 'alpha': 0.47036475460509525, 'learning_rate': 0.02292969709406545, 'n_estimators': 967, 'max_depth': 5, 'subsample': 0.5079758432551031}. Best is trial 11 with value: 0.8454287052154541.
[I 2024-12-08 10:55:56,722] Trial 12 finished with value: 0.8387008309364319 and parameters: {'lambda': 0.09759770469243004, 'alpha': 0.3773730350170788, 'learning_rate': 0.04486710870374457, 'n_estimators': 752, 'max_depth': 3, 'subsample': 0.5178484026912427}. Best is trial 11 with value: 0.8454287052154541.
[I 2024-12-08 10:55:58,859] Trial 13 finished with value: 0.8287453651428223 and parameters: {'lambda': 0.24460893941424927, 'alpha': 0.11662040342032488, 'learning_rate': 0.16187305300403354, 'n_estimators': 991, 'max_depth': 5, 'subsample': 0.500619622159379}. Best is trial 11 with value: 0.8454287052154541.
[I 2024-12-08 10:56:00,456] Trial 14 finished with value: 0.8218830227851868 and parameters: {'lambda': 0.013089934696972123, 'alpha': 0.5972090274266983, 'learning_rate': 0.17919222897278236, 'n_estimators': 726, 'max_depth': 5, 'subsample': 0.5666555831662032}. Best is trial 11 with value: 0.8454287052154541.
[I 2024-12-08 10:56:01,518] Trial 15 finished with value: 0.6891764402389526 and parameters: {'lambda': 0.24624659849479155, 'alpha': 0.104685423513635, 'learning_rate': 0.002526887523092214, 'n_estimators': 748, 'max_depth': 3, 'subsample': 0.6944222261253156}. Best is trial 11 with value: 0.8454287052154541.
[I 2024-12-08 10:56:03,861] Trial 16 finished with value: 0.8224325180053711 and parameters: {'lambda': 0.3077344587002374, 'alpha': 1.6041064606190354, 'learning_rate': 0.15837286889469637, 'n_estimators': 984, 'max_depth': 5, 'subsample': 0.5786364726642055}. Best is trial 11 with value: 0.8454287052154541.
[I 2024-12-08 10:56:06,941] Trial 17 finished with value: 0.7952969670295715 and parameters: {'lambda': 0.44900054057482497, 'alpha': 0.07863409695548591, 'learning_rate': 0.3995085452646391, 'n_estimators': 862, 'max_depth': 7, 'subsample': 0.560721335303362}. Best is trial 11 with value: 0.8454287052154541.
[I 2024-12-08 10:56:08,026] Trial 18 finished with value: 0.7354768514633179 and parameters: {'lambda': 3.9563412620557603, 'alpha': 0.733044466001957, 'learning_rate': 0.7856354342807693, 'n_estimators': 631, 'max_depth': 4, 'subsample': 0.6890569726245772}. Best is trial 11 with value: 0.8454287052154541.
[I 2024-12-08 10:56:10,414] Trial 19 finished with value: 0.8045781850814819 and parameters: {'lambda': 0.010060960142460414, 'alpha': 0.011043790282716594, 'learning_rate': 0.24500655584875713, 'n_estimators': 812, 'max_depth': 6, 'subsample': 0.6125180807530978}. Best is trial 11 with value: 0.8454287052154541.
[I 2024-12-08 10:56:11,923] Trial 20 finished with value: 0.8323745727539062 and parameters: {'lambda': 0.09258549933093563, 'alpha': 0.2233596906486729, 'learning_rate': 0.09513313778958986, 'n_estimators': 672, 'max_depth': 5, 'subsample': 0.536524428438579}. Best is trial 11 with value: 0.8454287052154541.
[I 2024-12-08 10:56:12,999] Trial 21 finished with value: 0.7848691940307617 and parameters: {'lambda': 0.12196431546733118, 'alpha': 0.4508604938292538, 'learning_rate': 0.00641970060055404, 'n_estimators': 792, 'max_depth': 3, 'subsample': 0.501547740730921}. Best is trial 11 with value: 0.8454287052154541.
[I 2024-12-08 10:56:14,273] Trial 22 finished with value: 0.8416885733604431 and parameters: {'lambda': 0.02255165487356963, 'alpha': 1.2477948753899188, 'learning_rate': 0.12801086421808144, 'n_estimators': 915, 'max_depth': 3, 'subsample': 0.5015635700773948}. Best is trial 11 with value: 0.8454287052154541.
[I 2024-12-08 10:56:15,921] Trial 23 finished with value: 0.837895929813385 and parameters: {'lambda': 0.028027052811802632, 'alpha': 2.105346968516769, 'learning_rate': 0.10844463526387349, 'n_estimators': 934, 'max_depth': 4, 'subsample': 0.591387098180146}. Best is trial 11 with value: 0.8454287052154541.
[I 2024-12-08 10:56:17,392] Trial 24 finished with value: 0.8227386474609375 and parameters: {'lambda': 0.026916554906699447, 'alpha': 1.140727052977945, 'learning_rate': 0.2192550044473113, 'n_estimators': 850, 'max_depth': 4, 'subsample': 0.5440617800000624}. Best is trial 11 with value: 0.8454287052154541.
Final R^2 score: 0.843
Средняя цена квартир: 4320096.83 рублей
Медианная цена квартир: 3960000.00 рублей

Process finished with exit code 0
~~~~~
