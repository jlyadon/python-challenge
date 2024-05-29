import os
import csv

electiondatapath = os.path.join("Resources","election_data.csv")
votecount = 0
cand_list = []    # A list for candidates' names
cand_votes = []   # A list for each candidate's vote count
cand_pct = []     # A list for each candidate's percentage of the votes
winnercount = 0   # We'll use this to find the winner
winnername = ""   # A placeholder for the winner's name


with open(electiondatapath, 'r') as pypoll:
    csvreader = csv.reader(pypoll, delimiter=',')
    electionheader = next(csvreader)
    for row in csvreader:
# The total number of votes cast:
        votecount += 1
# A complete list of candidates who received votes:
        if row[2] not in cand_list:
            cand_list.append(row[2])
            cand_votes.append(1) # This adds a spot to the count list and counts the new candidate's first vote
            cand_pct.append(0) # This is a placeholder for the candidate's percentage of the votes
# The total number of votes each candidate won:
        elif row[2] in cand_list:
            for i in range(len(cand_list)):
                if cand_list[i] == row[2]:
                    cand_votes[i] += 1

for i in range(len(cand_list)):
# The percentage of votes each candidate won:
    cand_pct[i] = (cand_votes[i] / votecount) * 100
# The winner of the election based on popular vote:
    if cand_votes[i] > winnercount:
        winnercount = cand_votes[i]
        winnername = cand_list[i]
# Your final script should both print the analysis to the terminal and export a text file with the results.

results = f"Election Results\n-------------------------------------------\nTotal Votes: {votecount}\n-------------------------------------------"
for i in range(len(cand_list)):
    results += f"\n{cand_list[i]}: {round(cand_pct[i],3)} ({cand_votes[i]})"
results += f"\n-------------------------------------------\nWinner: {winnername}\n-------------------------------------------"

print("\n" + results + "\n")

textfilepath = os.path.join("Analysis", "election_results.txt")

with open(textfilepath, 'w') as text:
    text.write(results)