# python-challenge
Challenge for Module 03

# PyBank

This folder contains the resources and analysis for the provided financial data.

## main.py

This file is a python application that reads data from Resources\budget_data.csv and returns:
    - the total number of months in the dataset
    - the total profits or losses over the period
    - the average change in profits or losses from month to month
    - the date and amount of the greatest increase
    - the date and amount of the greatest decrease.
The application also writes those results into a .txt file and creates a new .csv file that includes the original data plus the monthly changes in profits or losses. These files are placed in PyBank\Analysis.

## Resources

### budget_data.csv

This .csv file is the original data which PyBank\main.py analyzes.

## Analysis

Analysis is the output directory for PyBank\main.py. Running main.py again will overwrite these files.

### budget_data_updated.csv

A new .csv that incudes all the information in budget_data.csv, plus a third column for monthly changes.

### budget_analysis_results.txt

A .txt file with the results of the financial analysis. PyBank\main.py will also print these results to the terminal.

# PyPoll

This folder contains the resources and analysis for the provided election data.

## main.py

This python application analyzes Resources\election_data.csv and returns
    - the total number of votes cast in the election
    - the names of the candidates
    - the percentage of the votes each candidate received
    - the number of votes each candidate received
    - the winner of the election
The application also writes those results into a text file stored in PyPoll\Analysis

## Resources

### election_data.csv

This file contains the provided election data for analysis by PyPoll\main.py.

## Analysis

Analysis is the output directory for PyPoll\main.py. Running the application again will overwrite these files.

### election_results.txt

This file contains the results of the analysis of PyPoll\main.py. The application also prints these results to the terminal.