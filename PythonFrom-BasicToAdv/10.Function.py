# #without argument
# def greet():
#     print("Hello World")
# greet()
#
#
# #adding two no
# def add2numbers(num1 ,num2):
#     result = num1 + num2
#     print(result)
#
# add2numbers(10,30)
#
# #convert to lowercase
# s="hello"
# print(s.lower())
#
# #covert to uppercase
# s="hello"
# print(s.upper())
#
# #remove space from begining and end
# s="   hello    "
# print(s.strip())
#
#
# #replace the substring
# s="i like java"
# print(s.replace("java","python"))
#
#
# #find index of substring
#
# s="hello world"
# print(s.find("world"))
#
# #split
# s=["banana apple mango manowar Aahan"]
# print(s.split())
#
# #join
# lst=['a','b','c']
# print(s.join(lst))
#
# #count
#
# s="banana"
# print(s.count('a'))


def add2num(a,b):
    return a+b

sum2num=add2num(10,29)
print(sum2num)

#the pass statement
def kuchv():
    pass
print("hello")


def area(r):
    area=3.14*r**2
    return area
r=int(input("enter radius:"))
area=area(r)
print("area:",area)