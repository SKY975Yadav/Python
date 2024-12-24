'''#Problem 1 Vector 3d and 2d
class Vector2D:
    def __init__(self,i,j) -> None:
        self.i=i
        self.j=j
    def __str__(self) -> str:
        return f"{self.i}i + {self.j}j "
class Vector3D (Vector2D):
    def __init__(self, i,j,k) -> None:
        super().__init__(i,j)
        self.k=k
    def __str__(self) -> str:
        return f"{self.i}i + {self.j}j + {self.k}k"
    
vect1 = Vector2D(3,5)
vect2 = Vector3D(4,5,6)
print(vect1)
print(vect2)'''
'''#Problem 2 for multi level inheritence
class Animal:
    def __init__(self, species, habitat):
        self.species = species
        self.habitat = habitat

    def eat(self):
        print(f"{self.species} is eating")

    def sleep(self):
        print(f"{self.species} is sleeping")
class Pet(Animal):
    def __init__(self, species, habitat, name, owner):
        super().__init__(species, habitat)
        self.name = name
        self.owner = owner

    def play(self):
        print(f"{self.name} is playing with {self.owner}")
class Dog(Pet):
    def __init__(self, name, owner, breed, age):
        super().__init__('Dog', 'Domestic', name, owner)
        self.breed = breed
        self.age = age

    def bark(self):
        print("Woof! Woof!")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Owner: {self.owner}")
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age}")
# Create an instance of Dog
my_dog = Dog("Buddy", "John", "Labrador Retriever", 3)

# Access attributes and call methods
my_dog.display_info()
my_dog.eat()
my_dog.sleep()
my_dog.play()
my_dog.bark()'''
'''#Problem 3 Employee class increment salary related problem
class Employee :
    salary = 30000
    increment = 1.5
    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,newSal):
        self.increment = newSal/self.salary
emp = Employee()
# print(emp.salaryAfterIncrement)
print(emp.increment)
emp.salaryAfterIncrement=60000
print(emp.increment)'''
'''#Problem 4 Operetor overloading for Complex numbe
class Complex :
    def __init__(self,r,i) -> None:
        self.r=r
        self.i=i
    def __add__(self,obj):
        return Complex(self.r+obj.r , self.i+obj.i)
    def __mul__(self,obj):
        return Complex(((self.r*obj.r) - (self.i*obj.i)), ((self.r*obj.i)+(self.i*obj.r)))
    def __str__(self) -> str:
        if self.i<0:
            return f"{self.r} - {-self.i}i"
        return f"{self.r} + {self.i}i"
num1 = Complex(4,15)
num2 = Complex(6,15)
print(num1+num2)
num3 = Complex(5,-7)
num4 = Complex(8,-5)
print(num3*num4)'''
'''#Problem 5 Vector of N dimention  
def get_subscript(number):
    return chr(0x2080 + number)
def maximum(a,b):
    if a>=b : return a
    else : return b
class Vector:
    def __init__(self,li) -> None:
        self.li = li
    def __str__(self) -> str:
        temp = ""
        ind = 0
        for i in range(len(self.li)):
            # string = get_subscript(i)
            if i == len(self.li)-1:
                temp += f"{self.li[i]}a{ind}"# We can use string of 107 line also in place of ind
            else : temp += f"{self.li[i]}a{ind} + "
            ind +=1
        return temp
    def __add__(self,obj):
        big = maximum(len(self.li),len(obj.li))
        newList = []
        for i in range(big):
            newList.append(self.li[i]+obj.li[i])
        return Vector(newList)
    def __mul__(self,obj):
        big = maximum(len(self.li),len(obj.li))
        total = 0
        for i in range(big):
            total += self.li[i]*obj.li[i]
        return total
vec1 = Vector([5,5,10])
vec2 = Vector([4,2,1])
print(vec1 * vec2)
# print(vec1 + vec2)'''
'''#Problem 6 Vector of 3 dimentions as i+j+k
class Vector :
    def __init__(self,i,j,k) -> None:
        self.i = i
        self.j = j
        self.k = k
    def __str__(self) -> str:
        return f"{self.i}i+{self.j}j+{self.k}k"
vac = Vector(4,5,6)
print(vac)'''
'''#Problem 7 __len__() method for Vector class
def maximum(a,b):
    if a>=b : return a
    else : return b
class Vector:
    def __init__(self,li) -> None:
        self.li = li
    def __str__(self) -> str:
        temp = ""
        ind = 0
        for i in range(len(self.li)):
            # string = get_subscript(i)
            if i == len(self.li)-1:
                temp += f"{self.li[i]}a{ind}"# We can use string of 107 line also in place of ind
            else : temp += f"{self.li[i]}a{ind} + "
            ind +=1
        return temp
    def __add__(self,obj):
        big = maximum(len(self.li),len(obj.li))
        newList = []
        for i in range(big):
            newList.append(self.li[i]+obj.li[i])
        return Vector(newList)
    def __mul__(self,obj):
        big = maximum(len(self.li),len(obj.li))
        total = 0
        for i in range(big):
            total += self.li[i]*obj.li[i]
        return total
    def __len__(self):
        return len(self.li)
vec = Vector([3,7,2,6,8,2,3])
print(len(vec))'''