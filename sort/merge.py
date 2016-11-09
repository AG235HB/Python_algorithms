def awake():
    print("Merge sort")

def sort(*args):
    arr = [int(item) for item in args[0]]
    if len(arr)>1:
        middle=len(arr)/2
        left = sort(arr[:middle])
        right = sort(arr[middle:])
        i=0
        j=0
        k=0

        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
        
    return arr