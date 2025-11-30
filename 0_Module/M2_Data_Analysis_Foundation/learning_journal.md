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
