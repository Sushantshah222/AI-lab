# wap program to check if an given input is even or odd integer using a function

def check_int(n):
    if n % 2 == 0:
        return("Even number")
    else:
        return("Odd number")
    

if __name__ == "__main__":
    number = int(input("Enter the number"))
    print(number," is ",check_int(number))