# HWA1
CS3910 HWA 1: Data cleaning, reshaping and visualization in Excel &amp; Python

Run the "Assignment 1 with DB.py" file
First you will be asked to input the name of the CSV you want cleaned. 
Be sure to include '.csv' at the end.

The Datacleaning python process BELOW.

1. Read the CSV file into a Dataframe
2. Reshape the dataframe with pandas.melt()
3. Rename the column names in the dataframe
4. Split any joined columns if needed (such as "2011 divorce" into "2011","divorce")
5. Drops the joined column from dataframe once the split is done
6. Gets the current column names and places them into a list.
7. Reorder the columns to preferred order.
8. Apply the ordering to the dataframe
9. Done.

After the csv dataset is processed with Pandas and transformed from Wide to Long format,
you will be asked to create a name for the Output cleaned CSV file.
This will then create a CSV of the cleaned dataframe.

After this, you will be prompted to create a name for a Database.
This will then create a database to put all of the data into.
SQLite3 is used here.

Next, you will be prompted to create a table name in the database, and python will create it.

Once all is complete, the cleaned data that is now in the database will be printed for 
the user to see.
