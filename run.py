import random

def random_numbers(num, range_num):
    """
    Creates a random list of numbers in range of argument input
    """
    x = []
    for y in range(num):
        x.append(round(random.random() * range_num))
    return x


def number_input():
    """
    
    """
    amount_of_numbers = input("Enter the amount of number:\n")
    return int(amount_of_numbers)

def range_input():
    """
    
    """
    range_num = input("Enter number range:\n")
    return int(range_num)


def run_program():
    """
    
    """
    while True:
        test = random_numbers(number_input(), range_input())
        print(test)
        z = input("Would you like to continue? y/n \n")

        if z.lower() == "y":
            continue
        else:
            print("Exiting...")
            break

run_program()