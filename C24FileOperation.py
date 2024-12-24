#Open a file 
file = open("example2.txt","r")#Open a file or
# file = open("example.txt","r")
#Reading from a file 
# read1 = file.read()#read total text
# read2 = file.read(5)#read limit charecters
# read3 = file.readline()#Single line
# read4 = file.readlines()#All lines
# print(read1)
# print(read2)
# print(read3)
# print(read4)

#Writing a file
# write = file.write("I am a great Coder")
file.close()

#using with
with open("example2.txt","r") as f:
     a = f.read()
print(a)
    