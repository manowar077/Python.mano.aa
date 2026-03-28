import math
#Input coefficient
a=float(input("enter the coeficient :"))
b=float(input("enter the coeficient :"))
c=float(input("enter the coeficient :"))

#calculate the decrement
discriminant=b**2-4*a*c
#check if the dis is positive ,negative or zero
if discriminant<0:
    #two real distinct root
    root1=(-b+math.sqrt(discriminant))/(2*a)
    root2=(-b-math.sqrt(discriminant))/(2*a)
    print("The root of the equation is :",root1)
    print("The root of the equation is :",root2)
elif discriminant==0:
    #one real root (repeated)
    root=-b/(2*a)
    print("The root of the equation is :",root)
else:
    #complex root
    real_part=-b/(2*a)
    imaginary_part=math.sqrt(abs(discriminant)/(2*a))
    print(real_part,"+",imaginary_part,"i")
    print(real_part,"+",imaginary_part,"i")