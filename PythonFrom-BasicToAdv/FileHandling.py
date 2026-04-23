# with open() ('sample.txt' 'r') as file:
#     content = file.read()
#     print(content),

# file = open("sample.txt")
# print.write("hello world")
# print.write("file handaling in python")
# file.close()
 #seek
file=open("sample.txt","r")
print(file.read())
file.seek(4)
print(file.read())
file.close()

#tell and seek
file=open("sample.txt","r")
print(file.tell())

file.read(10)
print(file.tell())

file.seek(0)
print(file.tell())

file.close()
