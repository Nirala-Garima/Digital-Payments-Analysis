#!/usr/bin/env python
# coding: utf-8

# The Digital India program is a flagship program of the Government of India with a vision to
# transform India into a digitally empowered society and knowledge economy. 
# Digital India promotes cashless transactions and aims to convert India into a cashless society.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("NDAP_REPORT_7072.csv")


# In[3]:


# Display the first few rows of the data for inspection
#Scaling Factor Crores (1,00,00,000INR)
df.head(5)


# In[4]:


# Basic summary statistics of the transaction data
df.describe()


# In[5]:


# Display the data types of each column
df.dtypes


# In[6]:


# Display the number of rows and columns in the dataset
rows, columns = df.shape
print(f"Number of rows: {rows}, Number of columns: {columns}")


# In[7]:


# Check for missing values in each column
missing_values = df.isnull().sum()

# Display the count of missing values in each column
missing_values


# In[32]:


# Use groupby and sum to calculate the sum of transactions for each type and year
grouped_df = df.groupby('Year').agg({
   'Digital Transaction ': 'sum',
   'BHIM transaction': 'sum',
   'Debit Card': 'sum'
}).reset_index()

# Display the grouped DataFrame
print(grouped_df)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(grouped_df['Year'], grouped_df['Digital Transaction '], label='Digital Transaction')
plt.plot(grouped_df['Year'], grouped_df['BHIM transaction'], label='BHIM transaction')
plt.plot(grouped_df['Year'], grouped_df['Debit Card'], label='Debit Card')
plt.xlabel('Year')
plt.ylabel('Sum of Transactions')
plt.legend()
plt.show()



# In[37]:


# Sort the DataFrame by 'Digital Transaction ' in descending order
sorted_digital_df = df.sort_values(by='Digital Transaction ', ascending=False)

# Select the top-performing months for Digital Transaction (e.g., top 5)
top_digital_months = sorted_digital_df.head(5)

# Sort the DataFrame by 'BHIM transaction' in descending order
sorted_bhim_df = df.sort_values(by='BHIM transaction', ascending=False)

# Select the top-performing months for BHIM Transaction (e.g., top 5)
top_bhim_months = sorted_bhim_df.head(5)

# Sort the DataFrame by 'Debit Card' in descending order
sorted_debit_df = df.sort_values(by='Debit Card', ascending=False)

# Select the top-performing months for Debit Card (e.g., top 5)
top_debit_months = sorted_debit_df.head(5)

# Display the top-performing months for each type
print("Top Performing Months - Digital Transaction:")
print(top_digital_months[['MonthCode', 'Month', 'Digital Transaction ']])
print("\nTop Performing Months - BHIM Transaction:")
print(top_bhim_months[['MonthCode', 'Month', 'BHIM transaction']])
print("\nTop Performing Months - Debit Card:")
print(top_debit_months[['MonthCode', 'Month', 'Debit Card']])


# In[44]:


# Convert 'MonthCode' to datetime type
df['MonthCode'] = pd.to_datetime(df['MonthCode'], format='%Y%m')

# Group by 'MonthCode' and calculate the average for each type of transaction
average_df = df.groupby('MonthCode').agg({
    'Digital Transaction ': 'mean',
    'BHIM transaction': 'mean',
    'Debit Card': 'mean'
}).reset_index()


# Plotting as a stacked area chart
plt.figure(figsize=(10, 6))

plt.stackplot(average_df['MonthCode'], average_df['Digital Transaction '], average_df['BHIM transaction'], average_df['Debit Card'],
              labels=['Digital Transaction', 'BHIM transaction', 'Debit Card'], alpha=0.7)

# Formatting
plt.xlabel('Time')
plt.ylabel('Average Transaction Value')
plt.title('Average Transaction Values Over Time')
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()


# In[46]:


# Box Plot Showing the distribution of transactions
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['Digital Transaction ', 'BHIM transaction', 'Debit Card']])
plt.title('Box Plot of Transactions')
plt.ylabel('Transaction Value')
plt.show()


# In[48]:


# Select relevant columns for correlation analysis
Types_of_transaction= ['Digital Transaction ', 'BHIM transaction', 'Debit Card', 'Year']
df_selected = df[Types_of_transaction]

# Calculate the correlation matrix
correlation_matrix = df_selected.groupby('Year').corr()

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap - Digital Transaction, BHIM Transaction, Debit Card Over Years')
plt.show()


# In[ ]:




