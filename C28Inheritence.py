'''#Single Inheritence
class Person :
    country = "India"
    dress = "Casual"
    def __init__(self) -> None:
        self.name = "sai krishna"
        self.aadhar = 98457234
    def whereIam(self):
        print("I ma in house")   
class Student(Person):
    CollegeName = "CMR"
    dress = "Uniform"
    def __init__(self) -> None:
        super().__init__()#Compolsary if we want name and aadhar
        self.RollNo = 552
        self.branch = "cse"
        
    def whereIam(self): #Method overriding
        print("I am in college")
        
# person = Person()
# print(person.country)
# person.whereIam()
# print()
# print(person.dress)
student = Student()
# print(student.CollegeName)
# print(student.country)
# student.whereIam()#Method overriding
# print(student.dress)

#accesing instance variable :
# print(student.name)
# print(student.aadhar)
# print(student.name)'''
'''#Multiple inheritence
class Animal :
    def __init__(self,name) -> None:
        self.name = name
    def speak(self):
        pass
class Bird :
    def fly(self):
        print(f"{self.name} is flying ")  
class Eagle(Animal,Bird) : 
    def speak(self):
        print(f"{self.name} is speaking : Kuoooooo,Kuooooooo")

eag = Eagle("Hulk")
eag.fly()
eag.speak()'''
'''#MultiLevel inheritence
class Country :
    Planet = "Earth"
    def __init__(self,CountryName="Inida",CountryCapital = "Delhi",currencey = "Rupees(₹)",presidentOrPrimeMinister = "Narendra Modi") -> None:#Default values
        self.CountryName = CountryName
        self.CountryCapital = CountryCapital
        self.currency = currencey
        self.presidentOrPrimeMinister = presidentOrPrimeMinister
    def countryDetials(self):
        
        print("******************* Country Details *********************")
        print(f"Name : {self.CountryName}\nCapital : {self.CountryCapital}\nCurrency : {self.currency}")
    
class State(Country) :
    def __init__(self, CountryName="Inida", CountryCapital="Delhi", currencey="Rupees(₹)", presidentOrPrimeMinister="Narendra Modi",StateName = "Telangana",StateCapital = "Hyderabad",chiefMinister = "Revanth Reddy") -> None:
        super().__init__(CountryName, CountryCapital, currencey, presidentOrPrimeMinister)
        self.StateName = StateName
        self.StateCapital = StateCapital
        self.chiefMinister = chiefMinister
    def stateDetails(self):
        super().countryDetials()
        print("******************* State Details *********************")
        print(f"Name : {self.StateName}\nCapital : {self.StateCapital}\nCheif Minister : {self.chiefMinister}")
    def country(self): #return country class object
        return Country()
class Districts(State) : 
    def __init__(self, CountryName="India", CountryCapital="Delhi", currencey="Rupees(₹)", presidentOrPrimeMinister="Narendra Modi", StateName="Telangana", StateCapital="Hyderabad", chiefMinister="Revanth Reddy",DistrictName="Nizamabad",MLA = "Ganesh Gupta") -> None:
        super().__init__(CountryName, CountryCapital, currencey, presidentOrPrimeMinister, StateName, StateCapital, chiefMinister)
        self.DistrictName = DistrictName
        self.MLA = MLA
    def DistrictDetails(self):
        super().stateDetails()
        print("******************* District Details *********************")
        print(f"Name : {self.DistrictName}\nMLA : {self.MLA}")
    def state(self):   #return state class object
        return State()
    def country(self): #return country class object
        return Country()
# India = Country()
# India.countryDetials()
# print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
# Telangana = State()
# Telangana.stateDetails() 
# print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
# Nizamabad = Districts()
# Nizamabad.DistrictDetails()
    
# Dynamic Dispatch
# Telangana = State()
# uk = Telangana.country()
# uk.__init__()
# uk.CountryName="United Kingdom"
# uk.CountryCapital="England"
# uk.currency="Dollar($)"
# print(uk.countryDetials())

#We work like this also:
# Nizambad = Districts()
# Delhi = Nizambad.state()
# India = Delhi.country()'''
'''#Propery Decorators getter and setter 
class Rectangle:
    def __init__(self,length=0,breadth=0) :
        pass
        self.length = length
        self.breadth =  breadth
    @property
    def area(self):
        return self.breadth*self.length
    @area.setter
    def area(self,are):
        self.length = are / self.breadth
    @property
    def length(self):
        return self._length
    @length.setter
    def length(self,leng):
        self._length = leng
    @property
    def breadth(self):
        return self._breadth
    @breadth.setter
    def breadth(self,leng):
        self._breadth = leng
        
rectangle = Rectangle(56,45)
print(rectangle.area)
rectangle.length=34
rectangle.breadth=25
print(rectangle.area)
rectangle.area=100
print(rectangle.length)
print(rectangle.breadth)'''
'''#Operator oveloading
class Number :
    def __init__(self,num) -> None:
                self.num=num
    def __add__(self,obj):
        return self.num+obj.num
    def __mul__(self,obj):
        return self.num*obj.num

number1 = Number(5)
number2 = Number(10)
sumAns = number1+number2
print(sumAns)    
print(number1*number2)'''
        