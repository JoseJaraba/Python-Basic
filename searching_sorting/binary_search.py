import random


def binary_search(list, start, end, objective):

    print(f"Searching {objective} between {list[start]} and {list[end - 1]}")

    if start > end:
        return False

    middle = (start + end) // 2

    if list[middle] == objective:
        return True
    elif list[middle] < objective:
        return binary_search(list, middle + 1, end, objective)
    else:
        return binary_search(list, start, middle - 1, objective)


if __name__ == "__main__":
    length = int(input("Introduce the length of the list: "))
    objective = int(input("Which number do you want to find: "))

    list = sorted([random.randint(0, 100) for i in range(length)])

    found = binary_search(list, 0, len(list), objective)

    print(list)

    print(f"The element {objective} {'is' if found else 'is not'} in the list")
