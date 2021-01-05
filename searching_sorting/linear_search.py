import random


def linear_search(list, objective):
    match = False

    counter = 0

    for element in list:  # O(n)
        counter += 1
        if element == objective:
            match = True
            break

    print(counter) 
    return match



if __name__ == "__main__":
    length = int(input("Introduce the length of the list: "))
    objective = int(input("Which number do you want to find: "))

    list = [random.randint(0, 100) for i in range(length)]

    found = linear_search(list, objective)

    print(list)

    print(f"The element {objective} {'is' if found else 'is not'} in the list")
