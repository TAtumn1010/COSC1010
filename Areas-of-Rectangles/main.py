#
# Name Tatumn chavez
# Date 9/16/24
# Areas of Rectangles Programming Project
# COSC 2409 DNT
#
# Local variables
# length1
# width1
# length2
# width2
# Get rectangle 1 length and width
length1= int(input('Enter the lenght of rectangle 1:'))

width1= int(input('Enter the width of rectangle 1:')) 

# Get rectangle 2 length  and width
length2= int(input('Enter the lenght of rectangle 2:'))

width2= int(input('Enter the width of rectangle 2:')) 


# Calculate area 1
area1=  length1 * width1
# Calculate area 2
area2=  length2 * width2
# Print area comparison using if-elif-else statements
if area1 > area2:print('Rectangle 1 has the greater area.')

elif area2 > area1:print('Rectangle 2 has the greater area.')

else:print('Both have the same area.')
