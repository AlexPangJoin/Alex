numbers = [10,35,21,-23,26,13,78,92]
numbers.sort()

def binary_search(my_list,target):
    low = 0
    high = len(my_list)-1
    while low <= high:
        mid = (low + high)//2
        if my_list[mid] == target:
            return mid
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return -1

value = 13
result = binary_search(numbers,value)
if result == -1:
    print("Value is not in the list")
else:
    print(f"Value {value} is found at index {result}")