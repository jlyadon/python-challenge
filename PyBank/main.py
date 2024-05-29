import csv
import os
budgetdatapath = os.path.join("Resources","budget_data.csv")

with open(budgetdatapath, 'r') as pybank:
    csvreader = csv.reader(pybank, delimiter=',')
    budgetheader = next(csvreader)
    tot_mos=0      # total months covered
    tot_prof=0     # total net profits/losses
    prev_prof=0    # profits from the previous month
    tot_change=0   # total change in profits, to be averaged
    gr_inc=0       # the greatest increase
    gr_inc_date="" # the date of the greatest increase
    gr_dec=0       # the greatest decrease
    gr_dec_date="" # the date of the greatest decrease

    dates = ["Date"]
    profits = ["Profits/Losses"]            # initializing lists to zip together into a new csv file
    monthly_changes = ["Monthly Change"]

    for row in csvreader:
        dates.append(row[0])
        profits.append(row[1])
        tot_mos += 1
        tot_prof += int(row[1])
        if prev_prof != 0 and row[1] != "": # these conditions keep us from adding values at the ends
            tot_change += int(row[1]) - prev_prof
            monthly_changes.append(int(row[1]) - prev_prof)
        if int(row[1]) - prev_prof > gr_inc:
            gr_inc = int(row[1]) - prev_prof
            gr_inc_date = row[0]
        elif int(row[1]) - prev_prof < gr_dec:
            gr_dec = int(row[1]) - prev_prof
            gr_dec_date = row[0]
        prev_prof = int(row[1]) # Before moving on: the value on this row is now the prev. row
    avg_change = tot_change / (tot_mos - 1) # We use tot_mos - 1 to calculate the average because we can't include the first month in this calculation (we don't have data on the previous month).

# Write a new csv file with the monthly changes in it:
outputpath = os.path.join("Analysis", "budget_data_updated.csv")
outputdata = zip(dates, profits, monthly_changes)

with open(outputpath, 'w', newline = "") as output: # Thanks to Kian Layson for the insight about the newline parameter.
    csvwriter = csv.writer(output, delimiter=',')
    for line in outputdata:
        csvwriter.writerow([line[0], line[1], line[2]])

# Your final script should both print the analysis the the terminal and export a text file with the results.
results = f"Financial Analysis\n------------------\nTotal Months: {tot_mos}\nTotal: ${tot_prof}\nAverage Change: ${round(avg_change,2)}\nGreatest Increase in Profits: {gr_inc_date} (${gr_inc}) \nGreatest Decrease in Profits: {gr_dec_date} (${gr_dec})"

print("\n" + results + "\n")

textfilepath = os.path.join("Analysis", "budget_analysis_results.txt")

with open(textfilepath,'w') as text:
    text.write(results)