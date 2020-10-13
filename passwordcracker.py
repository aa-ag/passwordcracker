import itertools
import string
import time
import getpass, os

password = getpass.getpass(prompt="Enter your password: ")

def crack_password(password):

    valid_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    password_length = len(password)

    attempts = 0

    guessess = list(itertools.product(valid_characters, repeat=password_length))

    for guess in guessess:
        guess = ''.join(guess)
        attempts += 1
        if guess == password:
            return f'Password is {guess}.\n Guessed after {attempts} attempts.'

start = time.time()
print(crack_password(password))
end = time.time()

print(f" In {round(end - start, 4)} seconds.")