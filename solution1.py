import pandas as pd
#Read the csv into a Pandas DataFrame
flights = pd.read_csv('flights.csv')
#Examine the shape of the data
flights.shape
#Explore null cells
flights.isnull()
#View total of null values by column
flights.isnull().sum()
#View the number of null values in the 'TAXI_OUT' column
flights['TAXI_OUT'].isnull().sum()
#Fill all null values with a space, and score that in the current data frame
flights=flights.fillna(" ")
#Store the dataframe as a new CSV
flights.to_csv('new.csv', index=False)
