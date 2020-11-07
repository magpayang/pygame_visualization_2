def bubble_sort_one_pass(input_array):
    for idx in range(len(input_array) - 1):
        if input_array[idx] > input_array[idx + 1]:
            temp = input_array[idx + 1]
            input_array[idx + 1] = input_array[idx]
            input_array[idx] = temp

    return input_array


def selection_sort_one_pass(input_array, stick):
    current = 0
    current_index = 0
    for idx in range(stick):
        if input_array[idx] > current:
            current = input_array[idx]
            current_index = idx

    temp = input_array[stick - 1]  # archieve the last item
    input_array[stick - 1] = current  # replace last slot with the largest found
    input_array[current_index] = temp  # transfer last item to slot of greatest

    stick -= 1
    return input_array, stick


def insertion_sort_one_pass(input_array, idx):
    current = input_array[idx]
    increment = 0
    while (input_array[idx - 1 - increment] > current) and (idx - 1 - increment >= 0):
        input_array[idx - increment] = input_array[idx - 1 - increment]
        increment += 1

    input_array[idx - 1 - increment + 1] = current
    return input_array, idx


def Shell_sort_one_pass(input_array, idx, gap):
    current = input_array[idx]
    increment = 0
    while idx - gap - increment >= 0 and input_array[idx - gap - increment] > current:
        input_array[idx - increment] = input_array[idx - gap - increment]
        increment += gap
    input_array[idx - gap - increment + gap] = current
    return input_array, idx, gap


def merge_sort(input_array):
    if len(input_array) == 1:  # base case
        return input_array

    left = input_array[:len(input_array) // 2]
    right = input_array[len(input_array) // 2:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []

    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            result.append(left[0])
            left = left[1:len(left)]
        else:
            result.append(right[0])
            right = right[1:len(right)]

    while len(left) != 0:
        result.append(left[0])
        left = left[1:len(left)]

    while len(right) != 0:
        result.append(right[0])
        right = right[1:len(right)]

    return result
