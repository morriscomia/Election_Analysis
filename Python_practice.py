# Election_analysis
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':        
    print(counties[1])
if counties[2] != 'Jefferson':
    print(counties[2])


temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

temperature = int(input("What is the temperature outside? "))
print("What is the temperature outside?")
#What is the temperature?

score = int(input("What is your test score? "))
# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
     if score >= 80:
          print('Your grade is a B.')
     else:
         if score >= 70:
             print('Your grade is a C.')
         else:
            if score >= 60:
                 print('Your grade is a D.')
            else:
                    print('Your grade is an F.')
                 
# What is the score?
score = int(input("What is your test score?"))
# Determine the grade.
if score >= 90:
     print('Your grade is an A.')
elif score >= 80:
     print('Your grade is a B.')
elif score>= 70:
    print ('Your grade is C')
elif score >= 60:
    print ('Your grade is D')
else:
    print('Your grade is an F.')

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
      print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

x = 0
while x <= 5:
    print(x)
    x = x + 1
count = 7
while count < 1:
       print("Hello World")
for county in counties:
    print(county)
numbers = [0, 1, 2, 3, 4]
for num in numbers:
        print(num)
for num in range(5):
    print(num)


for i in range(len(counties)):
    print(counties[i])
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
for voters in counties_dict.values():
     print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
     print(counties_dict.get(county))

for key, value in counties_dict.items():
    print(key, value)
for county, voters in counties_dict.items():
    print(county, voters)
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
     print(county_dict)
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)        
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
#F string
print(f"I received {my_votes / total_votes * 100}% of the total votes.")
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
#For F-string
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")
print(message_to_candidate)


f'{value:{width}.{precision}}'
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)


# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

file_variable = open(filename, mode)
