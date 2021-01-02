def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def run():
    while True:
        try:
            num = int(input("Introduce an integer: "))
            break
        except ValueError:
            print("That's not a valid number")

    for i in range(num):
        result = fibonacci(i)
        print(result)


if __name__ == "__main__":
    run()

