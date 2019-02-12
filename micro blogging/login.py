print("1.Login")
print("2.Sign up")
choice=input("Enter your choice:-")
choice=int(choice)
if choice==1:
	uname=input("Enter username:-")
	pwd=input("Enter passward:-")
	file=uname+".txt"
	f=open(file,"r")
	str=f.read()
	list=str.split(",")
	if list[0]==uname:
		if list[3]==pwd:
			print("Wellcome!!! Happy to see you!!")
	else:
		print("Invalid Username or Passward")
	f.close()
elif choice==2:
	uname=input("Username:-")
	name=input("Enter your name:-")
	email=input("Enter Email id:-")
	pwd=input("Enter passward:-")
	phn=input("Enter phone number:-")
	str=uname+","+name+","+email+","+pwd+","+phn+"\n"
	file=uname+".txt"
	f=open(file,"a")
	f.write(str)
f.close()
