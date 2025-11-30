Use this readme file to track your own learning (see learning journal example)
# Learning Journal - Data Analysis Fundamentals

## What is a Learning Journal?

This learning journal is your personal space to document your journey through the Data Analysis Fundamentals course. Use it to:

- Record new concepts you've learned
- Keep track of useful code snippets
- Document challenges and how you overcame them
- Note questions for later follow-up
- Reflect on your progress and understanding

Maintaining this journal will help you solidify your knowledge and serve as a valuable reference after the course ends.

## Journal Entry Template

### Session Date: [Date]

#### Today I learned:
- Notebook LM use for queries on private PDF https://notebooklm.google.com/notebook/37801a59-95cf-4d29-b8eb-13fe0d14f0ea?pli=1
- public legit packages https://pypi.org/
- use seaborn for ML
- sk-learn next
- tenserflow for neuron network
- data.world
- when merging, set indicator = True
- .melt to reverse the pivoting (reverse the long format)
- set column.names = none  (long to wide and wide to long)
- one hot encoding.
- local average vs rolling average
- marimo.app, variable graph, dependency execution, sql injection :)


#### Code snippets I want to remember:
```python
# Example code here
```

#### Challenges I faced:
- 
- 

#### Questions I still have:
- 
- 

#### Next steps for practice:
- 
- 

## Example Entry

### Session Date: October 27, 2025

#### Today I learned:
- How to import data from Excel files using pandas
- How to perform basic data exploration (head, describe, info)
- How to filter data using conditions

#### Code snippets I want to remember:
```python
# Loading data from Excel
import pandas as pd

# Read an Excel file
df = pd.read_excel('sales_data.xlsx')

# Basic exploration
print(df.head())  # View first 5 rows
print(df.describe())  # Summary statistics
print(df.info())  # Column info and data types

# Filtering data
high_value = df[df['amount'] > 1000]
recent_sales = df[df['date'] > '2025-01-01']
```

#### Challenges I faced:
- Had trouble understanding the difference between loc and iloc
- Wasn't sure how to handle missing values in my dataset

#### Questions I still have:
- What's the best way to visualize my sales data?
- How can I automate data cleaning for my weekly reports?

#### Next steps for practice:
- Try creating different types of charts with matplotlib
- Apply what I learned to my own work data
- Complete the broccoli exercises in homework 1

## How to Use This Journal

1. Create a new entry after each class session
2. Record key concepts in your own words
3. Include helpful code examples
4. Note any challenges or questions
5. Review previous entries regularly to reinforce learning

Remember, this journal is for you - feel free to customize it to best support your learning style!



Tips:
#Importing the TB data dictionary into Python and showing the 2 columns 'variable_name' and 'definition'.

import csv

Tbdata_dict = {}

with open("../data/TB_data_dictionary_2025-11-24.csv") as file:
reader = csv.DictReader(file)
for row in reader:
Tbdata_dict[row["variable_name"]] = row["definition"]

#How to see the whole dictionary:Tbdata_dict

#How to look up a abbreviation: 
Tbdata_dict["cfr"]

Fiona 18:26
#Creating the Bubble Maps for 'Incidence per 100 000 Inhabitants'
fig_incidence = px.scatter_geo(df_tbworld_cleaned,
locations="iso3", #Country codes in ISO-3 format
color="estimated_incidence_per_100k", #Color by estimated incidence per 100k
size="estimated_incidence_per_100k", #Size of the bubble
hover_name="country", #Displays the country name and Infos
animation_frame="year",
size_max=40, #Max size of the bubbles
projection="natural earth",
title="Estimated Incidence of TB per 100,000 Inhabitants (2000-2024)",
color_continuous_scale='YlOrRd', #Color scale from yellow to red)
width=1300,
height=800,
template="plotly_dark" ) #Dark background so bubbles are better visible

fig_incidence.show()