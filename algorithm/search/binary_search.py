def binary_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if target == guess:
            return mid

        elif target > guess:
            low = mid + 1

        else:
            high = mid - 1

    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 4))
print(binary_search(my_list, 3))
