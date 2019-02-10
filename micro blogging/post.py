print("1.to post something")
print("2.search a post")
choice=input("Enter your choice:-")
choice=int(choice)
if choice==1:
    uname=input("Enter the user name:-")
    post=input("Whats in your mind!! say something:-")
    str=uname+","+post+",\n"
    f=open("post1.txt","a")
    f.write(str)
elif choice==2:
    name=input("Enter user's name")
    f=open("post1.txt","r")
    line=f.readlines()
    for x in line:
        list=x.split(',')
        if name==list[0]:
            print("post is :")
            print("-->"+list[1])
        f.close()
