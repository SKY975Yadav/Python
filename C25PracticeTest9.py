'''#Problem 1 string is in file or not
with open("poem.txt") as f:
    rd = f.read()
if "twinkle" in rd :
    print("Twinkle is present in given poem")
else:print("Twinkle is not present in given poem")'''
'''#Problem 2 update highscore file
def game():
    return 4095725;
with open("HighScore.txt") as f :
    HighScoreAsString = f.read()
newHighScore = game()
if HighScoreAsString == '' or int(HighScoreAsString)< newHighScore :
    with open("HighScore.txt","w") as f:
        f.write(str(newHighScore))'''
'''#Problem 3 Multiplication tables in files
for item in range(2,21):
    fileWriting = open(f"MultiplicationTables/Table{item}.txt","w")
    text = ''
    for i in range(1,11):
        text = text + f"{item} X {i} = {item*i}\n"
    fileWriting.write(text);  '''
'''#Problem 4 Replacing donkey with ######
StrOfFileWrite = ''
with open("donkey.txt") as fileWrite :
    StrOfFileWrite = str(fileWrite.read())
    if "donkey" in StrOfFileWrite:
        StrOfFileWrite = StrOfFileWrite.replace("donkey","######")
with open("donkey.txt","w") as f :
    print(StrOfFileWrite)
    f.write(StrOfFileWrite) '''
'''#Problem 5 Replacing list of words with ######
words = ["sai","yadav","sanjey","naidu"]
StrOfFileWrite = ''
with open("list.txt") as fileWrite :
    StrOfFileWrite = str(fileWrite.read())
    for word in words : 
        if word in StrOfFileWrite:
            StrOfFileWrite = StrOfFileWrite.replace(word,"######")
with open("list.txt","w") as f :
    print(StrOfFileWrite)
    f.write(StrOfFileWrite) '''
'''#Problem 6 Program for find word in log file
with open("log.txt") as f:
    st = f.read()
if "python" in st.lower() :
    print("Yes python in a log file ")
else : print("Python is not in log file") '''
'''#Problem 7 program for find line of a word of problem 6
i = 1
content = True
bol = False
with open("log.txt") as f:
    while content: 
        content = f.readline()
        if "python" in content.lower() :
            bol = True
            print("Yes python is present in log file at line number ",i)
        i = i+1
if bol == False: print("Python is not present")'''
'''#Problem 8 Copy of a text file 
with open("example.txt") as f :
    content = f.read()
with open("copy.txt","w") as f:
    f.write(content)'''
'''#Problem 9 Is both file content is same or not(i.e Identical or not)
with open("example.txt") as f :
    content1 = f.read()
with open("copy.txt","r") as f:
    content2 = f.read()
if content1==content2 : print("Yes, both files are identical ")
else : print("No, both files are not identical")'''
'''#Problem 10 Wipe out a file 
with open("example3.txt","w") as f :
    f.write("")'''
'''#Problem 11 Rename a file
import os
with open("OldName.txt") as f:
    content = f.read()
with open("NewName.txt","w") as f:
    f.write(content)
os.remove("OldName.txt")'''
