def Request():
    blood_request = open("blood_request.txt","w")
    blood_type_required = input("blood_type_requried:")   
    name = input("Name:")
    hospital = input("Hospital:")
    contact_number = input("Contact Number:")

    blood_request.write(blood_type_required+","+name+","+hospital+","+contact_number+"\n")
    blood_request.close()

while(1):
    print("1.Request Emergency")
    print("2.Quit Application")
    i = (int)(input("Your choice:"))
    if i == 1:
        Request()
    elif i == 2:
        quit()
    else:
        print("Invalid entry!")
