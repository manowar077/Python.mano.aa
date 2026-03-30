

#Q1.write a python program to input student name and marks of 3 subject .print name &percentage inoutput
#Name=input("Enter your name:")
cheMarks=input("Enter your chems:")
phyMarks=input("enter your phys:")
mathsMarks=input("enter your maths:")

#claculating percentage
percentage=((int(cheMarks)+int(phyMarks)+int(mathsMarks))/300)*100

#print("my name :",Name)
print("percentage :",perc)

#Q2.program that collect data multiple times of data from user and store in dictionary and then print tha data
user_data={} #intilizing a dictionary

#input from user data
user_data["name"]=input("Enter your name:")
user_data["age"]=int(input("Enter your age:"))
user_data["height"]=float(input("Enter your height:"))
user_data["student"]=input("Enter your name (yes/no):")

#print
print(user_data)

