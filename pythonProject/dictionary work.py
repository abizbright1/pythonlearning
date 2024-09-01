veggies=["carrot","potato","spinach","carrot","cabbage","flower","ginger","garlic","garlic","garlic"]
mymap1 = {}
for x in veggies:
    if x not in mymap1:
        mymap1[x] = 1
    else:
        mymap1[x] = mymap1[x]+1
print(mymap1)
maxx = 0

for x in mymap1:
    if mymap1.get(x) > maxx:
        maxx = mymap1.get(x)
        maxx_key = x
print(maxx)
print(maxx_key)

