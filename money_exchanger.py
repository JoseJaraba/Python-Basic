def exchange(currency, equivalence, amount):
    result = 0
    # COP to USD
    if currency == 1:
        result = amount / equivalence
        result = "%.2f" % result  # Only two numbers after the decimal point
        print(f"Los {amount} COP equivalen a {result} USD")  # Spanish message
    # MXN to USD
    elif currency == 2:
        result = amount / equivalence
        result = "%.2f" % result
        print(f"Los {amount} MXN equivalen a {result} USD")  # Spanish message
    # ARG to USD
    elif currency == 3:
        result = amount / equivalence
        result = "%.2f" % result
        print(f"Los {amount} ARG equivalen a {result} USD")  # Spanish message
    else:
        print("Ingrese solo uno de los números del menú")  # Spanish message


def run():
    exit_point = 0
    # Spanish input message
    menu = """
    Ingrese el número de la moneda que desea convertir a dolares:
    [1]: COP a USD
    [2]: MXN a USD
    [3]: ARG a USD
    [0]: Salir
    Selecciona:
    """
    while True:
        try:
            while True:
                currency = int(input(menu))
                if currency >= 0 and currency <= 3:
                    break
            if currency == 0:
                print("Bye bye")
                exit_point = 1
            else:
                amount = int(input("Ingresa la cantidad que deseas convertir:"))
                equivalence = float(input("Ingresa el valor de la moneda:"))
                exchange(currency, equivalence, amount)
        except:
            print("Por favor, ingresar solo valores numéricos")  # Spanish message
        if exit_point == 1:
            break


if __name__ == "__main__":  # Entry point
    run()

