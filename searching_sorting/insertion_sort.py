import random


def insertion_sort(list):

    for i in range(1, len(list)):
        current_value = list[i]
        current_position = i

        while current_position > 0 and list[current_position - 1] > current_value:
            list[current_position] = list[current_position - 1]
            current_position -= 1

        list[current_position] = current_value

    return list


if __name__ == "__main__":
    length = int(input("Introduce the length of the list: "))

    list = [random.randint(0, 100) for i in range(length)]
    print(list)

    sorted_list = insertion_sort(list)
    print(sorted_list)
