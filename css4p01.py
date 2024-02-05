#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 13:42:36 2024

@author: sanelecebekhulu
"""

import pandas as pd

df = pd.read_csv("movie_dataset.csv")

pd.set_option('display.max_rows',None)
print(df)

#remove spaces in columns

df.columns = df.columns.str.replace(' ', '_')

x = df["Metascore"].mean()

df["Metascore"].fillna(x, inplace = True) 

x2 = df["Revenue_(Millions)"].mean()

df["Revenue_(Millions)"].fillna(x2, inplace = True) 

print(df)



df= df.sort_values(by= ['Rating'], ascending= False)


df["Revenue_(Millions)"].mean()



start_Year = 2015
end_Year = 2016
filtered_df = df[(df['Year'] >= start_Year) & (df['Year'] <= end_Year)]
average_value = filtered_df['Revenue_(Millions)'].mean()
print(average_value)



start_Year = 2016
end_Year = 2016
filtered_df = df[(df['Year'] >= start_Year) & (df['Year'] <= end_Year)]
sum_value = filtered_df['Year'].sum()
print(sum_value)



Chris_Nolan = df[df['Director'] == 'Christopher Nolan']
print(Chris_Nolan)


print(df[df['Rating'] >= 8])



Chris_Nolan = df[df['Director'] == 'Christopher Nolan']
print(Chris_Nolan['Rating'].median())
print(Chris_Nolan)


filtered_df = df[(df["Year"] == '2016')]
average_value = filtered_df['Rating'].mean()
print(average_value)



df.groupby("Year").agg({"Rating":"mean"})

start_Year = 2016
end_Year = 2016
filtered_df = df[(df['Year'] >= start_Year) & (df['Year'] <= end_Year)]
sum_value = filtered_df['Year'].sum()
print(sum_value)



#question9
#percentage_increase = ((final_value_2016 - initial_value_2006) / initial_value_2006) * 100

data = df[(df['Year'])] 
movies_df = pd.DataFrame(data)

# Calculate the number of movies per year
movies_per_year = movies_df.value_counts().sort_index()

# Calculate the percentage change in the number of movies
percentage_change = movies_per_year.pct_change() * 100

# Display the result
print(percentage_change)


#trial 2

df.groupby("Year").agg({"Rating":"mean"})

#attempt 3

movies_2006 = df[df['Year'] == 2006].shape[0]
movies_2016 = df[df['Year'] == 2016].shape[0]

# Calculate the percentage increase
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100

print(percentage_increase)

#Question10

target_name = 'Bradley Cooper'
name_frequency = df['Actors'].str.count(target_name).sum()
print(name_frequency)


#Question11
target_name = 'Bradley Cooper'
name_frequency = df['Actors'].str.count(target_name).sum()
print(name_frequency)


grouped = df.groupby('Genre')

count_unique = grouped['Genre'].count()
print(count_unique)
 

#attempt2
genres_df = df['Genre'].str.split(',').explode().str.strip()

unique_genres_count = genres_df.nunique()
print(unique_genres_count)

#Question12

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

correlation = df['Rating'].corr(df['Runtime_(Minutes)'])

# Plot a scatter plot for visualization
sns.lmplot(x='Runtime_(Minutes)', y='Rating', data=df)
#plt.title(f'Correlation between Runtime and Rating: {correlation:.2f}')
#plt.show()


correlation = df['Year'].corr(df['Runtime_(Minutes)'])

# Plot a scatter plot for visualization
sns.scatterplot(x='Year', y='Runtime_(Minutes)', data=df)
#plt.title(f'Correlation between Runtime and Rating: {correlation:.2f}')
#plt.show()



correlation = df['Year'].corr(df['Rating'])

# Plot a scatter plot for visualization
sns.scatterplot(x='Year', y= 'Rating', data=df)
#plt.title(f'Correlation between Runtime and Rating: {correlation:.2f}')
#plt.show()



correlation = df['Revenue_(Millions)'].corr(df['Rating'])

# Plot a scatter plot for visualization
sns.scatterplot(x='Revenue_(Millions)', y= 'Rating', data=df)
#plt.title(f'Correlation between Runtime and Rating: {correlation:.2f}')
#plt.show()


correlation = df['Genre'].corr(df['Rating'])

# Plot a scatter plot for visualization
sns.scatterplot(x='Genre', y= 'Rating', data=df)
#plt.title(f'Correlation between Runtime and Rating: {correlation:.2f}')
#plt.show()





















