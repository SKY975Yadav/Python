'''#Problem 1 Programmer in a company microsoft
class Programmer :
    company = "Microsoft"
    def __init__(self,name,Pid,lang,sal) -> None:
        self.name = name 
        self.id = Pid
        self.lang = lang
        self.salary = sal
    def printProgrammerDetalis(self):
        print(f"Programmer Name : {self.name}\nProgrammer Id : {self.id}\nProgrammer Language : {self.lang}\nPrpgrammer Salary : {self.salary}")
        print()

programmer1 = Programmer("Sai Krishna Yadav",552,"Java",30000)
programmer2 = Programmer("Rahul Yadav",507,"Python",40000)
programmer3 = Programmer("Narasihmlu",527,"C++",35000)
# programmer1.name = "Sai Krishna Yadav"
# programmer2.name = "Rahul Yadav"
# programmer3.name = "Narasihmlu"
# programmer1.id = 552
# programmer2.id = 507
# programmer3.id = 526
# programmer1.lang = "Java"
# programmer2.lang = "Python"
# programmer3.lang = "C++"
programmer1.printProgrammerDetalis()
programmer2.printProgrammerDetalis()
programmer3.printProgrammerDetalis()'''
'''#Problem 2 calculator for finding square and squareRoot
import math
class Calculator :
    def findSquare(self,num):
        return num*num
    def findSquareRoot(self,num):
        return math.sqrt(num)

cal1  = Calculator()
number = int(input("Enter Number : "))
print("Finding Square of the Number ",cal1.findSquare(number))
print("Finding Square root of the Number ",cal1.findSquareRoot(number))'''
'''#Problem 3 changing object variable can't change the class variable
class Example :
    a = "Sai"
exm = Example()
exm.a = "Krishna"
print(exm.a)
print(Example.a)'''
'''#Problem 4 add static method to problem to for greet 'hello'
import math
class Calculator :
    def findSquare(self,num):
        return num*num
    def findSquareRoot(self,num):
        return math.sqrt(num)
    @staticmethod
    def greet():
        print("Hello Welcome to Calculator : ")

cal1  = Calculator()
cal1.greet()
number = int(input("Enter Number : "))
print("Finding Square of the Number ",cal1.findSquare(number))
print("Finding Square root of the Number ",cal1.findSquareRoot(number))'''
'''#Problem 5 Train booking and other functions
# 1 2 3 4 5 6 7 8 9 10
import random 
class Train:
        def __init__(self,TrainNumber,fare,seats) -> None:
            self.li = []
            self.trainNubmer = TrainNumber
            self.fare = fare
            self.seats = seats
            for i in range(1,seats+1):
                self.li.append(i)
        def getStatus(self):
            print("*********************")
            print(f"Train Number : {self.trainNubmer}")
            print(f"Number of Seats available : {self.seats}")    
            print(f"They are : {self.li}")
            print("*********************")
            
        def fareInfo(self):
            print(f"Price of the Ticket is : {self.fare}")
            
        def bookTicket(self):
            if self.seats>0 : 
                seatNumber = random.choice(self.li)
                print("Ticket has been Booked And your Seat Number is : ",seatNumber)
                self.li.remove(seatNumber)
                self.seats = self.seats-1
        def cancleTicket(self,seatNumber):
            if seatNumber not in self.li:
                self.seats = self.seats+1
                print("Ticket has been Cancelled")
                self.li.append(seatNumber)
            else:print("Entered wrong seat number")

interCity = Train(160583,70,10)
interCity.getStatus()
interCity.fareInfo()
interCity.bookTicket()
interCity.getStatus()
interCity.bookTicket()
interCity.bookTicket()
interCity.getStatus()
interCity.cancleTicket(10)
interCity.getStatus()'''
'''#Problem 6 Can we use other name in place of self? ANS:"Yes"
class Example :
    def __init__(other) -> None:
        other.name = "sai Kumar"#No error
    def printName(another) :
        print(another.name)
exp = Example()
exp.name = "sai Krishna"
exp.printName()'''