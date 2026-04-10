#Q1
a=float(input("Enter a number: "))
b=float(input("Enter b number: "))
c=float(input("Enter c number: "))

if a>=b and a<=c:
    largest=a
elif b>=a and b>=c:
    largest=b
else:
    largest=c
    print(largest)    