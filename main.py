from  dbhelper import  DBHelper

def main():
    db = DBHelper()
    while True:
        print("************welcome*********")
        print()
        print("Press 1 to insert new user")
        print("press 2 to display all user")
        print("press 3 to delete user")
        print("press 4 to update user")
        print("press 5 to exit program")
        print()
        try:
            choice=int(input())
            if(choice==1):
                id = int(input("enter user id: "))
                name = input("enter user name: ")
                phone = input("enter phone number: ")
                db.insert_user(id, name, phone)
            elif choice==2:
                db.feach__all()
            elif choice==3:
                id = int(input("enter user id who is deleted: "))
                db.delete__user(id)
            elif choice==4:
                id = int(input("enter  user id: "))
                name = input("enter new user name: ")
                phone = input("enter new phone number: ")
                db.update__user(id, name, phone)

            elif choice==5:
                break
            else:
                print("invalid input")
        except Exception as e:
            print(e)
            print("invalid details")

if __name__ == "__main__":
    main()