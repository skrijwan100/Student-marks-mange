student_laibary={}
def add_new():
    name=input("Enter the student name:")
    marks= int(input("Enter the student marks:"))
    student_laibary.setdefault(name,marks)
    print(f"{name} has successfully add student laibary")
def view():
    for name,marks in student_laibary.items():
        print(f"{name}:{marks}")
def update():
    name=input("Enter the student you wnat to update:")
    if name in student_laibary.keys():
      marks= int(input("Enter update marks of the student: "))
      student_laibary[name]=marks
    else:
        print("The student name is not find.")
def find():
    name=input("Enter the student name:")
    if name in student_laibary.keys():
      print(f"{name}:{student_laibary[name]}")
    else:
        print("The name is not found.")

def delete_std():
    name=input("Enter the student name you want to delete:")
    del student_laibary[name]
    print(f"successfully delete the student.")

if(__name__=="__main__"):
     while True:
        try:
            print("WElcome to student management sysytem\n1.addd new student\n2.view all student\n3.update student marks\n4.find student marks\n5.delete student\n6.exit")
            user_choose=int(input("Enter your chooise:"))
            if user_choose==1:
                add_new()
            elif user_choose==2:
                view()
            elif user_choose==3:
                update()
            elif user_choose==4:
                find()
            elif user_choose==5:
                delete_std()
            elif user_choose==6:
                print("Have a good day.")
                exit()
        except ValueError as e :
            print("Enter a valid number.")
        except Exception as e :
            print(e) 