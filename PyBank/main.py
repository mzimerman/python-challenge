# import dataset
import os
import csv

# Create file path
budget_data = os.path.join("Resources", "budget_data.csv")

# Create variables
total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

# Opening and reading the CSV file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Reading the header row
    header = next(csvreader)

    # Reading the first row (so that we track the changes properly)
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    
    # Going through each row of data after the header & first row 
    for row in csvreader:
        # Keeping track of the dates
        dates.append(row[0])
               
        # Calculate the change, then add it to list of changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        # Find total # of months in dataset
        total_months += 1

        # Find net total amount of Profit/Losses
        total_pl = total_pl + int(row[1])

    # Greatest increase in profits (date/amount)
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    # Greatest decrease in losses (date/amount)
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    # Average of changes in Profit/Losses
    avg_change = sum(profits)/len(profits)
    

#Displaying information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

#Export to .txt file
with open("Analysis/PyBankl.txt", "w") as analysis:
    analysis.write("Financial Analysis\n")
    analysis.write("---------------------\n")
    analysis.write(f"Total Months: {str(total_months)}\n")
    analysis.write(f"Total: ${str(total_pl)}")
    analysis.write(f"Average Change: ${str(round(avg_change,2))}")
    analysis.write(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
    analysis.write(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
