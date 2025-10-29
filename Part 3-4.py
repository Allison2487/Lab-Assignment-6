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

#Question 1
sns.relplot(data=data, x="Life expectancy, female", 
            y="GNI per Capita").set(title="GNI per capita according to female life expectancy")

sns.relplot(data=data, x="Life expectancy, male", 
            y="GNI per Capita").set(title="GNI per capita according to male life expectancy")

#Question 2
sns.relplot(data=data, x="Life expectancy, female", y="GNI per Capita", 
            hue="Region").set(title="GNI per capita according to female life expectancy in different regions")

sns.relplot(data=data, x="Life expectancy, male", y="GNI per Capita", 
            hue="Region").set(title="GNI per capita according to male life expectancy in different regions")   

#Question 3
sns.relplot(data=data, x="Life expectancy, female", y="GNI per Capita", hue="Region", kind="line", 
            errorbar="sd").set(title="GNI per capita according to female life expectancy")

sns.relplot(data=data, x="Life expectancy, male", y="GNI per Capita", hue="Region", kind="line", 
            errorbar="sd").set(title="GNI per capita according to male life expectancy")

#Question 4
sns.lmplot(data=data, x="Life expectancy, female", y="GNI per Capita", 
           hue="Region").set(title="GNI per capita according to female life expectancy")

sns.lmplot(data=data, x="Life expectancy, male", y="GNI per Capita", 
           hue="Region").set(title="GNI per capita according to male life expectancy")

#Question 5 (5.1-5.5)

#5.1 Life expectancy and Greenhouse gas emissions
sns.relplot(data=data, x="Greenhouse gas emissions", y="Life expectancy, female", hue="Region", col="Region", 
            col_wrap=3).set(title="Effect of greenhouse gases on female life expectancy around the world")

sns.relplot(data=data, x="Greenhouse gas emissions", y="Life expectancy, male", hue="Region", col="Region", 
            col_wrap=3).set(title="Effect of greenhouse gases on male life expectancy around the world")

#5.2 Life Expectancy and Tertiary Education
sns.relplot(data=data, x="Life expectancy, female", y="Tertiary education, female", hue="Region", col="Region", 
            col_wrap=3).set(title="Correlation between a country's female life expectancy and female tertiary education")

#5.3 Tertiary Education and Women in national parliament
sns.relplot(data=data, x="Tertiary education, female", y="Women in national parliament", hue="Region", col="Region", 
            col_wrap=3).set(title="Female teriary education and its influence to have women in national parliament")
#5.4
#5.5

#Q6
