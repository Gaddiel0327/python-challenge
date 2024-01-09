import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join('Analysis', 'analysis.txt')

LINE_SEP = '-------------------------\n'

with open(csvpath, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    header = next(csvreader)
    
    # Initialize variables
    total_votes = 0
    candidates_votes = {}
    
    # Looping over each row in the CSV file
    for row in csvreader:
        total_votes += 1
    
    # Candidates Column
        candidate_name = row[2]

        if candidate_name in candidates_votes:
            candidates_votes[candidate_name] += 1 
        else:
            candidates_votes[candidate_name] = 1

    
election_results = (
    'Election Results\n'
    f'{LINE_SEP}'
    f'Total Votes: {total_votes}\n'
    f'{LINE_SEP}'
)

for candidate_name in candidates_votes:
    current_candidate_votes = candidates_votes[candidate_name]
    current_candidate_percentage = round(100 * (current_candidate_votes / total_votes), 3) 
    candidate_result =  f'{candidate_name}: {current_candidate_percentage}% ({current_candidate_votes})\n'
    election_results += candidate_result 

winning_votes = max(candidates_votes.values())
for candidate_name in candidates_votes:
    current_candidate_votes = candidates_votes[candidate_name]
    if current_candidate_votes == winning_votes:
        winner_name = candidate_name
        break

election_results += (
   f'{LINE_SEP}'
   f'Winner: {winner_name}\n'
   f'{LINE_SEP}' 
)       



with open(output_path, 'w', encoding='utf-8') as output_file:
    output_file.write(election_results)
    print(election_results)
   