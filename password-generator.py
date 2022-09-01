import random
import string

def generateRandomPassword(numOfChar):
    letters = string.ascii_letters + string.digits + string.punctuation # this line generates letters, numbers and symbols
    generatedPassword = ''.join(random.choice(letters) for i in range(numOfChar))
    return generatedPassword

while True:
    numberOfCharacters = input("Number of characters for the password: ")

    if numberOfCharacters == "close":
        break

    try:
        print(f"Genrated password: {generateRandomPassword(int(numberOfCharacters))}")
        input("Press enter to continue...")
        break

    except ValueError:
        print(f"{numberOfCharacters} is not an integer.")