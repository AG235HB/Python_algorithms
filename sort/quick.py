def awake():
    print("Quick sort script")

def sort(*args):
    arr = [int(item) for item in args[0]]
    
    if len(arr)<=1:
        return arr
    
    less=[]
    equal=[]
    greater=[]
    pivot=arr[0]

    for item in arr:
        if item < pivot:
            less.append(item)
        elif item == pivot:
            equal.append(item)
        elif item > pivot:
            greater.append(item)

    return sort(less) + equal + sort(greater)