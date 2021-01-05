import random


def bubble_sort(list):
    n = len(list)

    for i in range(n):  # O(n)

        for j in range(0, n - i - 1):  # O(n - i - 1) = O(n)

            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list


if __name__ == "__main__":
    length = int(input("Introduce the length of the list: "))

    list = [random.randint(0, 100) for i in range(length)]
    print(list)

    sorted_list = bubble_sort(list)
    print(sorted_list)
