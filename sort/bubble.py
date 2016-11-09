def awake():
    print("Bubble sort")

def sort(*args):
    arr = [int(item) for item in args[0]]
    
    for i in range(0,len(arr),1):
        for j in range(1,len(arr),1):
            if arr[j-1]>arr[j]:
                tmp = arr[j-1]
                arr[j-1]=arr[j]
                arr[j]=tmp
    
    return arr