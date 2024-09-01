veg=["potato","spinach","carrot","cabbage","flower","ginger","garlic","cauliflower"]
x = 0
max1 = 0
mymap = {}
for x in veg:
    mymap[x]=len(x)
print(mymap)
for x in mymap:
     if mymap.get(x) > max1:
         max1 = mymap.get(x)
         max_key = x
print(max1)
print(max_key)

mystring = "programming in python"

mymapp = {}
for x in mystring:
    if x not in mymapp:
        if x == " ":
            continue
        mymapp[x] = 1
    else:
        mymapp[x]=mymapp[x] + 1
print(mymapp)
# the code abve was used to skip the spcae " " in the code. we can use it to skip any item in the list



