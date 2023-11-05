import os
import csv

#pathway
PollData = os.path.join(".","Resources","election_data.csv")
outfile = os.path.join(".","analysis","election_analysis.txt")

#variables
total_votes = 0
l_candidates = []
d_candidates = {}

with open(PollData, newline='') as infile:
    csv_reader = csv.reader(infile)
    header = next(csv_reader)

    for row in csv_reader:
        total_votes = total_votes + 1
        candidate = row[2]
        
        if candidate not in l_candidates:
            l_candidates.append(candidate)
            d_candidates[candidate] = 0
        d_candidates[candidate] = d_candidates[candidate] + 1

#gets winner
winner = ""
winner_votes = 0

for candidate, votes in d_candidates.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

output = (
    f"Election Results\n"
    f"-----------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-----------------------\n"
)
#this part lists the candidate results
for candidate, votes in d_candidates.items():
    percentage = (votes / total_votes) * 100
    output += f"{candidate}: {percentage:.3f}% ({votes})\n"

output += (
    f"-----------------------\n"
    f"Winner: {winner}\n"
)
with open(outfile,"w") as out_file:
    print(output)
    out_file.write(output)