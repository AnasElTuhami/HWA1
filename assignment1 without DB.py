import pandas as pd
import numpy as np

## START ##

# Reads the csv file and places into a Dataframe
df = pd.read_csv('csv_dataset.csv')

#Reshapes from Wide to Long format
df = pd.melt(df, id_vars=['State'])

#Renames the Column names
df.columns = ['State','Type','Rate']

#Splits the "2011 Divorce" into "Year" and "Event" columns
df['Year'], df['Event'] = df['Type'].str.split(' ', 1).str

#Drops the original un-split column
df = df.drop(['Type'], axis=1)

#Gets the column names and places into a list
cols = df.columns.tolist()

#Re-order the list of columns to preferred order
reorderColumn = cols[:1] + cols[2:] + cols[1:2]

#Applies the column ordering to the dataframe
df = df[reorderColumn]

print(df)


