# import dataset
import os
import csv

# Create file path
budget_data = os.path.join("/Users\mzimerma\Desktop\PythonStuff\python-challenge\PyBank", "Resources", "budget_data.csv")

# Create variables
total_months = 0
total_revenue = 0
sum_revenue_change = 0

# Open and read CSV
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header row   
    header = next(csvreader)
    # print(header)

    for row in csvreader:
        print(row[1])

# Find total # of months in dataset

# Find net total amount of Profit/Losses

# Average of changes in Profit/Losses

# Greatest increase in profits (date/amount) 

# Greatest decrease in losses (date/amount)

# Display information
print ("Financial Analysis")
print("---------------------")
