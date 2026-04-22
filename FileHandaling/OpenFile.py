#open file
f = open("sample.txt")
print(f.read())

#open by line_by_line
f = open("sample.txt")
print(f.readline())
f.close()
#read character
with open("sample.txt") as f:
    print(f.read(5))

#looping
with open("sample.txt") as f:
    for line in f:
        print(line)
