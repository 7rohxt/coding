arr = [1, 4, 6, 3, 2]

def merge(l, r):
    i, j = 0, 0
    res = []

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
        
    while i < len(l):
        res.append(l[i])
        i += 1
        
    while j < len(r):
        res.append(r[j])
        j += 1

    return res

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

print(merge_sort(arr))