# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 08:14:49 2025

@author: Allison Leung, Ava Binetti
"""
import pandas as pd
import seaborn as sns

data= pd.read_csv("data.csv")

#Part 3

#Q3
data_1= data[["Physicians", "Population"]]
pd.DataFrame.info(data_1)
#there are 10 empty cells in "physicians" and none in "population"

#Q4
print(pd.DataFrame.nunique(data))

#Q5
print(pd.DataFrame.describe(data))
#It provides the count of values, the mean, standard deviation, min and max value and level of confidence(25%,50%,75%) for columns with numerical values.

#Q6
data["GNI per Capita"] = data["GNI"]/data["Population"]
data["GNI per Capita"]=round(data["GNI per Capita"],2) # Rounds column to 2 decimals.
print(data["GNI per Capita"])

#Q7
Region_count= data["Region"].value_counts() #Counts how many of each variable in a column
print(Region_count)
# There are 56 countries in Africa, 50 in Asia, 47 in Europe, 46 in Americas and 19 in Oceania

HIE_count = data["High Income Economy"].value_counts()
print(HIE_count)
# There are 67 countries with HIE and 150 that don't

#Q8
HIE_countries=pd.crosstab(data["Region"], data["High Income Economy"]) #Counts how many 1 and 0 (Yes and no) in HIE column sorted by Region
print(HIE_countries)
#There are 17 HIE countries in Amercias, 14 in Asia, 31 in Europe and 4 in Oceania.

#Q9
count=0
for i in range(0,217):
    if data.iloc[i]["Life expectancy, female"] > 80: #iloc finds value in the named column using its index (i)
        print(data.iloc[i]["Country Name"])
        count+=1
print(count, "countries")

#Part 4

#Q1
sns.relplot(
    data=data,
    x="Life expectancy, female",
    y="GNI per Capita")

sns.relplot(
    data=data,
    x="Life expectancy, male",
    y="GNI per Capita")





