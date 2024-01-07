# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Setting to 0 total months, total profit 
total_months = 0
total_pnl = 0


# Setting to find the average change
changes = []


# Method 2: Improved Reading using CSV module (Used some part of this script from a module)

with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row if it exists
    next(csvreader)

    #Setting to None incase no previous profit/losses
    previous_pnl = None

    # Converting Data as List
    for row in csvreader:
        total_months += 1
        profit_loss = int(row[1])
        total_pnl += profit_loss
        if previous_pnl is not None:
            change = profit_loss - previous_pnl
            changes.append(change)
        previous_pnl = profit_loss



average_change = sum(changes) / len(changes)


#Making sure Greatest Increase and Decrease resets to zero when it it loops
greatest_increase = 0
greatest_decrease = 0
greatest_increase_date = ""
greatest_decrease_date = ""

with open(csvpath, 'r') as file:
    csv_reader = csv.reader(file)
   
    #Skipping the first row for the header
    header = next(csv_reader)

    #Looping to find the greeatest increase and decrease 
    for row in csv_reader:
        profit_loss = int(row[1])
        
        if previous_pnl is not None:
            change = profit_loss - previous_pnl
            
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]
                
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]
        
        previous_pnl = profit_loss




print("Total Months:", total_months)
print(f"Net Profit/Losses:, ${total_pnl}")
print(f"Average Change:, ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")