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
#Remove all null values
flights=flights.dropna()
#Store the dataframe as a new CSV
flights.to_csv('new.csv',index=False)
