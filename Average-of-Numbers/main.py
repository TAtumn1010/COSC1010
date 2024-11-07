
#
# Name Tatumn Chavez
# Date21/11/6
## Average of Numbers Programming Project
# COSC 2409 DNT
#

#
# Name Tatumn Chavez
# Date21/10/24
#
# COSC 2409 DNT
#


# Open the file 

num_file = open('numbers.txt', 'r')


# Read  the line from the file

num1 = int(num_file.readline())
num2 = int(num_file.readline())
num3 = int(num_file.readline())

#close the file

num_file.close()


# Calculate the sum  and avege of the three numbers

sum = num1 + num2 + num3
average = sum / 3


# Print statement

print(num1, num2, num3)
print(average)




