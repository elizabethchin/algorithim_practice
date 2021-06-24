def reverse_arry_in_place(array):
    start = 0
    end = len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]

    start += 1
    end -= 1  