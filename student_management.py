def add_student():
    sid=input("Enter student ID:")
    name=input("Enter student name:")
    marks=input("Enter student marks:")
    file=open("students.txt","a")
    file.write(sid+" "+name+"  "+marks+"\n")
    file.close()
    print("Student added successfully")
def view_student():
    file=open("students.txt","r")
    print("\nstudent Records:")
    print("ID  Name  Marks")
    for line in file:
        print(line.strip())#remove newline
    file.close()
def search_student():
    sid=input("Enter student ID to search:")
    file=open("students.txt","r")
    found=False
    for line in file:
        data=line.split()
        if data[0]==sid:
            print("Student found:",line)
            found=True
            break
    if not found:
        print("Student not found!")
    file.close()
def delete_student():
    sid = input("Enter Student ID to delete: ")

    file = open("students.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("students.txt", "w")
    found = False

    for line in lines:
        data = line.split()
        if data[0] != sid:
            file.write(line)
        else:
            found = True

    file.close()

    if found:
        print("Student deleted successfully!")
    else:
        print("Student not found!")


while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice")





    



    
