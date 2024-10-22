#
# Name Tatumn chavez 
# Date 21/10/24
# File Display Programming Project
# COSC 2409 DNT
#
# main function

# open the file
myfile = open('numbers.txt', 'r')

# read and display the file's contents.
for line in myfile:
    number = int(line)
    print(number)

# close the file
myfile.close()

