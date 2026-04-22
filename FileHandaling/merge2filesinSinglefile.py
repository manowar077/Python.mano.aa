#WAP to merge the amount the content of 2 files into single file
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", "w") as f3:
    f3.write(f1.read())
    f3.write(f2.read())

print("Files merged successfully.")