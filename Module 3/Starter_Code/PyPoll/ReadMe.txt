# python-challenge

#pathway
For both challenges I neededd help with the file path. One I used the tutor and the other I used the AskBCS Learning Assistant. I hope they didn't get messed up with the upload/

PyPoll
The majority of this code was workshopped with the tutor. Once done with her I was able to print the results for the total_votes and the winner. She also left me hints on how to do the rest of the challenge.
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
        
This section of code was explained to me by the tutor. The loop goes through each row of code, and reads the candidate name in column 2. If the name isn't the dictionary it will be added to it. 
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
I had to trial and error this part a lot. 
Part of my logic came from here: https://stackoverflow.com/questions/5306756/how-to-print-a-percentage-value
More came from here: https://www.w3resource.com/python-exercises/python-basic-exercise-37.php
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
