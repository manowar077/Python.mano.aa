try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))

    result=a/b
    print("result :",result)
except ZeroDivisionError:
    print("error cannot divide by zero")
