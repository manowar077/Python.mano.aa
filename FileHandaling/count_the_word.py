#writre a program to count np of words in a file
with open("sample.txt","r") as file:
    data=file.read()
    words=data.split()
    count=len(words)
    print(count)
file.close()