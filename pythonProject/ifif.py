
malist = [1,2,5,6,0,7,8,0,9]
malist2 = [200,100,300,400,500]

#for x in malist:
 #   if x == 0:
  #      malist.pop()
#print(malist)
index = 0
for x in malist:
    if x == 0:
        malist.pop(index)
    index=index+1
print(malist)

for x in malist:
    for y in malist2:
        print(x,y)