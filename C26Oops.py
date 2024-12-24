#CLass Variable and Methods
class Student :
    CollegeName = "Brillian institute of engineering and technology" #Class Variable
    @classmethod
    def getCollegeName(cls):
        return cls.CollegeName;
student1 = Student()
# print(Student.getCollegeName()) # Accessing Class method using class.method
# print(Student.CollegeName) #Accessing class variable using Class.variable
# print(student1.getCollegeName()) #Accessing Class method using Object.method
# print(student1.CollegeName) #Accessing Class method using Object.variable

#Instance variable and methods using __init__ Method
class Employee :
    ComapnyName = "Google"
    # def __init__(self) -> None:#Default 
    #     # print("This is constructor")
    #     self.name = ''
    #     self.Id = 0
    #     self.salary = 0
    def __init__(self,name,id,salary) -> None:#Parameter constructor
        self.name = name
        self.Id = id
        self.salary = salary
    def PrintDetails(self) -> None:
        print(f"Name = {self.name}\nId = {self.Id}\nSalary = {self.salary}")
        print(self.ComapnyName)
    def getSalary(self):
        return self.salary
    def setSalary(self,amount):
        self.salary = amount
    @staticmethod
    def greet():
        print("Here are the details : ")
# emp1 =Employee()
# emp1.name = "SAI kRISHNA YADAV"
# emp1.Id = 552
# emp1.salary = 50000
# emp2 =Employee()
# emp2.name = "Rahul YADAV"
# emp2.Id = 507
# emp2.salary = 42000
# emp1.PrintDetails()
# emp2.PrintDetails()
emp3 = Employee("Mahesh",17,45000)
emp3.ComapnyName = "YouTube"
# emp3.PrintDetails()
# emp3.setSalary(60000)
# Employee.ComapnyName = "FaceBook"
emp3.greet()
emp3.PrintDetails()
emp4 = Employee("Uday",4,50000)
emp4.PrintDetails()

#What is both class variable and instance variable has same name :
#Solution : instance vaiable will prefer first if it is not present then class variable will call