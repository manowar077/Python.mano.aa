#dictionary in python
Mydict={"name":"John","age":25}
print(Mydict["name"])
print(Mydict["age"])
print(Mydict.keys())
print(Mydict.values())


dict1={"a":1,"b":2,"c":3}
dict2={"c":4,"d":5,"e":6}

dict.update(dict2)
print(dict)

a=[]
for i in range(1,100):
    if(i%2==0):
        a.append(i)
print(a)

a=[i**2 for i in range(1,100) if i%2==0]
print(a)

x=["python","java","javascript"]
for i in enumerate(x ):
    print(x)
