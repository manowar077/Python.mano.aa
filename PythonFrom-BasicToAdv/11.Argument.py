def print_info(name="xyz", age=21):
    print_info(f"hello {name} age is{21}")

# order of argument
# 1.postional -> Default -> positional variable -> keyword variable length
#1.Required Argument
def greeting(namee):
    print("hek=llo",namee ,"!")
greeting("madav")

#2.Default Argumeent

def greeting(name="manowar"):
    print("hello",name ,"!")
greeting("alam")

#3.Keyword Argument
def divide(a,b):
    return a/b
result=divide(10,5)
print(result)

#4.Arbitary argument
def add_num(*args):
    return sum(args)
result=add_num(1,2,3,4,5)
print(result)