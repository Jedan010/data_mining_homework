# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 21:22:28 2017

@author: J
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('income.csv',encoding='latin1', usecols=['income_middle','income_means'])
index = pd.date_range('2/1/2013', '8/1/2017',freq='Q-JAN')
data.index = index
print(data.head())

data.plot()
plt.show()
data.boxplot()
plt.show()

data['bias'] = data['income_means'] - data['income_middle']

data['bias'].plot()
plt.scatter(data.index, data['bias'])
plt.show()
plt.boxplot(data['bias'])
plt.show()