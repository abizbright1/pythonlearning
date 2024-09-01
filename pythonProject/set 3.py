l1 = [1,2,3,3,4,4,5,5,6,6]

# l2=[]
myset = set()
i = 0
while i < len(l1):
    if l1[i] not in myset:
        myset.add(l1[i])
        i = i +1
    else:
        i +=1

print(myset)
