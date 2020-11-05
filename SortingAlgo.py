
def buble_sort_one_pass(input_array):
    for idx in range(len(input_array)-1):
        if input_array[idx] > input_array[idx+1]:
            temp = input_array[idx+1]
            input_array[idx+1] = input_array[idx]
            input_array[idx] = temp

    return input_array