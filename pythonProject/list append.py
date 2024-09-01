list1=[2,3,4,5,6]
list2=list1
list2.append(10)
print(list1)
#.append(10) is used to add the element at the end
#list1.insert(1:3) is used to add 3 to a particular index
#list2=list1.copy() will copy the dails of the list1 and create a new list2 which will not have relationship with list1 after copying
list2 = list1[1:2] #this copies from index 1 to index 2
print(list2)
list3 = list1 + list2
print(list3)
mylist1=[1,2,3,4,6]
mylist2=[7,8,9,10,11]
#mylist1.append(mylist2[:])
print(mylist1)

for x in mylist2:
    mylist1.append(x)
print(mylist1)

list12=[2,4,6]
list13=[7,8,9,10,11,12]

for x in list13:
    if x %2 ==0:
        list12.append(x)
print(list12)

