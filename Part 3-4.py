# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 08:14:49 2025

@author: Allison Leung, Ava Binetti
"""
import pandas as pd
import seaborn as sns

data = pd.read_csv("data.csv")

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
a=sns.relplot(data=data, x="Greenhouse gas emissions", y="Life expectancy, female", hue="Region", col="Region", 
            col_wrap=3)
a.fig.suptitle("Effects of greenhouse gases on female life expectancy", y=1.05)

#5.2 Life Expectancy and Tertiary Education
b=sns.lmplot(data=data, x="Life expectancy, female", y="Tertiary education, female", hue="Region", col="Region", 
            col_wrap=3)
b.fig.suptitle("Life expectancy and the effet it has on women in higher education", y=1.05)

#5.3 Tertiary Education and Women in national parliament
c=sns.relplot(data=data, x="Tertiary education, female", y="Women in national parliament", hue="Region", col="Region", 
            col_wrap=3)
c.fig.suptitle("Women in national parliament as a result of higher education", y=1.05)

#5.4 Population and Physicians
d=sns.relplot(data=data, x="Population", y="Physicians", hue="Region", col="Region", 
            col_wrap=3)
d.fig.suptitle("Population and the amount of physicians in that country ", y=1.05)

#5.5 Male tertiary education and internet use
e=sns.relplot(data=data, x="Internet use", y="Tertiary education, male", hue="Region", col="Region", 
            col_wrap=3).set(title="Male Education and Internet Use by Region")
e.fig.suptitle("Correlation between men with higher education and internet use", y=1.05)

#Question 6

#A
data["Emissions per Capita"] = data["Greenhouse gas emissions"]/data["Population"]
print(data["Emissions per Capita"])

sns.lmplot(data=data, x="Internet use", y="Emissions per Capita").set(title="Effects of internet use on ghg emissions per capita")

#B
High_emissions=data[data["Emissions per Capita"]>0.03]
for country in High_emissions["Country Name"]:
    print(country)
print(High_emissions["Region"])

#C
for HE_Internet_use in High_emissions["Internet use"]:
    print(HE_Internet_use)
f=sns.lmplot(data=data,  x="Internet use",  y="Emissions per Capita", hue="Region", col="Region", 
           col_wrap=3)
f.fig.suptitle("Effects of internet use on ghg emissions per capita", y=1.05)

#D
high_income = data[data["High Income Economy"] == 1]
HI_HE = high_income[high_income["Emissions per Capita"]> 0.03]
print(HI_HE)

