#Student Result
while True:
    print("Studen Result Management.")
    print("1:Add New Result")
    print("2.Update Result")
    print("3.Delete Result")
    print("4.Show All Result")
    print("5.Search Result")
    print("6.Exit")

    choice = input("Enter your choice:")
    if choice == "1":
        add_result()
    elif choice == "2":
        update_result()
    elif choice == "3":
        delete_result()
    elif choice == "4":
        show_all_result()
    elif choice == "5":
        search_result()
    elif choice == "6":
        exit()
    else:
        print("Please enter a valid choice.")

def add_result():
    name = input("Enter your name:")
    roll_no = input("Enter your roll no:")
    marks = float(input("Enter your marks:"))
    student[roll_no] = {"Name":name, "marks":marks}
    print("Result Added Successfully")

