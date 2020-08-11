# Import data
import os
import csv

# Variables for vote count
candidates = []
num_votes = 0
vote_counts = []

# Loop file
election_data = os.path.join("Resources", "election_data.csv")

for files in election_data:
   
    # Read CSV
    with open(election_data) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        row = next(csvreader,None)

        # Process the votes
        for row in csvreader:
            num_votes = num_votes + 1
            candidate = row[2]

            # If the candidate has other votes then add to vote total
            if candidate in candidates:
                candidate_index = candidates.index(candidate)
                vote_counts[candidate_index] = vote_counts[candidate_index] + 1
            # Else create new spot in list for candidate
            else:
                candidates.append(candidate)
                vote_counts.append(1)

    # Variables for percentages
    percentages = []
    max_votes = vote_counts[0]
    max_index = 0

    # Percentage of vote for each candidate and overall winner
    for count in range(len(candidates)):
        vote_percentage = format((vote_counts[count]/num_votes*100), '.3f')
        percentages.append(vote_percentage)
        if vote_counts[count] > max_votes:
            max_votes = vote_counts[count]
            print(max_votes)
            max_index = count
    winner = candidates[max_index]

    # Print results
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {num_votes}")
    for count in range(len(candidates)):
        print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
    print("---------------------------")
    print(f"Winner: {winner}")
    print("---------------------------")

    #Export to .txt file
    with open("Analysis/PyPoll.txt", "w") as analysis:
        analysis.write("Election Results\n")
        analysis.write("---------------------\n")
        analysis.write(f"Total Votes: {num_votes}\n")
        analysis.write("---------------------\n")
        for count in range(len(candidates)):
            analysis.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
        analysis.write("---------------------\n")
        analysis.write(f"Winner: {winner}\n")
        analysis.write("---------------------\n")
    