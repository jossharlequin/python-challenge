PyBank
import os
import csv

# Define file paths
I originally did (".","Resources", "budget_data.csv") here but it dodn't work.
BankData = os.path.join("Resources", "budget_data.csv")
outfile = os.path.join("analysis", "bank_analysis.txt")

The first variable here was lifted from PyPoll. I then just renamed them. total_months = total_votes. 
total_months = 0
The net profit/loss came from her; https://stackoverflow.com/questions/4841436/what-exactly-does-doe
total_revenue = 0
profits_losses = []
months = []

with open(BankData, newline='') as infile:
    csv_reader = csv.reader(infile)
    header = next(csv_reader)

    # make variables
Previous_Revenue code came from here: https://stackoverflow.com/questions/53474110/python-determine-change-in-value-from-one-period-to-the-next
The first one starts the Previous_Revenue at 0
    previous_revenue = 0
    greatest_increase = 0
    greatest_decrease = 0

    for row in csv_reader:
        total_months += 1
        month = row[0]
        revenue = int(row[1])

        # Calculate previous month and current month
        if total_months > 1:
            change = revenue - previous_revenue
            profits_losses.append(change)
            months.append(month)

This part looks at the change variable. It stores the change in greatest_increase, and visa versa, if the change is larger than the current greatest, that variable is updated and the month is stored. If not, it just passes through.
This youtube video had code help: https://www.youtube.com/watch?v=uN5EeC2ClEc
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = month
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = month

This Total_Revenue takes the value of the revenue and adds it to the revenue amount it has in the next loop.
        total_revenue += revenue
The Previous_Revenue takes on the current revenue amount and holds it for the next loop.
        previous_revenue = revenue

# Calculate the average change
This is a standard average formula
average_change = sum(profits_losses) / (total_months - 1)

# Format results
Formatting help: https://www.geeksforgeeks.org/python-output-formatting/
dollar_total_revenue = "${:,.2f}".format(total_revenue)
dollar_average_change = "${:,.2f}".format(average_change)
dollar_greatest_increase = "${:,.2f}".format(greatest_increase)
dollar_greatest_decrease = "${:,.2f}".format(greatest_decrease)

This is where it prints the info.
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: {dollar_total_revenue}\n"
    f"Average Change: {dollar_average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} ({dollar_greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} ({dollar_greatest_decrease})\n"
)

with open(outfile, "w") as out_file:
    out_file.write(output)

print(output)
