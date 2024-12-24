#Empty set 
st = set()
st.add(34)#adding elements
st.add(52)
st.add("sai Krishna")
bol =  "sai Krishna" in st
# print(bol)
# print(len(st))
st.remove(52)
st.add(93)
st.add(72)
st.add(63)
# print(st)
st.pop()  
# print(st)
# st.add((14,235,614))
st.update([34,23,52])
st.update((372,725))
# print(st)

#Operations
st1 ={35,62,831,14,73}
st2 = {23,62,14,346,25,73}#B-A 
# print("Union : ",st2.union(st1))
# print("Intersection : ",st2.intersection(st1))
# print("Difference st2-st1 : ",st2.difference(st1))
# print("Symmetric difference : ",st2.symmetric_difference(st1))
# print("Disjoint : ",st2.isdisjoint(st1))

#spectial update operation
s1 = {23,52,17,57,24,23}
s2 = {52,16,432,52,432,2}
print("s1 = ",s1)
print("s2 = ",s2)
# s1.update(s2)
# print("s1 After update with s2(union) ",s1)

# s1.intersection_update(s2)
# print("s1 After update with s2(intersection) ",s1)
#Similar with difference and symetric difference

