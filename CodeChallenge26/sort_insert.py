
def insert(arr, value):
    """This function inserts a value into from the given array and sorts it

    Args:
        arr (list): the array that is received from the insertion_sort function
        value (number): the number after index determined by i 
    """
    i = 0
    while i < len(arr) and value > arr[i]:
        i+=1
    while i < len(arr):
        temp = arr[i]
        arr[i] = value
        value = temp
        i+=1
    arr.append(value)
    
def insertion_sort(arr):
    """this function assigns a new list and works on sorting the input list

    Args:
        arr (list): unsorted list of numbers

    Returns:
        list: returns the sorted list
    """
    sorted = []
    sorted.append(arr[0])
    for value in range(1, len(arr)):
        insert(sorted, arr[value])
    return sorted

print(insertion_sort([3,2,5,6,8,9,1]))