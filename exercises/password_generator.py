import random
import string


def generate_password():
    uppercase = tuple(string.ascii_uppercase)
    lowercase = tuple(string.ascii_lowercase)
    numbers = tuple(string.digits)
    sings = tuple(string.punctuation)

    characters = uppercase + lowercase + numbers + sings
    password = list()

    for i in range(15):
        random_character = random.choice(characters)
        password.append(random_character)

    password = "".join(password)  # Converts the list into a string
    return password


def run():
    password = generate_password()
    print("Your new password is: " + password)


if __name__ == "__main__":
    run()
