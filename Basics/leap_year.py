#check year is leap or not
year=int(input("enter the year"))

##divided by 100 means centuary year (ending with 00)
#centuary year divided by 400 is leap year
if(year%400==0 and year%100==0):
    print(year,"is a leap year")
#not divided by 100 means not a centuary year
elif year%4==0 and year%100==0 and year%400==0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")