'''#Problem 1 Greatest of 3 numbers
def greatestOf3(a,b,c):
    if a>b and a>c : return a
    elif b>a and b>c : return b
    else : return c
num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
num3 = int(input("Enter Number 3 : "))
print("The Greatest of given 3 nubmers is : ",greatestOf3(num1,num2,num3))'''
'''#Problem 2 Celsius to Fahrenheit and Fahrenheit to Celsius
def cToF(c):
    return format((c*9/5)+32,".2f")
def fToC(f):
    return format((f-32)*(5/9),".2f")
# cel = int(input("Enter Celsuis : "))
# print(f"Fahrenhiet of Celsius{cel} is : ",cToF(cel))
far = int(input("Enter Fahrenhiet : "))
print(f"Celsius of Fahrenhiet {far} is : ",fToC(far))'''
'''#Problem 3 Calc sum of n numbers using recursive
def sumOfN(n):
    if n==1 : return 1
    return n+sumOfN(n-1)
num = int(input("Enter the number : "))
print("The Sum of given natural numbers is : ",sumOfN(num))'''
'''#Problem 4 Function for printig special pattern
def pat(n):
    if n==0 : return
    print("*"*n)
    return pat(n-1)
num = int(input("Enter the number : "))
pat(num)'''
'''#Problem 5 Remove a word from string and strip it

def remove_Word_from_String(String,word):
    newStr = String.replace(word,"")
    return newStr.strip()
text = "This is my name Sai Krishna Yadav"
print(remove_Word_from_String(text,"Sai"))'''
'''#Problem 6 fucntion for multiplication table
def mulTable(n):
    for i in range(1,11):
        print(f"{n} X {i} = ",n*i)
num = int(input("Enter the Number : "))
mulTable(num)'''