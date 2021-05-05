# change the working directory to where the full_data.csv is stored.
import os
os.chdir("D:/python/python39")
import numpy as np
import pandas as pd
covid_data = pd.read_csv("full_data.csv")
covid_data.info()
print(covid_data.describe())

# show all columns,  and  every  second  row  between  (andincluding) 0 and 10
print(covid_data.iloc[0:10:2, :])

# used a Boolean to show “totalcases” for all rows correspondingto Afghanistan.
print(covid_data.loc[covid_data["location"] == "Afghanistan", "total_cases"])

# save "world" as separate objects.
world_data = covid_data.loc[(covid_data.location == "World"), ["new_cases", "date", "new_deaths"]]

# computed the mean and median of new cases for the entire world.
a = np.mean(world_data.new_cases)
b = np.median(world_data.new_cases)
print('The mean of the new cases worldwide is ', a, '.')
print('the median of the new cases worldwide is', b, '.')

# create a boxplot of new cases worldwide.
import matplotlib.pyplot as plt
plt.boxplot(world_data.new_cases,
            labels={'new cases worldwide'},
           boxprops={'color': 'yellow'})
plt.title('boxplot of new cases worldwide')
plt.show()

# plotted both new cases and new deaths worldwide.
plt.plot(world_data.date, world_data.new_cases, 'bo', label='new cases')
plt.plot(world_data.date, world_data.new_deaths, 'ro', label='new deaths')
plt.xticks(world_data.date.iloc[0:len(world_data.date):4], rotation=-90)
plt.xlabel('date')
plt.ylabel('number')
plt.title('new cases and new deaths worldwide')
plt.show()

# the tendency for the new cases and total cases in China.
china = covid_data.loc[(covid_data.location == "China"), ["new_cases", "date", "total_cases"]]
plt.plot(china.date, china.new_cases, 'b+', label='china new cases')
plt.plot(china.date, china.total_cases, 'r+', label='china total cases')
plt.xticks(china.date.iloc[0:len(china.date):4], rotation=-90)
plt.xlabel('date')
plt.ylabel('number')
plt.title('new cases and new deaths in china')
plt.show()
