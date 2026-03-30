#operator in paython
#1. Arthematic operator
a=5;
b=4;
print(a+b)
print(a-b)
print(a*b)

#2.comperison operator(output is boolean (t/f)
a=5;
b=4;
print(a>b)
print(a<b)
print(a==b)
print(a!=b)

#3.Assignment operator
a=4;
b="madav"

#4.logical operator
a=5;
b=6;
print(a>b and b<10) # true +false=false
print(a>b or b<10) # true + false=true
print(a<b and b>10)
print(a==b and b<10)

#4.Identity operator(is ,is not)
x=[1,2,3]
y=x
z=[1,2,3]
print(x is y)
print(x is z) #compare on the basis of location not value
print(x is not z)

#6.membership operator(in,not in)
my_list=['orange','apple','banana']
print('apple' in my_list)
print('orange' in my_list)
print('litchy' not in my_list)

#7.Bitwise operator
a=5         # 5 in binary -0101
b=3         # 3 in binary _0011
print(a&b)  # 1 in binary -0001