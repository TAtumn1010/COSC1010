#
# Name Tatumn chavez
# Date 9/30/24
# Kilometer Converter Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program.
def main():
    # Constants
    def main():
        CONVERSION_FACTOR = 0.6214
        

    # get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    # Display the distance converted to miles.
    show_miles(kilometers)
  
def show_miles(km) :
    # Calculate miles.
    CONVERSION_FACTOR = 0.6214
    miles = km * CONVERSION_FACTOR

    # Display the miles.
    print(km,'kilometers equals', miles,'miles.')

main()



