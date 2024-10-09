import random

def random_numbers(num):
    """
    Creates a random list of numbers in range of argument input
    """
    x = []
    for y in range(num):
        x.append(round(random.random() * 100))
    return x

test = random_numbers(20)
print(test)