def exchange(currency, equivalence, amount):
    result = 0
    # COP to USD
    if currency == 1:
        result = amount / equivalence
        result = "%.2f" % result  # Only two numbers after the decimal point
        print(f"The {amount} COP are equivalent to {result} USD")
    # MXN to USD
    elif currency == 2:
        result = amount / equivalence
        result = "%.2f" % result
        print(f"The {amount} MXN are equivalent to {result} USD")
    # ARG to USD
    elif currency == 3:
        result = amount / equivalence
        result = "%.2f" % result
        print(f"The {amount} ARG are equivalent to {result} USD")
    else:
        print("Please, introduce a valid number")


def run():
    exit_point = 0
    # Input message
    menu = "Introduce the number of the currency that do you want to convert:\n[1]: COP to USD\n[2]: MXN to USD\n[3]: ARG to USD\n[0]: Exit\nSelect: "

    while True:
        try:
            while True:
                currency = int(input(menu))
                if currency in range(4):
                    break
                else:
                    print("Please, introduce a valid number")

            if currency == 0:
                print("Bye bye")
                exit_point = 1

            else:
                amount = int(
                    input("Introduce the amount of money that do you want to convert: ")
                )
                equivalence = float(
                    input("Introduce the current value of the currency: ")
                )
                exchange(currency, equivalence, amount)
        except:
            print("Please, introduce only numerics values")
        if exit_point == 1:
            break


if __name__ == "__main__":  # Entry point
    run()

