source_file="sample.txt"
with open(source_file ,"r") as file:
    content=file.read()
with open(source_file,"w") as file2:
    file2.write(content)
print("file copied succesfully")

