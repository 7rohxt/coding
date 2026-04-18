arr = [1, 4, 6, 3, 2]

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    p = arr[-1]

    L = [x for x in arr[:-1] if x <= p]
    R = [x for x in arr[:-1] if x > p]

    L = quickSort(L)
    R = quickSort(R)

    return L + [p] + R

print(quickSort(arr))