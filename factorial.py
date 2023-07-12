#tail recursion v/s normal method
#tail cost optimization TCO

#normal way of recurcive function


def recursive(x):
    if x == 0:
        return 1
    else:
        return x * recursive(x-1)


if __name__ == "__main__":
    number = 7
    print("factorial of the given number is: {}".format(recursive(number)))
