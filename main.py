
from manager import Manager

main=Manager()

while True:
    print("\nTask Tracker")
    print("1 Add Taskses")
    print("2 Show Taskses")
    print("3 Upgrade")
    print("4 Deletes")
    print("5 Exit")

    choice=input("choice valid num: ")

    if choice=="1":
        title=input("title: ")
        description=input("desc: ")
        if main.add(title,description):
            print("added")

    elif choice=="2":
        main.show()
    elif choice=="3":
        main.show()
        try:
            no=int(input("task no: "))-1
            new_title=input("new title: ")
            new_description=input("new desc: ")
            if main.Upgrade(no,new_title,new_description):
                print("Upgrade ")
        except:
            print("all number Give")

    elif choice=="4":
        main.show()
        try:
            no=int(input("task delete no: "))-1
            if main.delete(no):
                print("deleted ")
        except:
            print("vulue number")

    elif choice=="5":
        print("closing program")
        break

    else:
        print("not valid option")
