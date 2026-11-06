def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]   # swap with i

numbers = [10, 35, 21, -23, 26, 13, 78, 92]
print(numbers)
selection_sort(numbers)
print(numbers)