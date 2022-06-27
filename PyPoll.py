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

# Print Candidate Options list
print(candidate_options)
