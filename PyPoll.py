# The data we need to retrieve.
# 1. The total number of votes cast. 
# 2. A complete list of candidates who received votes. 
# 3. The percentage of votes each candidate won. 
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote. 

# Import the csv and os modules # os module is used for indirect path to file

# add dependancies.
import csv
import os

# assign variable to load pile from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#declare the accumulator - total votes counter - and initialize the variable to 0
total_votes = 0

# declare a new list for candidate names
candidate_options = []

# Declare an empty dictionary to count and store votes for candidates
candidate_votes = {}

#Winning candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with tthe reader function.
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # get candidate name
        candidate_name = row[2]
        
        #Conditional for adding candidate names that are not on the list
        if candidate_name not in candidate_options:
            
            # add candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count, set outside the if conditional
        candidate_votes[candidate_name] += 1
    
# Determine the percentage of votes for each candidate by looping through the counts
for candidate_name in candidate_votes:
    
    # Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]

    # Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100 
    
    # Print the candidate name and percentage of votes
    print(f"{candidate_name}: received {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true, then set the winning_count = votes and winning_percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # Set the winning_candidate equal to candidate_name
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
)
print(winning_candidate_summary)
   
