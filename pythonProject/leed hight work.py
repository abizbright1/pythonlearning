sentence = "the quick brown fox jumps over the dog the dog barks"

mylist =sentence.split()
print(mylist)
mymapp ={}

for x in mylist:
    if x not in mymapp:
        mymapp[x] = 1

    else:
        mymapp[x] += 1
print(mymapp)