def awake():
    print("Insertion sort")

def sort(*args):
    arr = [int(item) for item in args[0]]
    
    for i in range(1,len(arr),1):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        
    return arr