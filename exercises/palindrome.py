def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


def run():
    # Spanish input message
    word = input("Introduce a word: ").replace(" ", "").lower()
    if is_palindrome(word):
        print("It's palindrome")
    else:
        print("It's not  palindrome")


if __name__ == "__main__":  # Entry point
    run()

