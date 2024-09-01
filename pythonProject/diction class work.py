mylist1 = [1,1,1,2,2,2,3,3,3,3,4,4,5,5,6,6,6,7,7]
mymap={}
for x in mylist1:
    if x not in mymap:
        mymap[x] = 1

    else:
        mymap[x] =mymap[x] + 1
print(mymap)
max = 0
for x in mymap:
    if mymap.get(x) > max:
        max = mymap.get(x) + 1
print(max)

veggies=["carrot","potato","spinach","carrot","cabbage","flower","ginger","garlic","garlic"]
mymap1 = {}
for x in veggies:
    if x not in mymap1:
        mymap[x] = "carrot"
    else:
        mymap1[x] = mymap1[x]+1
print(mymap1)

