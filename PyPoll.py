# Dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total votes counter
total_votes = 0

# Candidate Options
candidate_options = []

# Candidate votes dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Read and print the header row.
    headers = next(file_reader)

#Print ech row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print the tcandidate name from each row
        candidate_name = row[2]

        # If the candidate does not match existing candidate
        if candidate_name not in candidate_options:
            
            # Add it to the list of candidates
            candidate_options.append(candidate_name)

            # Track candidate_votes 
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count    
        candidate_votes[candidate_name] += 1

# Ddetermine percentage of votes for each candidate by looping
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100

    # Print candidate name and percentage
    print(f"{candidate_name} : received {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    if (votes> winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
     # Set winning candidate = candidates name
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
