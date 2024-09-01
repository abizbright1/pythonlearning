mylist = ["apple", "banaa", "cherry", "apricop", "blueberry"]
mymap= {}


for x in mylist:
    first_word = x[3]
    if first_word not in mymap:
        mymap[first_word] = 1
    else:
        mymap[first_word] += 1
print(mymap)