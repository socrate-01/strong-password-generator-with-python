import random
import string
print("\t\t\t\tWelcome to Socratis strong password Generator\n")

adjectives = ['sleepy', 'small', 'smelly', 'wet', 'fat', 'lovely', 'clearly', 'old', 'green', 'cheerful', 'fantastic', 'gentle', 'perfect', 'rough', 'brave']
nouns = ['fortnite', 'spartacus', 'ball', 'country', 'goat', 'dragon', 'mercedes', 'python', 'javax']

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char
    print("You Password is : %s" % password)

    response = input("\nWould you like another password? Type Y or N: ")
    if response == 'N':
        break 