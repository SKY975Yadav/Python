'''# List
li = [34,23,23,"sai krishna",True,34.23]
print(li[0]+34)
print(li[3]+" I am from nizamabad in Telangana")
print(li)
print(li[2:4]'''

#List Methods
data = [32,31,34,1235,1124,513,1161,23,151,1,25]
data[8] = 150
print("Before sorting :", data)
data.sort()
print("After sorting :", data)
data.append(32324)
print("After Append 32324 :", data)
few = [56,22,2351,91,15]
data.extend(few)
data.sort()
print("After Append 'few' List :", data)
data.reverse()
print(data)
data.reverse()
data.insert(4,46)
print(data)
data.pop(3)
data.remove(32324)
print(data)
some = [34,262,83,256]
newList = data + some
some = some *3
print("Some after using '*'",some)
print(newList)
print(34 in some)
print(52 in some)
print(34 not in some)
print(23 not in some)
print(tuple(some))
print(data.count(31))
