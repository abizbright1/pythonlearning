mylist = [1,2,3,4,4,5,6,6,7,8,9,10]
mymap = {}
mymap["even"] = 0
mymap["odd"] = 0

for x in mylist:
    if x%2 == 0:
        mymap["even"] = mymap["even"] + x
    else:
        mymap["odd"] = mymap["odd"] + x
print(mymap)
