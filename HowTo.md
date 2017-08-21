
# How-To Use Python to prepare data sets with missing values for Predix Studio
## Problem 
Data sets are not perfect. Sometimes they end up with invalid, corrupt, or missing values. To [import data into Predix Studio using the data management workbench](https://bitstew.atlassian.net/wiki/spaces/GDDN/pages/101286250/Data+Management+Workbench), you cannot have any values that are null or empty. This How-To will walk you through writing a simple Python script to see if your data set has null or empty values, and if so, it will propose two options for how to modify your data to make it consumable by the Data Management Workbench.

## Dependencies
- [Python](https://www.python.org/downloads/)
- [Python Data Analysis Library (Pandas) ](https://pandas.pydata.org/pandas-docs/stable/install.html#installing-from-pypi)
- A CSV dataset
- Optional: [iPython](https://ipython.org/) interactive shell

## Disclaimers
- This can significantly increase the size of your data set, because you are adding values to it. With large data sets, the pandas commands can take time.
- These may not be the best solutions for your data. For more information on other ways to handle missing data with pandas, please refer to [Handling missing data](https://pandas.pydata.org/pandas-docs/stable/missing_data.html)

##Other Resources 
I used [this](https://www.kaggle.com/usdot/flight-delays) kaggle data set to perform these operations, and it includes some more instructions on using Pandas and other Python libraries to explore your data


## Steps
The following steps can be written in a Python script and run at once, but I find it more interesting to explore in an interactive Python shell like [iPython](https://ipython.org/)
### Solution 1: Replace empty/null values with Space
1. Import pandas `import pandas as pd`
2. Import csv into a Pandas [DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) object `flights = pd.read_csv('flights.csv')`
3. Check the shape of your data in (rows, columns) format `flights.shape`
3. (Optional) Check for all null values in your dataset. This will return a boolean stating if each cell is null. This can take a long time and may not be particularly useful in a very large dataset. `flights.isnull()`
4. Explore how many null values are in each column of your dataset `flights.isnull().sum()`
5. (Optional) Check how many null values are in a specific column, substituting the name of your column in string form where it says 'col' `flights[col].isnull().sum()`
6. Fill all null or empty cells in your original DataFrame with an empty space and set that to a new DataFrame variable, here, called 'modifiedFlights'*. ( `modifiedFlights=flights.fillna(“ “)`
7. Verify that you no longer have any null values by running `modifiedFlights.isnull().sum()`
8. Save your modified dataset to a new CSV, replacing 'modifiedFlights.csv' with whatever you would like to name your new file. `modifiedFlights.to_csv('modifiedFlights.csv')`
*If you wish, you can replace your original DataFrame, using `flights=flights.fillna(" ")`

### Solution 2: Remove rows with empty values
1. Import pandas `import pandas as pd`
2. Import csv into a Pandas [DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) object `flights = pd.read_csv('flights.csv')`
3. Check the shape of your data in (rows, columns) format `flights.shape`
3. (Optional) Check for all null values in your dataset. This will return a boolean stating if each cell is null. This can take a long time and may not be particularly useful in a very large dataset. `flights.isnull()`
4. Explore how many null values are in each column of your dataset `flights.isnull().sum()`
5. (Optional) Check how many null values are in a specific column, substituting the name of your column in string form where it says 'col' `flights[col].isnull().sum()`
6. If only a few null values and you know that deleting values will not cause adverse effects on your result, remove them from your DataFrame and store that in a new DataFrame* `modifiedFlights = flights.dropna()`
7. Verify that you no longer have any null values by running `modifiedFlights.isnull().sum()`
8. Save your modified dataset to a new CSV, replacing 'modifiedFlights.csv' with whatever you would like to name your new file. `modifiedFlights.to_csv('modifiedFlights.csv')`
*If you wish, you can replace your original DataFrame, using `flights=flights.dropna()`


