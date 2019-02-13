import time
import random
import os.path
from os import path
print("**********KHOJIBA SEARCH ENGINE**********\n")
keyword=input("Enter the keyword: ")
links=[]
for i in range(0,25000):
	links.append("sample"+str(i)+".html")
choice=input("1. Get Links\n2. Get Content\nMy choice is: ")
choice=int(choice)
keyword = keyword.capitalize()
strt = time. time()
def start():
	count = 0
	for link in links:
			f=open(link,'r')
			if choice==1:
				html=f.read()
				if keyword in html:
					print(link)
					count+=1
			elif choice==2:	
				html=f.readlines()
				for line in html:
					if keyword in line:
						print(line)
						count+=1
			else:
			   print("Result not found")
	end = time. time()
	print(str(count)+" results found in "+str(end-strt)+"seconds")
def init():
	topics=['JavaScript','Python','Java','C++','Swift','TypeScript','Go','SQL','Ruby','Rlanguage','Php','Perl','Kotlin','Csharp','Rust','Scheme','Erlang','Scala','Elixir','Haskell']
	for i in range(0,5000):
		sr="<html>\n<head>\n<title>"+random.choice(topics)+"</title>\n<meta name='keywords' content='"+random.choice(topics)+"'/>\n<meta name='description' content='description of "+random.choice(topics)+"'/>\n<body>\n<p>"+random.choice(topics)+"</p>\n</body>\n</head>\n<body>\n<h1>Welcome to our "+random.choice(topics)+"</h1>\n<p>This is about "+random.choice(topics)+"</p>\n<a href='"+random.choice(topics)+".html'>CLICK TO "+random.choice(topics)+"</a>\n</body>\n</html>"
		f=open('sample'+str(i)+'.html','w')
		f.write(sr)
		f.close()
	topics=['Grapefruit','Pineapple','Avocado','Blueberries','Apple','Pomegranate','Mango','Strawberries','Cranberries','Lemons','Durian','Watermelon','Olives','Blackberries','Orange','Banana','Guava','Papaya','Cherry','Apricot']
	for i in range(5000,10000):
		sr="<html>\n<head>\n<title>"+random.choice(topics)+"</title>\n<meta name='keywords' content='"+random.choice(topics)+"'/>\n<meta name='description' content='description of "+random.choice(topics)+"'/>\n<body>\n<p>"+random.choice(topics)+"</p>\n</body>\n</head>\n<body>\n<h1>Welcome to our "+random.choice(topics)+"</h1>\n<p>This is about "+random.choice(topics)+"</p>\n<a href='"+random.choice(topics)+".html'>CLICK TO "+random.choice(topics)+"</a>\n</body>\n</html>"
		f=open('sample'+str(i)+'.html','w')
		f.write(sr)
		f.close()
	topics=['Potato','Onion','Eggplant','Tomato','Chilli','Pumkin','Cucumber','Carrot','Lettuce','Peas','Bean','Radish','Corn','Beetroot','Ginger','Capsicum','Garlic','Jackfruit','Spinach','Ladysfinger']
	for i in range(10000,15000):
		sr="<html>\n<head>\n<title>"+random.choice(topics)+"</title>\n<meta name='keywords' content='"+random.choice(topics)+"'/>\n<meta name='description' content='description of "+random.choice(topics)+"'/>\n<body>\n<p>"+random.choice(topics)+"</p>\n</body>\n</head>\n<body>\n<h1>Welcome to our "+random.choice(topics)+"</h1>\n<p>This is about "+random.choice(topics)+"</p>\n<a href='"+random.choice(topics)+".html'>CLICK TO "+random.choice(topics)+"</a>\n</body>\n</html>"
		f=open('sample'+str(i)+'.html','w')
		f.write(sr)
		f.close()
	topics=['Mumbai','Delhi','Cuttack','Bangalore','Hyderbad','Ahmedabad','Chennai','Kolkata','Surat','Pune','Jaipur','Lucknow','Kanpur','Nagpur','Visakhapatnam','Ludhiana','Agra','Bhubaneswar','Delhi','Puri']
	for i in range(15000,20000):
		sr="<html>\n<head>\n<title>"+random.choice(topics)+"</title>\n<meta name='keywords' content='"+random.choice(topics)+"'/>\n<meta name='description' content='description of "+random.choice(topics)+"'/>\n<body>\n<p>"+random.choice(topics)+"</p>\n</body>\n</head>\n<body>\n<h1>Welcome to our "+random.choice(topics)+"</h1>\n<p>This is about "+random.choice(topics)+"</p>\n<a href='"+random.choice(topics)+".html'>CLICK TO "+random.choice(topics)+"</a>\n</body>\n</html>"
		f=open('sample'+str(i)+'.html','w')
		f.write(sr)
		f.close()
	topics=['Pizza','Burger','Dosa','Sandwidch','Roll','Fried chicken','Cheese slider','Chicken roll','Biriyani','Momo','French fries','Badapao','Paobhaji','Manchurian','Noodles','Chicken finger','Hamburger','Pancake','Onion ring','Patty']
	for i in range(20000,25000):
		sr="<html>\n<head>\n<title>"+random.choice(topics)+"</title>\n<meta name='keywords' content='"+random.choice(topics)+"'/>\n<meta name='description' content='description of "+random.choice(topics)+"'/>\n<body>\n<p>"+random.choice(topics)+"</p>\n</body>\n</head>\n<body>\n<h1>Welcome to our "+random.choice(topics)+"</h1>\n<p>This is about "+random.choice(topics)+"</p>\n<a href='"+random.choice(topics)+".html'>CLICK TO "+random.choice(topics)+"</a>\n</body>\n</html>"
		f=open('sample'+str(i)+'.html','w')
		f.write(sr)
		f.close()
	start()
if path.exists('sample0.html'):
	start()
else:
	init()