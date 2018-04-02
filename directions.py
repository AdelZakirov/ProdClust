# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

dfXY = pd.read_csv("XY.csv", sep=";")
#добавить функциональность basemap

dfLrate = pd.read_csv("Lrate.csv", sep=";")

#Заменяем 0 на nan и убераем столбец w
dfLrate = dfLrate.replace(0, np.nan).drop(columns='w')

dfF = dfLrate.apply(lambda x: x.first_valid_index(), axis=1)
dfL = dfLrate.apply(lambda x: x.last_valid_index(), axis=1)

#Узнать длину каждой записи Lrate и Wcut и сколько внутри nan


#Провести интерполяцию значений внутри цепочек


#Выбрать наиболее представительные кривые по суммарным признакам


#Применить DTW для кластеризации эталонных примеров

