#
# Name Tatumn Chavez
# Date 28/10/24
# Lottery Number Generator Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

import random

# Generate a seven-digit lottery number

lottery_numbers = [random.randint(0, 9) for _ in range(7)]

# Display the contents of the list

for number in lottery_numbers:
    print(number,)

    
