#check number is positive negative and Zero
num=int(input("enter the number : "))
def check_pos_neg_zero(num):
    if num>0:
        print(num,"is positive")
    elif num==0:
        print(num,"is zero")
    else:
        print(num,"is negative")
print(check_pos_neg_zero(num))
