
#
# Name Tatumn Chavez
# Date21/10/24
## Average of Numbers Programming Project
# COSC 2409 DNT
#

def calculate_average(file_name):
    # Initialize the variables 
    total = 0  
    count = 0  
    # Open file in read mode
    with open(file_name, 'r') as file:
        # Iterate  the file over each line
        for line in file:
# Convert the line to an integer
          total += number  
          number = int(line)  
            total += number  
            count += 1  

    if count == 0:
        return 0 
# Calculate the average
    average = total / count  
    return average 

file_name = 'numbers.txt'
average = calculate_average(file_name)
print("Average:", average)
