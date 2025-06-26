# Task Title: Working with Lists, Split/Join, and Tuples
# Takes a sentence input from the user
# Splits the sentence into a list of words
# Prints the list, then joins the list back into a sentence using ' - ' separator
# Stores your first and last name in a tuple, then prints each part using indexing
sentence = input("Enter a sentence:")
new_sentence= sentence.split()
print(new_sentence)
new_sentence='-'.join(new_sentence)
print(new_sentence)

tuple=()
tuple=input("Enter your full name: ")
print(tuple)
pos=tuple.find(" ")
print(f'First name: {tuple[:pos]}')
print(f'Last name: {tuple[pos+1:]}')
