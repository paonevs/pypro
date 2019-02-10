print("**********FILE HOSTING**********")
print("1.TO UPLOAD A FILE")
print("2.TO SEARCH A FILE")
choice=int(input("ENTER YOUR CHOICE:"))

def upload():
    uname = input("ENTER YOUR NAME:")
    print("Hi "+uname+" enter file details:")
    file_name = input("\tFILENAME WITH FORMAT:")
    type = input("\tUSE AS:")
    str=file_name+","+type+","+uname+",\n"
    f=open("filedetails.txt","a")
    f.write(str)
    print("Succsefully uploaded file")
    f.close()
def search():
    print("1.SEARCH BY USE AS")
    print("2.SEARCH BY USER")
    choice2=int(input("ENTER YOUR CHOICE:"))
    if choice2==1:
        type=input("TYPE:")
        print("All "+type+" files are:")
        f=open("filedetails.txt","r")
        line=f.readlines()
        for x in line:
            list = x.split(',')
            if list[1] == type:
                print("\t\t-->"+list[0])
        f.close()
    elif choice2==2:
        user = input("NAME OF USER:")
        f = open("filedetails.txt", "r")
        line = f.readlines()
        print("Hi " + user + " Your files are here:")
        for x in line:
            list = x.split(',')
            if list[2] == user:
                print("\t\t-->"+list[0]+" used as "+list[1])
        f.close()
if choice==1:
    upload()
elif choice==2:
    search()
else:
    print("WRONG INPUT")