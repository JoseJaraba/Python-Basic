import random


def merge_sort(list):
    if len(list) > 1:
        middle = len(list) // 2
        left = list[:middle]
        right = list[middle:]

        # Recursive call for each half
        merge_sort(left)
        merge_sort(right)

        # Iterators
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
    return list


if __name__ == "__main__":
    length = int(input("Introduce the length of the list: "))

    list = [random.randint(0, 100) for i in range(length)]
    print(list)
    print("-" * 20)

    sorted_list = merge_sort(list)
    print(sorted_list)
