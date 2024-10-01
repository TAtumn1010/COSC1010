#
# Name Tatumn Chavez
# Date 9/30/24
# Feet to Inches Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program.


def main():
    # Constants
    INCHES_CONVERSION_FACTOR = 12

    # get the distance in feet.
    feet = float(input('Enter the amount of feet: '))

    # Display the feet converted to inches.
    show_inches(feet, INCHES_CONVERSION_FACTOR)

def show_inches(x, INCHES_CONVERSION_FACTOR):
    # Calculate inches using the conversion factor provided as an argument.
    inches = x * INCHES_CONVERSION_FACTOR
    
    # Display the inches.
    print(x,'feet equals ',inches, 'inches.')

main()


  


