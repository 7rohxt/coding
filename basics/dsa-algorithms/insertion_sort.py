arr = [1, 4, 6, 3, 2]

def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    
    return arr

print(insertionSort(arr))
        