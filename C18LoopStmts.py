'''#while loop
i =0
while i<10 :
    print("Number = ",i)
    i=i+1
else : print("The loop is done")

while i<10 :
    if i==4 : break
    print("Number = ",i)
    i=i+1
else : print("The loop is done")

while i<10 :
    i=i+1
    if i==4 : continue
    print("Number = ",i)
    
else : print("The loop is done")


num = []
i=1
while i<5:
    user_input = input("Enter your phone number : ")
    if user_input.isdigit() :
        num.append(int(user_input))
        i +=1
    else : print("Invalid number")
print("Your phone numbers : ")
for item in num:
    print(item)'''
'''#for Loop
name = "Sai Krishna"
for i in name:
    print(i,end=", ")

tup = (34,62,61,46)
for i in tup:
    print(i,end=", ")

for i in range(10):
    print(i,end=", ")

for i in range(1,11):
    print("5 X",i,"=",5*i)'''
