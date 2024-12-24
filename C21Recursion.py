#Factorial  Number 
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
#Fibanocci Number
def fibonacci(n): 
    if n==0 or n==1 :
        return n
    return fibonacci(n-1)+fibonacci(n-2)
num = int(input("Enter the number : "))
print("Factorial of a number is : ",fact(num))
print("Fibonacci of a number is : ",fibonacci(num))
