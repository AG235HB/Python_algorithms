def awake():
    print("Bubble sort")

def sort(*args):
    arr = [int(item) for item in args[0]]
    length = len(arr)
    
    for i in range(0,length,1):
        for j in range(1,length,1):
            if arr[j-1]>arr[j]:
                tmp = arr[j-1]
                arr[j-1]=arr[j]
                arr[j]=tmp
    
    return arr

def random_sort():
    import random
    arr = list(random_numbers(10))
    print(arr)

    for i in range(0,10,1):
        for j in range(1,10,1):
            if arr[j-1]>arr[j]:
                tmp = arr[j-1]
                arr[j-1]=arr[j]
                arr[j]=tmp

    return arr

def random_numbers(count):
    import random
    for i in range(count):
        yield(random.randint(0,25))