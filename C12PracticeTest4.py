#Problem 1
fruits = ["Mango","Apple","Banana","Orange","Grapes","Cherry"]
#Problem 2
Marks = [45.23,89.62,92.34,95.00,74.23,68.34]
print("Marks : ")
print(Marks)
Marks.sort()
Marks.reverse()
print("Marks by Highest to lowest : ")
print(Marks)
#Prolem 3 Tuple Cannot be change in the tuple
panNumber = ("234AC5298",
             "234AC5298",
             "274AC5298",
             "234AE5223",
             "234BC5926",
             "283BG5227",)
# panNumber[0] = 234 Cannot modify tuple
print(panNumber)
#problem 4 Sum of list with 4 numbers
lis = [34,2,7,67]
print("Sum using sum() fun : ",sum(lis)) # or
sum = lis[0]+lis[1]+lis[2]+lis[3]
print("Sum by performing '+' : ",sum)
#problem 5 count no.of Zeroes in tuple
tup = (34,23,0,6234,20,0,235,0,25,0)
print(tup.count(0))
