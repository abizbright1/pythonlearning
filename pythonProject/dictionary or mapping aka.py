ny = {"name": "chioma","roll number":123,"branch": "csc"}
print(ny)

mydict=dict(name = 'nur', roll_number = 17656, branch = 'iesb')

print(mydict)
#myvalu = ny["roll number"]
myvalu = ny.get("roll number")
print(myvalu)
mylist = mydict.keys()
print(mylist)
for x in mylist:
    print(x)

myvalues= mydict.values()
print(myvalues)
for x in myvalues:
    print(x)
mydict["who"]="bright"
print(mydict)
x = "uni"
if x not in mydict:
    mydict["john"]="oga"

else:
    print("move on")
print(mydict)

x = "john"
if x in mydict:
    mydict.pop("branch")
print(mydict)
mydict.popitem()
print(mydict)
# del= delete the dictionary
# clear = clear the dictionary

for key in mydict:

    print(mydict.get(key))
myd1 = {1:2,4:4}
myd2 =myd1
myd1[8]=4
print(myd2)
myd3 =myd1.copy()
print(myd3)
myd1[7]=88
print(myd1)
print(myd3)
mylist1 = [1,1,1,2,2,2,3,3,3,3,4,4,5,5,6,6,6,7,7]
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0
count_7 = 0
for x in mylist1:
    count_1 = count_1 +1
    print(count_1)
    