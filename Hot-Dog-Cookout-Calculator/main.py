#
# Name Tatumn chavez
# Date 16/9/24
# Hot Dog Cookout Calculator Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

# varibles

hotdog_pack =10
Buns_pack = 8
# ask the number of hot dog packs and bun packs



x= int(input('Enter the amount of bun packs:'))
y= int(input('Enter the amount of hot dog packs:'))
#calculate the total hot dogs and buns + leftover buns and hot dogs
 
amount1= x * hotdog_pack
amount2= y * Buns_pack

leftover1= amount1 - amount2
leftover2= amount2 - amount1

#print total hot dogs and buns
 
print(' total hod dogs:',amount1)
print(' total buns:',amount2)

# print the number of leftover hotdogs or buns

if amount1 > amount2: print('Amount of leftover hotdogs:',leftover1)

elif amount2 > amount1:print('Amount of leftover buns:',leftover2)

else: print('there are no leftovers:')  

#
