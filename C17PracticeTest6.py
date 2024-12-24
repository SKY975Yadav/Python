'''#Problem 1 : Greatest of 4 numbers
num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
num3 = int(input("Enter Number 3 : "))
num4 = int(input("Enter Number 4 : "))
if(num1>=num2 and num1>=num3 and num1>=num4):
    print(num1," is Greatest number")
elif(num2>=num1 and num2>=num3 and num2>=num4) :
    print(num2," is Greatest number")
elif(num3>=num1 and num3>=num2 and num3>=num4) :
    print(num3," is Greatest number")
else : print(num4," is the Greatest number")'''
'''#Problem 2 : student is pass or not
maths = int(input("Enter marks in Maths : "))
physics = int(input("Enter marks in Physics : "))
english = int(input("Enter marks in English : "))
total = ((maths+physics+english)/300)*100
if(maths<33):print("Student is failed in Maths with marks of ",maths)
elif(physics<33):print("Student is failed in Physics with marks of ",physics)
elif(english<33):print("Student is failed in Egnlsih with marks of ",english)
else:
    if(total<40):print("Student is failed by total percentage of ","{:.2f}".format(total))
    else : print("Student is passed out with total percentage of ","{:.2f}".format(total))'''
'''#Problem 3
messege = input("Enter Messege : ")
messege = messege.lower()
bol = ("make a lot of money" in messege) or ("buy now" in messege) or ("subscribe this" in messege) or ("click this" in messege)
if bol :print("The given messege is a spam messege")
else : print("It is not a spam messege")'''
'''#problem 4
userName = input("Enter username : ")
if(len(userName)<=10):print("It is valid User Name")
else:print("It is not a valid user Name :")'''
'''#problem 5
names = ["sai krishna","sai kumar","kiran kumar","rakesh"]
name = input("Enter Name : ").lower()
name =' '.join(name.split())
if name in names :print("Yes Your name is on this list")
else :print("No Your name is not on this list")'''
'''#problem 6
marks = int(input("Enter your Marks : "))
if marks<=100 and marks>0 :
    if marks>90 : print("Student is Exceptional")
    elif marks>80 : print("Student is Grade A student")
    elif marks>70 : print("Student is Grade B student")
    elif marks>60 : print("Student is Grade C student")
    elif marks>50 : print("Student is Grade D student")
    else: print("Student is Grade F(Failed) student")
else:print("Invalid Marks")   '''
'''#problem 7
post = input("Enter Post :").lower()
if "harry" in post : print("Post is about harry ")
else : print("Post is not about harry")'''
