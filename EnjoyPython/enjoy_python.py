# -*- coding: utf-8 -*-
import pandas as pd
from pandas import DataFrame

from pylab import *
from scipy import *
df1 = pd.read_csv("indicator_gapminder_gdp_per_capita_ppp.txt", sep='\t')
df2 = pd.read_csv("indicator_gapminder_population.txt", sep='\t')
df3 = pd.read_csv("indicator_life_expectancy_at_birth.txt", sep='\t')

time = []
y = []
x = []
years = []
color = []
area = []
label = []
i = 0 
for year in range(1950, 2012 + 1):
    years.append(year)
    
    for data in df3[str(year)]:
        if data!=data:data=0
        y.append(data)
        color.append(data)
        
    for data in df1[str(year)]:
        if data!=data:data=0
        x.append(data)
        
    for data in df2[str(year)]:
        if data!=data:data=0
        area.append(sqrt(data/10))
        
   
    
    for data in df1["GDP per capita"]:
        text(x[i], y[i], data + "\n" + str(year),size=9,horizontalalignment='center')
        i = i + 1

scatter(x, y, c=color, s=area, linewidths=2, edgecolor='w')

axis([0,max(x)*1.2,0,max(y)*1.2])
xlabel('GDP per capita')
ylabel('Life Expectancy')
show()

