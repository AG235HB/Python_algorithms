def search(obj, *args):
    from sort import merge
    collection = [int(item) for item in args[0]]
    collection = merge.sort(collection)
    print "sorted collection:\t"+ str(collection)
    if len(collection) > 1:
        lower = 0
        higher = len(collection) - 1
        while lower <= higher:
            mid = int((lower + higher) / 2)
            if collection[mid] < obj:
                lower = mid + 1
            elif collection[mid] > obj:
                higher = mid - 1
            else:
                return mid
