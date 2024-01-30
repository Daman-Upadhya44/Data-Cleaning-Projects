#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Import Librbary for code
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[79]:


## import CSV file
df = pd.read_csv("C:\\Users\\Daman\\Downloads\\Support Hours Calculation.csv")
df


# In[ ]:


## basic information for dataframe
df.info()
df.describe()
df.head()
df.tail()
##display all the rows and column from dataframe 
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
##Shape of Dataframe 
df.shape


# ###### Data Cleaning steps (duplicates remove,null values remove,datatype change )

# In[21]:


## Remove duplicate from Dataframe 
df["Title"] = df["Title"].drop_duplicates()

## Find null values from dataframe 
df.isnull().sum()

##List of rows which have Null values in columns
df[df['Spent Hours'].isna()==1]

## drop null value from dataframe from perticular column 
df.dropna(subset = ["Spent Hours"])

##  Drop null values from dataframe 
df.drop(["Mace Category","Report Category","Support Rep"],axis=1)

# Assuming df is your DataFrame and 'column_name' is the column you want to convert
df['Spent Hours'] = pd.to_numeric(df['Spent Hours'], errors='coerce') # The 'errors' parameter is set to 'coerce', which means invalid parsing will be set as NaN



# ###### Data Cleaning steps (Correct String values, remove unwated charactor , split ,marged columns )

# In[69]:


## Remove unwated charactor from left right or between the string 
df['Title'] = df['Title'].str.strip('N_123')
df['Title'] = df['Title'].str.lstrip('_')
df['Title'] = df['Title'].str.rstrip('_')

## Replace values with other
df['Type'] = df['Type'].replace(to_replace='PowerBI Reports', value='PBI')

##replace multiple values from columns
replacement_dict = {'PowerBI Reports': 'PBI', 'Project Setup': 'Setup'}
df['Type'] = df['Type'].replace(to_replace=replacement_dict)

## rename columns Title name 
df.rename(columns = {'Title':'Title_Name'})

# Assuming df is your DataFrame and 'Spent Hours' is the column you want to split
df['Spent Hours'] = df['Spent Hours'].astype(str)  # Convert to string
df[['Hour', 'Minutes']] = df['Spent Hours'].str.split('.', expand=True)

# Assuming df is your DataFrame and 'Matches' is the column you want to split and keep only first part
df['Title'] = df['Title'].str.split('*').str[0]

# Change type again into numaric 
df['Minutes'] = pd.to_numeric(df['Minutes'], errors='coerce')# The 'errors' parameter is set to 'coerce', which means invalid parsing will be set as NaN
df['Hour'] = pd.to_numeric(df['Hour'], errors='coerce')# The 'errors' parameter is set to 'coerce', which means invalid parsing will be set as NaN



# In[ ]:


# Change type of column from object to int by  finding and removing null values
df[df['Hour'].isna()==1]
df = df.dropna(subset='Hour')
df['Hour'] = df['Hour'].astype('int')
df.info()


# In[90]:


df['Actual Finish'] = pd.to_datetime(df['Actual Finish'],errors='coerce')
df['Target Date'] = pd.to_datetime(df['Target Date'], errors='coerce')
df['Request Received On'] = pd.to_datetime(df['Request Received On'], errors='coerce')


# In[ ]:





# In[ ]:




