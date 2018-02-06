import os
import csv

budget_data_1_csv = os.path.join("Resources", "budget_data_1.csv")
budget_data_2_csv = os.path.join("Resources", "budget_data_2.csv")

# Declare variables to store data
date = []
revenue = []
revenue_delta = []
total_months = 0
total_revenue = 0
total_revenue_delta = 0
average_change = 0
max_increase_date = ""
max_increase = 0
max_decrease_date = ""
max_decrease = 0
header_skipped = False

with open(budget_data_2_csv, "r", newline="") as csvfile_2:
    csvreader= csv.reader(csvfile_2, delimiter=",")
    for row in csvreader:
        if header_skipped == True:
            # Add date from csv
            date.append(row[0])

            # Add revenue from csv
            revenue.append(row[1])
			
			# Sum each month of revenue to total_revenue
            total_revenue += int(row[1])
            
            if len(revenue) >= 2:
				# Take the difference between revenue months to find change in revenue per month
                revenue_delta.append(int(revenue[-1]) - int(revenue[-2]))
                total_revenue_delta += (int(revenue[-1]) - int(revenue[-2]))
            if int(row[1]) > max_increase:
                max_increase = int(row[1])
                max_increase_date = row[0]
            if int(row[1]) < max_decrease:
                max_decrease = int(row[1])
                max_decrease_date = row[0]
        header_skipped = True

total_months = len(date)
average_change = total_revenue_delta / len(revenue_delta)
	
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: " + str('${:,.2f}'.format(total_revenue)))
print("Average Revenue Change: " + str('${:,.2f}'.format(average_change)))
print("Greatest Increase in Revenue: " + str(max_increase_date) + " " + str('${:,.2f}'.format(max_increase)))
print("Greatest Decrease in Revenue: " + str(max_decrease_date) + " " + str('${:,.2f}'.format(max_decrease)))


# Set variable for output file
output_file = os.path.join("financial_analysis.txt")

with open(output_file, "w", newline="\r\n") as text_file:
	line1 = "Financial Analysis"
	line2 = "----------------------------"
	line3 = "Total Months: " + str(total_months)
	line4 = "Total Revenue: " + str("${:,.2f}".format(total_revenue))
	line5 = "Average Revenue Change: " + str('${:,.2f}'.format(average_change))
	line6 = "Greatest Increase in Revenue: " + str(max_increase_date) + " " + str('${:,.2f}'.format(max_increase))
	line7 = "Greatest Decrease in Revenue: " + str(max_decrease_date) + " " + str('${:,.2f}'.format(max_decrease))
	text_file.write("{}\n{}\n{}\n{}\n{}\n{}\n{}".format(line1,line2,line3,line4,line5,line6,line7))