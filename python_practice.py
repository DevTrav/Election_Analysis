#temperature = int(input("What is the temperature outside? "))

#if temperature > 80:
#    print("Turn on the AC.")
#else:
 #   print("Open the windows.")

    # What is the score?
#score = int(input("What is your test score? "))

# Determine the grade.
# if score >= 90:
  #  print('Your grade is an A.')
#elif score >= 80:
  #  print('Your grade is a B.')
#elif score >= 70:
#    print('Your grade is a C.')
#elif score >= 60:
 #   print('Your grade is a D.')
#else:
 #   print('Your grade is an F.')

counties = ["Arapahoe","Denver","Jefferson"]
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#if "El Paso" in counties:
 #   print("El Paso is in the list of counties.")
#else:
 #   print("El Paso is not the list of counties.")
#if "Arapahoe" in counties and "El Paso" not in counties:
#   print("Only Arapahoe is in the list of counties.")
#else:
#    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
    {"county":"Denver", "registered_voters": 463353},
    {"county":"Jefferson", "registered_voters": 432438}]

for county in counties:
    print(county)

x = 0
while x <= 5:
  print(x)
  x = x + 1

# Print items in a list
for i in range(len(counties)):
  print(counties[i]) 

# Get keys of a dictionary
for county in counties_dict.keys():
  print(county)

# Get values of a dictionary 
for voters in counties_dict.values():
  print(voters)

# Get key-value pairs of a Dictionary
for county, voters in counties_dict.items():
  print(f"{county}, has {voters} registered voters.") 

# Get each dictionary in a list of dictionaires
for counties_dict in voting_data:
  print(counties_dict)

# Get key value from list of dictionaries using for loop
for counties_dict in voting_data:
  print(counties_dict['registered_voters'])

# Iterate over a list of dictionaries and print the key value using range()
for i in range(len(voting_data)):
  print(f" Boom!, {voting_data[i]['county']}")
  
# Multiline F-strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)
