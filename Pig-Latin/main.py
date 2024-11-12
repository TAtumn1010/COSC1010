# Name Tatumn Chavez
# Date 11/11/24
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 



def main():
    # Read a sentence from the user
    sentence = input('Enter a sentence: ')
    
    # Split the sentence into words
    words = sentence.split()
    
    # Convert each word to Pig Latin
    pig_latin_words = [convert_to_pig_latin(word) for word in words]
    
    # Join the Pig Latin words back into a sentence
    pig_latin_sentence = ' '.join(pig_latin_words)
    
    # Output the Pig Latin sentence
    print('Pig Latin:', pig_latin_sentence)

def convert_to_pig_latin(word):
    # Move the first letter to the end and add 'ay'
    return word[1:] + word[0] + 'ay'
    
# Call the main function
if __name__ == "__main__":
    main()
