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
    amount_of_numbers = input("Enter the amount of numbers:\n")
    return int(amount_of_numbers)

def range_input():
    """
    
    """
    range_num = input("Enter number range:\n")
    return int(range_num)


def golden_egg(i):
    """
    
    """
    for j in i:
        if j == 7:
            print("You won a golden egg ()\n")
            print(f"Total: {sum(i)} \n")
            break
    else:
        print("Better luck next time...\n")
        print(f"Total: {sum(i)} \n")


def run_program():
    """
    
    """
    while True:
        test = random_numbers(number_input(), range_input())
        print(f"{test}\n")
        golden_egg(test)

        odd_even(test)

        z = input("Enter any key to continue, or 'e' to exit.. \n")

        if z.lower() == "e":
            print("Exiting...")
            break
        else:
            continue


class AClass:
    """
    
    """
    def __init__(self, f):
        self.f


def odd_even(nums):
    """
    
    """
    odd = []
    even = []
    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    
    print(odd)
    print(even)
    
    amount = (sum(odd) * 10) / sum(even)
    print(f"({sum(odd)} * 10) / {sum(even)} = {amount}")


def main():
    """
    
    """
    run_program()

main()