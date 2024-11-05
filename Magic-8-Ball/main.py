#
# Name Tatumn chavez
# Date November 4 2024
# Magic 8 Ball Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 



import random

def load_responses(filename):
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read all the lines from the file
        responses = file.readlines()
        
def magic_8_ball():
    responses = load_responses('8_ball_responses.txt')
    print("Welcome to the Magic 8 Ball!")
    
    while True:
        question = input("Ask a yes or no question (or type 'quit' to exit): ")
        if question == 'quit':
            # If the user types 'quit', say goodbye and exit the loop
            print("Goodbye!")
            break
        else:
            # Choose a random response from the list and print it
            print(random.choice(responses))

if __name__ == "__main__":
    magic_8_ball()


