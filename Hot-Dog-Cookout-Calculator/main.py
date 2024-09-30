#
# Name Tatumn chavez
# Date 29/9/24
# Hot Dog Cookout Calculator Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

HOT_DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

# Local Variables
numAttending = 0  # number of people attending
numPerPerson = 0  # The number of hot dogs and buns needed per person
total = 0         # The total number of hot dogs and buns needed
minDogs = 0       # The minimum number of packages of hot dogs
minBuns = 0       # The minimum number of packages of hot dog buns
dogsLeft = 0      # the number of hot dogs left from a pack
bunsLeft = 0      # The number of hot dog buns left over from a pack

# Get the number of people attending the cookout from the user.
numAttending = int(input('Enter the number of people attending the cookout: '))

# Get the number of hot dogs per person from the user
numPerPerson = int(input('Enter the number of hot dogs per person: '))

# Calculate the total number of hot dogs and buns needed
total = numAttending * numPerPerson

# Calculate the minimum number of hot dog packs needed
minDogs = total // HOT_DOGS_PER_PACKAGE

# Calculate the number of hot dogs left over from a package if any
dogsLeft = total % HOT_DOGS_PER_PACKAGE

# If there will be leftover hot dogs, add an additional package of hot dogs
if dogsLeft != 0:
    minDogs += 1

# Determine the total number of hot dogs after considering the additional package
totalDogs = minDogs * HOT_DOGS_PER_PACKAGE

# Calculate the number of hot dogs left over after considering all packages
dogsLeft = totalDogs - total

# Calculate the minimum number of bun packs needed
minBuns = total // BUNS_PER_PACKAGE 

# Calculate the number of hot dogs left over from a package if any
bunsLeft = total % BUNS_PER_PACKAGE 

# If there will be leftover hot dogs, add an additional package of hot dogs
if bunsLeft != 0:
    minBuns += 1

# Determine the total number of hot dogs after considering the additional package
totalBuns = minBuns * BUNS_PER_PACKAGE 

# Calculate the number of hot dogs left over after considering all packages
BunsLeft = totalBuns - total

# Display the minimum packages of hot dogs needed
print('Minimum packages of hot dogs needed:', minDogs)

# Display the number of hot dogs left over
print('Hot dogs left over:', dogsLeft)

# Display the minimum packages of buns needed
print('Minimum packages of Buns needed:', minBuns)

# Display the number of bunsleft over
print('Hot dogs left over:', BunsLeft)
