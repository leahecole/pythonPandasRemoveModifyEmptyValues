# How-To Use Python to Remove or Modify Empty Values in a CSV Dataset
## Problem 
Data sets are not perfect. Sometimes they end up with invalid, corrupt, or missing values. For the project I was working on, I could not have any values that are null or empty. This How-To will walk you through writing a simple Python script to see if your data set has null or empty values, and if so, it will propose two options for how to modify your data.

### Example
This simple data set shows you a flight and tells you its airline, flight number, and the reason it was cancelled. However, if a flight wasn't cancelled, it will have no cancelled reason, and therefore has a null/empty value.

**Example of CSV missing data in excel** - there is no "Cancelled Reason" for AwesomeAir flight 456:
![CSV with missing data in one cell](https://github.com/leahecole/pythonPandasRemoveModifyEmptyValues/blob/master/images/excel.png)


**Example of same CSV missing data in traditional comma-separated format** - there is no "Cancelled Reason" for AwesomeAir flight 456:
![csv in terminal with one value missing](https://github.com/leahecole/pythonPandasRemoveModifyEmptyValues/blob/master/images/csv.png) 


## Dependencies
- [Python](https://www.python.org/downloads/)
- [Python Data Analysis Library (Pandas) ](https://pandas.pydata.org/pandas-docs/stable/install.html#installing-from-pypi)
- A CSV dataset
- Optional: [iPython](https://ipython.org/) interactive shell

## Disclaimers
- This can significantly increase the size of your data set, because you are adding values to it. With large data sets, the pandas commands can take time.
- These may not be the best solutions for your data. For more information on other ways to handle missing data with pandas, please refer to [Handling missing data](https://pandas.pydata.org/pandas-docs/stable/missing_data.html)

## Other Resources 
I used [this](https://www.kaggle.com/usdot/flight-delays) kaggle data set to perform these operations, and it includes some more instructions on using Pandas and other Python libraries to explore your data


## Steps
The following steps can be written in a Python script and run at once, but I find it more interesting to explore in an interactive Python shell like [iPython](https://ipython.org/)

If you want to see what the scripts look like all together, please check out [Solution 1](https://github.com/leahecole/pythonPandasRemoveModifyEmptyValues/blob/master/solution1.py) and [Solution 2](https://github.com/leahecole/pythonPandasRemoveModifyEmptyValues/blob/master/solution2.py). Otherwise, keep reading and follow along step by step.

1. Import pandas `import pandas as pd`
2. Import csv into a Pandas [DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) object `flights = pd.read_csv('flights.csv')`
3. Check the shape of your data in (rows, columns) format `flights.shape`
3. (Optional) Check for all null values in your dataset. This will return a boolean stating if each cell is null. This can take a long time and may not be particularly useful in a very large dataset. `flights.isnull()`
4. Explore how many null values are in each column of your dataset `flights.isnull().sum()`
5. (Optional) Check how many null values are in a specific column, substituting the name of your column in string form where it says 'col' `flights[col].isnull().sum()`

At this point, you will either [replace your values with a space](#sol1) or [remove them entirely](#sol2)
### Solution 1: Replace empty/null values with Space <a id="sol1"></a>

7. Fill all null or empty cells in your original DataFrame with an empty space and set that to a new DataFrame variable, here, called 'modifiedFlights'*. `modifiedFlights=flights.fillna(“ “)`
8. Verify that you no longer have any null values by running `modifiedFlights.isnull().sum()`
9. Save your modified dataset to a new CSV, replacing 'modifiedFlights.csv' with whatever you would like to name your new file. `modifiedFlights.to_csv('modifiedFlights.csv',index=False)`

*If you wish, you can replace your original DataFrame, using `flights=flights.fillna(" ")`

### Solution 2: Remove rows with empty values <a id="sol2"></a>
7. If there are only a few null values and you know that deleting values will not cause adverse effects on your result, remove them from your DataFrame and store that in a new DataFrame* `modifiedFlights = flights.dropna()`
8. Verify that you no longer have any null values by running `modifiedFlights.isnull().sum()`
9. Save your modified dataset to a new CSV, replacing 'modifiedFlights.csv' with whatever you would like to name your new file. `modifiedFlights.to_csv('modifiedFlights.csv',index=False)`

*If you wish, you can replace your original DataFrame, using `flights=flights.dropna()`


