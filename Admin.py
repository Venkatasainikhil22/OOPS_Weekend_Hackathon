import details

while (1):
    print("******************* Welcome to XYZ Blood Company *******************")
    print("********************        1.Donars List       ********************")
    print("********************     2.Add Hospital List    ********************")
    print("********************    3.View Hospital List    ********************")
    print("********************        4.Users List        ********************")
    print("********************      5.Notifications       ********************")
    print("********************     6.Quit Application     ********************")
    i = (int)(input("Your choice:"))
    if i == 1:
        print("1.Add a Donar")
        print("2.View Donar's list")
        print("3.View Donar's with rare blood groups")
        j = (int)(input("Your choice:"))
        if j == 1:
            details.Add_donar()
        elif j == 2:
            print("1.View all Donar's")
            print("2.View Donar's with a particular blood group")
            k = (int)(input("Your choice:"))
            if k == 1:
                details.view_donar()
            if k == 2:
                details.Donar_with_blood()
            else:
                print("Invalid choice")
        elif j == 3:
            print("Donars of blood groups AB+ , AB- , B- are displayed below")
            details.view_donar_rare_blood()
        else:
            print("Invalid choice-2")
    elif i == 2:
        details.Add_hospital()
    elif i == 3:
        details.View_hospital()
    elif i == 4:
        details.view_user()
    elif i == 5:
        check = details.Emergency_check()
        if check != None:
            print("Emergency! There is a Blood Request")
            print("Patients details:")
            print("Requied blood group:",check[0])
            print("Patients Name:",check[1])
            print("Contact Number:",check[2])
            print("Hospital Name:",check[3])
            print("Notifying below donars")
            details.Donar_with_blood_help(check[0])
            print("Notifying Hosipitals and Blood banks press '1' if not required, or press anything else")
            a = (int)(input("Your choice:"))
            if a != 1:
                print("Below Hospitals and Blood banks are Notified")
                details.View_hospital()
            file = open("patients.txt",'a')
            file.write(f"\n{check[0]},{check[1]},{check[2]},{check[3]}")
            file.close()
            print("Patient details are succesfully added to the file 'patients.txt'")
        else:
            print("There are no Notifications or blood requests as of now")
    elif i == 6:
        quit()
    else:
        print("Invalid choice")









