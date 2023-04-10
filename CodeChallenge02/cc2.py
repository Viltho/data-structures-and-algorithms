import math


def array_insert_shift(arr, num):
    x = len(arr)
    if x % 2 == 0:
        y = math.floor(x/2)
    else:
        y = math.ceil(x/2)
    output = arr[:y] + [num] + arr[y:]
    print(output)


array_insert_shift([1,2,3,5], 5)
