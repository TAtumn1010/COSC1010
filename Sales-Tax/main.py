#
# Name Tatumn chavez
# Date 9/9/24
# Sales Tax Programming Project
# COSC 2409 DNT
#

# Variable declarations

# Constants for the state and county sale tax rates
State_tax=0.05 
country_tax =0.025
# Get the amount of the purchase.
sale =float(input('Enter the amount of a purchase :'))
# Calculate the state sales tax.
x = (sale  * State_tax) 
# Calculate the county sales tax.
y = (sale * country_tax) 
# Calculate the total tax.
total_tax = (x + y )
# Calculate the total of the sale.
total_sale = (total_tax + sale )
# Print information about the sale.
print('The sub total =$',sale)
print('state tax =$',x)
print(' country tax =$',y)
print('The total =$',total_sale)
