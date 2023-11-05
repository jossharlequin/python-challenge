import os
import csv

# Define file paths
BankData = os.path.join(".","Resources", "budget_data.csv")
outfile = os.path.join(".","analysis", "bank_analysis.txt")

total_months = 0
total_revenue = 0
profits_losses = []
months = []

with open(BankData, newline='') as infile:
    csv_reader = csv.reader(infile)
    header = next(csv_reader)

    # make variables
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

            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = month
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = month

        total_revenue += revenue
        previous_revenue = revenue

# Calculate the average change
average_change = sum(profits_losses) / (total_months - 1)

# Format results
dollar_total_revenue = "${:,.2f}".format(total_revenue)
dollar_average_change = "${:,.2f}".format(average_change)
dollar_greatest_increase = "${:,.2f}".format(greatest_increase)
dollar_greatest_decrease = "${:,.2f}".format(greatest_decrease)

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