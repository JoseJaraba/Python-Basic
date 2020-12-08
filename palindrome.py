def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


def run():
    # Spanish input message
    word = input("Ingrese una palabra: ").replace(" ", "").lower()
    if is_palindrome(word):
        print("Es un palíndromo")  # Spanish message
    else:
        print("No es un palóndromo")  # Spanish message


if __name__ == "__main__":  # Entry point
    run()

