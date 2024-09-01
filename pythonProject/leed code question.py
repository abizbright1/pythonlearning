mystring = "this is a simple string used for testing vowels"
vowels = ["a","e","i","o","u"]
mymap ={}

for x in mystring:
    if x in vowels:
        if x in mymap:
            mymap[x] += 1
        else:
          mymap[x] =1

print(mymap)