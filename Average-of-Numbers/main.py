#
# Name Tatumn Chavez
# Date 11/11/24
#
# COSC 2409 DNT



def Main():
#initializing variables
    total = 0.0
    count = 0

    my_file = open('numbers.txt', 'r')

    # Read the line from the file
    for line in my_file:
        amount = float(line)
        total += amount
        count += 1

    my_file.close()
    
    # Calculate the average:
    average = total / count
    
    print("Total:", total)
    print("Average:", average)

# Call the Main function
Main()
