arr = [1, 4, 6, 3, 2]

def bubbleSort(arr):
    n = len(arr)
    flag = True

    while flag:
        flag = False
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                flag = True
                arr[i], arr[i-1] = arr[i-1], arr[i]
    
    return arr

print(bubbleSort(arr))