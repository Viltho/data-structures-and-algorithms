import math


def insert_shift_array(arr, num):
    x = len(arr)
    if x % 2 == 0:
        y = math.floor(x / 2)
    else:
        y = math.ceil(x / 2)
    output = arr[:y] + [num] + arr[y:]
    print(output)


insert_shift_array([1,2,3,6,5], 4)