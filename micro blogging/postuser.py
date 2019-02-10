print("*******message*******")
print("1. post message")
print("2. search message")
choice=int(input("Enter your choice ="))


def search():

     name=input("Enter name =")
     f=open("message.txt","r")
     Line=f.readlines()
     for x in Line:
         list=x.split(",")
         if list[0]==name:
             print(list[1])
     else:
         print("message not found")
     f.close()
def post():
    msg=input("Enter the message")
    f=open("message.txt","w")
    f.close()

if choice==1:
    post()
elif choice==2:
    search()
else:
    print("Error")