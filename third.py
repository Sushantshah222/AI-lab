#wap to display prime number form 1 to 1000
# use trail division method for the optimization of this code



def check_prime(n:int) -> bool:
    count = 0
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

num = int(input("Enter a number :"))
if check_prime(num):
    print(f"{num} is PRIME NUMBER")
else:
    print(f"{num} is NOT PRIME")

    
    