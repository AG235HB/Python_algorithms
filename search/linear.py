def search(obj, *args):
    from sort import merge
    collection = [int(item) for item in args[0]]
    result = " "
    for i in range(0, len(collection), 1):
        if obj == collection[i]:
            result += " " + str(i)
    return result
