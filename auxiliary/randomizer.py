import random

def create_collection(count, min, max):
    for i in range(count):
        yield(random.randint(min,max))