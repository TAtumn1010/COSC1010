#
# Name Tatumn chavez 
# Date 9/23/24
# Budget Analysis Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program.
#  
# 

#Get the budget for the month.
budget = int(input('What is your budget for the month? '))

# Initialize the accumulator. 
expenditure = 0

# Loop get the weekly expenes . 
for weeks in range(1, 5):
    total = int(input('Enter the expenses for week ' + str(weeks) + ': '))
    expenditure += total

# calculate the total budget used
x = budget - expenditure

#Print the budget used
if expenditure < budget:
    print('This month you saved:', x, 'dollars.')
else:
    print('This month you went over budget by:', abs(x), 'dollars.')





