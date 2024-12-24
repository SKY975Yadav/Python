'''#Problem 1 : table using for
num = int(input("Enter the number of a table that you want to print : "))
for i in range(1,11):
    print(num,"X",i,"=",num*i)'''
'''#problem 2 Greeting names in list
li = ["Sai","Kiran","Eshwar","Kaleem"]
for item in li :
    print(f"Good Morning Mr.{item}, Welocme to India")'''
'''#Problem 3  table using while
num = int(input("Enter the number of a table that you want to print : "))
i=1
while i<=10:
    print(num,"X",i,"=",num*i)
    i += 1'''
'''#Problem 4 Prime number
num = int(input("Enter the number : "))
i=2
while i<num :
    if(num%i==0): 
        print("Given number is not a prime number ")
        break
    i=i+1
else:print("Given number is a prime Number")'''
'''#Problem 5 
num = int(input("Enter the number : "))
i = 1
sum =0
while i<=num:
    sum = sum +i
    i=i+1
print(sum)'''
'''#Problem 6 Factorial of given number
num = int(input("Enter the number : "))
fact = 1
for i in range(1,num+1):
    fact = fact*i
print(fact)'''
'''#Problem 7
n=3
for i in range(3):
    print(" "*(n-i-1),end=" ")
    print("*"*(2*i+1),end=" ")
    print(" "*(n-i-1))'''
'''#Problem 8
for i in range(1,4):
    print("*"*(i))'''
'''#Problem 9
for i in range(3):
    if(i==1) : print("*  *")
    else : print("****")'''
'''#Problem 10 Printin of a table in reverse order
num = int(input("Enter the number : "))
for i in range(10,0,-1):
    print(f"{num} X {i} = {num*i}")'''