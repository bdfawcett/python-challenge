import os
import csv
import operator

election_data_1_csv = os.path.join("Resources", "election_data_1.csv")
election_data_2_csv = os.path.join("Resources", "election_data_2.csv")

# Declare variables to store data

total_votes = 0
candidates = {}
header_skipped = False

with open(election_data_2_csv, "r", newline="") as csvfile_2:
	csvreader= csv.reader(csvfile_2, delimiter=",")
	for row in csvreader:
		if header_skipped == True:
			if row[2] not in candidates.keys():
				candidates[row[2]] = 1
			else:
				candidates[row[2]] += 1
			total_votes += 1
		header_skipped = True
		
print("Election Results")
print("-------------------------")
print("Total Votes: " + str('{:,.0f}'.format(total_votes)))
print("-------------------------")
for key, value in candidates.items():
    print(str(key) + ":" , "{0:.1f}%".format(value/total_votes*100), "("+ str('{:,.0f}'.format(value) + ")"))
print("-------------------------")
print("Winner: " + str(max(candidates.items(), key=operator.itemgetter(1))[0]))
print("-------------------------")

# Set variable for output file
output_file = os.path.join("election_results.txt")

with open(output_file, "w", newline="\r\n") as text_file:
	line1 = "Election Results"
	line2 = "-------------------------"
	line3 = "Total Votes: " + str('{:,.0f}'.format(total_votes))
	line4 = "-------------------------\n"
	text_file.write("{}\n{}\n{}\n{}".format(line1,line2,line3,line4))
	for key, value in candidates.items():
		text_file.write(str(key) + ": " + "{0:.1f}%".format(value/total_votes*100) + " ("+ str('{:,.0f}'.format(value) + ")\n"))
	line5 = "-------------------------"
	line6 = "Winner: " + str(max(candidates.items(), key=operator.itemgetter(1))[0])
	line7 = "-------------------------"
	text_file.write("{}\n{}\n{}".format(line5,line6,line7))