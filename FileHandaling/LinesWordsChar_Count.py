#wAp to count Lines Words And Char
# Python program to count lines, words, and characters in a file

file_path = "sample.txt"   # replace with your file name

lines = 0
words = 0
characters = 0

with open(file_path, 'r') as file:
    for line in file:
        lines += 1
        words += len(line.split())
        characters += len(line)

print("Number of lines:", lines)
print("Number of words:", words)
print("Number of characters:", characters)