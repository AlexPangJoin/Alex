number = [10,35,21,-23,26,13,78,92]

def linear_search(my_list,target):
    for i in range (len(my_list)):
        if my_list[i] == target:
            return i
    else:
        return - 1

value = 13
result = linear_search(number,value)
if result == -1:
    print("Value isnot in the list")
else:
    print(f"Value {value} is found at index {result}")
