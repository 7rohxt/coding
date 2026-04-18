arr = [1, 2, 3, 4, 5, 6]

def binarySearch(arr, k):
    L = 0
    R = len(arr) - 1
    
    while L <= R:
        M = (L + R) // 2

        if arr[M] == k:
            return M
        
        elif arr[M] > k:
            R = M - 1
        
        else:
            L = M + 1
    
    return -1

print(binarySearch(arr, 5))