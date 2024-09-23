#
# Name Tatumn Chavez
# Date 9/23/24
# Bug Collector Programming Project
# COSC 2409 DN

# Initialize the accumulator.
total_bugs_collected = 0

# get the bugs collected for each day

for day in range(1, 8):

    bugs_collected = int(input('Enter the number of bugs collected on day ' + str(day) + ': '))

# Add bugs to total.
    total_bugs_collected += bugs_collected

# Display the total bugs.
print('Total number of bugs collected:', total_bugs_collected)
