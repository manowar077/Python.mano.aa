#Open In Read Mode
file=open("sample.txt","r")
data=file.read(5) #we defined a size
print(data)
print(type(data))
dat=file.readline()
print(dat)
dat=file.readline()
print(dat)
file.close()
#
