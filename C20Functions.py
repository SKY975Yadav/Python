def printHelloWorld():
    print("Hello World")
# printHelloWorld()   
#Default function :
def greet(name = "Satranger"):
    print(f"Hi,{name} have a good day")
greet("Sai Krishna")
def sumList(li) :
    sum=0
    for item in li :
        sum +=item
    return sum
def printList(li) :
    for item in li:
        print("Marks : ",item)
def printDict(di) :
    for key,value in di.items() :
        print(f"{key} : {value}")
cseMarks = [34,26,23,62,23]
eceMarks = [36,64,62,84,83]
eeeMarks = [53,83,53,83,23]
# print("Printing CSE sum students Marks ",sumList(cseMarks))
# print("Printing ECE sum students Marks ",sumList(eceMarks))
# print("Printing EEE sum students Marks ",sumList(eeeMarks))
# printList(cseMarks)
# print("\n")
# printList(eceMarks)
# print("\n")
# printList(eeeMarks)

#Dictionary using functions
Colleges = {
    "BRIL" : {
        "CSE":{
            "21QA1A0552" : {
                "Name" : "Sai Krishna",
                "Age ": 21,
                "Marks": 95.34
            },
            "21QA1A0553" : {
                "Name" : "Sindhu",
                "Age ": 21,
                "Marks": 99.34
            },
            "21QA1A0554" : {
                "Name" : "Bhavana",
                "Age ": 20,
                "Marks": 97.34
            }
        },
        "ECE":{
            "21QA1A0652" : {
                "Name" : "Sai Krian",
                "Age ": 21,
                "Marks": 91.33
            },
            "21QA1A0653" : {
                "Name" : "Mahesh",
                "Age ": 21,
                "Marks": 92.52
            },
            "21QA1A0654" : {
                "Name" : "Divya",
                "Age ": 20,
                "Marks": 93.74
            }
        },
        "EEE":{
            "21QA1A0352" : {
                "Name" : "Kumar Karthikiya",
                "Age ": 21,
                "Marks": 93.34
            },
            "21QA1A0353" : {
                "Name" : "Balaram",
                "Age ": 21,
                "Marks": 89.34
            },
            "21QA1A0354" : {
                "Name" : "Kavya",
                "Age ": 20,
                "Marks": 92.34
            }
        },

    },"KNRR" : {
        "CSE":{
            "21QA1A1552" : {
                "Name" : "Rama Krishna",
                "Age ": 22,
                "Marks": 95.34
            },
            "21QA1A1553" : {
                "Name" : "Sri latha",
                "Age ": 22,
                "Marks": 99.23
            },
            "21QA1A1554" : {
                "Name" : "Ramya Krishna",
                "Age ": 19,
                "Marks": 93.34
            }
        },
        "ESE":{
            "21QA1A1652" : {
                "Name" : "Sukesh Krian",
                "Age ": 21,
                "Marks": 93.56
            },
            "21QA1A1653" : {
                "Name" : "Rahul",
                "Age ": 21,
                "Marks": 97.34
            },
            "21QA1A1654" : {
                "Name" : "Sindhu",
                "Age ": 23,
                "Marks": 93.74
            }
        },
        "EEE":{
            "21QA1A1352" : {
                "Name" : " Karthikiya",
                "Age ": 23,
                "Marks": 97.23
            },
            "21QA1A1353" : {
                "Name" : "Yonesh",
                "Age ": 20,
                "Marks": 95.34
            },
            "21QA1A1354" : {
                "Name" : "Uday",
                "Age ": 21,
                "Marks": 95.34
            }
        },

    },"BRIG" : {
        "CSE":{
            "21QA1A0552" : {
                "Name" : "Parmesh",
                "Age ": 19,
                "Marks": 93.37
            },
            "21QA1A0553" : {
                "Name" : "Chandrashekar",
                "Age ": 21,
                "Marks": 99.99
            },
            "21QA1A0554" : {
                "Name" : "Bhavishya",
                "Age ": 21,
                "Marks": 94.62
            }
        },
        "ESE":{
            "21QA1A0652" : {
                "Name" : "Suresh",
                "Age ": 20,
                "Marks": 96.73
            },
            "21QA1A0653" : {
                "Name" : "Mallesh",
                "Age ": 22,
                "Marks": 89.82
            },
            "21QA1A0654" : {
                "Name" : "Dileep",
                "Age ": 21,
                "Marks": 95.74
            }
        },
        "EEE":{
            "21QA1A0352" : {
                "Name" : "Kumar Sangakara",
                "Age ": 23,
                "Marks": 99.64
            },
            "21QA1A0353" : {
                "Name" : "Rohit",
                "Age ": 21,
                "Marks": 90.94
            },
            "21QA1A0354" : {
                "Name" : "Virat",
                "Age ": 20,
                "Marks": 95.14
            }
        },

    },
}
# printDict(Colleges["BRIL"]["CSE"]["21QA1A0552"])
print(Colleges["BRIL"]["CSE"]["21QA1A0552"]["Name"])

