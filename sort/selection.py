def sort(*args):
    arr = [int(item) for item in args[0]]
    length = len(arr)
    for i in range(0, len(arr), 1):
        min = arr[i]
        minin = i
        for j in range(i+1, len(arr), 1):
            if arr[j] < min:
                min = arr[j]
                minin = j
        arr[minin] = arr[i]
        arr[i] = min
    return arr
    