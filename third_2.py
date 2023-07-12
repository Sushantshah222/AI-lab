
from factorial import recursive


#tail recursion method

def recurse(n, accumulator=1):
    if n == 0:
        return accumulator
    recurse(n-1, accumulator=accumulator*n)


if __name__ == "__main__":
    number = int(input("Enter a number :"))
    print("factorial of the given number is: {}".format(recursive(number)))
