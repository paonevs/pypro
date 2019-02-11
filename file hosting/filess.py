print("1. search by filename")
print("2. search by usernamename")
print("3. new file")

choice= input("enter your choice")
choice= int(choice)
if choice==1:
	filename= input("enter filename")
	file="fitt.txt"
	f=open(file,"r")
	str=f.readlines()
	f.close()
	for x in str:
		#print(x+"\n")
		lst=x.split(',')
		#print(lst[1])
		if lst[1]==filename:
			print(lst[0])

elif choice==2:
	uname= input("enter username")
	file="fitt.txt"
	f=open(file,"r")
	str=f.readlines()
	f.close()
	for x in str:
		#print(x+"\n")
		lst=x.split(',')
		#print(lst[2])
		if uname in lst[2]:
			print(lst[0])

elif choice==3:
	f=input("file")
	n=input("name")
	u=input("user")
	str=f+","+n+","+u
	f=open("fitt.txt","a")
	f.write(str+"\n")
	f.close()
else:
	print("wrng")
			
			
	  
	    
    
