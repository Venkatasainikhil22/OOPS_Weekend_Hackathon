import csv
import details

def admin_login():
    user_id = input("User Name:")
    password = input("Password:")
    with open("admin_login_credentials.txt",'r') as file:
        f = csv.reader(file)
        for row in f:
            if row[0] == user_id:
                if row[1] == password:
                    print("Logged in Succesfully")
                    file.close()
                    import Admin
                    return 0
                else:
                    print("Incorrect credentials")
                    file.close()
                    return 1
            else:
                print("Incorrect credentials")
                file.close()
                return 1

def user_login():
    user_id = input("User Name:")
    password = input("Password:")
    with open("users_login_credentials.txt",'r') as file:
        f = csv.reader(file)
        for row in f:
            if row[0] == user_id:
                if row[1] == password:
                    print("Logged in Succesfully")
                    file.close()
                    import User
                    return 0
                else:
                    print("Incorrect credentials")
                    file.close()
                    return 1
        print("Incorrect credentials")
        file.close()
    
def new_user():
    user_id = input("Enter User Name:")
    with open("users_login_credentials.txt",'r') as file:
        f = csv.reader(file)
        for row in f:
            if row[0] == user_id:
                print("This user already exist choose another one.")
                file.close()
                return new_user()
        file.close()
    password = input("Enter a password:")
    name_ = details.name()
    contact_ = details.contact()
    blood_ = details.blood()
    f = open("users_login_credentials.txt",'a')
    f.write(f"\n{user_id},{password},{name_},{contact_},{blood_}")
    f.close()
    print("Account created succesfully")
    print("Login to continue")

def Login():
    print("1.Login as user")
    print("2.Login as Admin")
    print("3.Dont have an accout? sign up as user")
    print("4.Quit application")
    i = (int)(input("Your choice:"))
    if i == 1:
        if (user_login()):
            print("1.try again")
            print("2.Go to login page")
            j = (int)(input("Your choice:"))
            if j == 1:
                if (user_login()):
                    Login()
            elif j == 2:
                Login()
            else:
                print("Invalid choice going to home")
                Login()
    elif i == 2:
        if (admin_login()):
            print("1.try again")
            print("2.Go to login page")
            j = (int)(input("Your choice:"))
            if j == 1:
                if (admin_login()):
                    Login()
            elif j == 2:
                Login()
            else:
                print("Invalid choice going to home")
                Login()
    elif i == 3:
        new_user()
    elif i == 4:
        quit()
    else:
        print("Enter valid option")

while(1):
    Login()


        
