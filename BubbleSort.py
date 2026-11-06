numbers = [10,35,21,-23, 26,13,78,92]

def bubble_tea(arr):
    n=len(arr)
    for i in range (n-1):
        for j in range (n- i -1):
            if arr[j] > arr [j+1]:
                temp = arr[j]
                arr[j] = arr [j+1]
                arr[j+1] = temp

print (numbers)
bubble_tea(numbers)
print (numbers)
