#Write a Python program that takes a sentence as input, removes punctuations from the sentence, and displays the modified sentence.
import string

# Read input from the user
sentence = input()

# Remove punctuation using str.translate
no_punct = sentence.translate(str.maketrans('', '', string.punctuation))

# Print the result
print(no_punct)
