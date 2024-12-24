import mysql.connector
# Replace 'host', 'user', 'password', and 'database' with your actual connection details
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='6301722975',
    database='saikrishna'
)
# print(connection)
myConnection = connection.cursor()
#Creating databse:
# myConnection.execute("create database saiKrishna")
# myConnection.execute("SHOW DATABASES")
# for item in myConnection : 
#     print(item)
# myConnection.execute("DROP DATABASE sai")
# myConnection.execute("USE SAIKRISHNA")
#Creating table :
# myConnection.execute("CREATE TABLE EMPLOYEE(id int, name varchar(34))")
# myConnection.execute("show tables")
# for item in myConnection :
#     print(item)
#insert : 
# sql = "insert into employee values(%s,%s);"
# val = (23,"sai Kumar")
# myConnection.execute(sql,val)
# connection.commit()
#select : 
myConnection.execute("select * from employee")
res = myConnection.fetchall()
for x in res:
    print(x)


