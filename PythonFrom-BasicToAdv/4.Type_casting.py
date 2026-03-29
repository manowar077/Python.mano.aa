#type casting =convert data type to another data type
a=1
print(a)
print(type(a))

b="1"
print(type(b))

c=int(b)
print(type(c))

mynum=26
mynum=str(mynum)
print(type(mynum))

f1=111.33
f2=int(f1)
print(type(f2))

#implicit type casting(automaticaly type casted)
var1=10
var2=30.44
var3=var1+var2
print(var3)
print(type(var3))


#explicit type casting(manualy changed by programer)

int_num=101
str_num=str(int_num)
print(type(str_num))

a0=bool(0)
print(a0)
print(type(a0))

#types of type_casting
int( )
float()
str()
list()
tuple()
set()
dict()
bool()