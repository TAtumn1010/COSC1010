#
# Name Tatumn chavez
# Date 10/28/24
# Exception Handling Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 




def calculate_average(file_name):
    # Initialize the variables
    total = 0 
    count = 0 
    try:
     with open(file_name, 'r') as file:
            
     # Iterate the file over each line
            for line in file:
                try:
                    number = int(line)
                    total += number 
                    count += 1 
                except ValueError:
                    print("Error: Cannot convert value to an integer. Skipping line.")
    except IOError as e:
        print("Error: Could not read the file. Error message:", e)
        return 0

    if count == 0:
        return 0
    # Calculate the average
    average = total / count 
    return average

file_name = 'numbers.txt'
average = calculate_average(file_name)
print("Average:", average)
