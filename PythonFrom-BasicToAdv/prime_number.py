#check prime number
num=int(input("enter your number : "))
def check_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
        else:
            return True
    return True
print(check_prime(num))