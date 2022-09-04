import random
import string
import pyperclip

def generateRandomPassword(numOfChar):
    letters = string.ascii_letters + string.digits + string.punctuation # this line generates letters, numbers and symbols
    generatedPassword = ''.join(random.choice(letters) for i in range(numOfChar))
    return generatedPassword

while True:
    numberOfCharacters = input("Number of characters for the password: ")

    if numberOfCharacters == "close":
        break

    try:
        randomStringOfPassword = generateRandomPassword(int(numberOfCharacters))
        pyperclip.copy(randomStringOfPassword)
        print(f"Genrated password: {randomStringOfPassword}")
        input("Press enter to continue...")
        break

    except ValueError:
        print(f"{numberOfCharacters} is not an integer.")
