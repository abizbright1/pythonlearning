newlist101=[x for x in range(10)]

mylisw=[100,3,4,2,9,7,8]
mylisw.sort()
print(mylisw)

stringlist=["ws", "amazon", "aws", "microsoft"]
stringlist.sort()
print(stringlist)

mystring=["Z","z","A","a","B","b","c"]
mystring.sort()
print(mystring)

mylist8=[1,2,3,4.3,3.3]
mylist8.sort()
print(mylist8)
print(type(mylist8[1]))

#decending order
mylist8.sort(reverse=True)
print(mylist8)

#.pop(1) is used to remove the index nposition 1
#.remove(1) element 1 in the list

#sorting without considering the case we use:
mylista=["A","B","D","c","b","d","C"]
mylista.sort(key=str.upper)
print(mylista)