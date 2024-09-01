x =100
if 0:
    print(x)
else:
    print("good work bro")

a=100
b=100
if a > b:
    print("a is greater")
elif b==a:
    print("whatever")
else:
    print("b is greater")

if a % 2 == 0:
    print("even")
if a % 4 == 0:
    print("even more")
if a % 8 == 0:
    print("more more even")

#but
if a % 2 == 0:
    print("even")
elif a % 4 == 0:
    print("more")
else:
    print("much more even")

zork = 0
print('befor', zork)
for x in [9,44,12,3,77,14]:
    zork = zork + 1
    print(zork, x)
print('after', zork)

a = 30
b = 40
c = 30

if a > b:
    if a > c:
        print("a is greater")
elif b > a:
    if b > c:
     print("b is greater")
elif c > a:
    if c > b:
        print("c is greater")
else:
    print("all is equal")

if a > b and a > c:
        print("a is greater")
elif b > a and b > c:
     print("b is greater")
elif c > a and c > b:
        print("c is greater")
else:
    print("all is equal")

malist = [1,2,3,4,0,5,6,7,8,9]
for x in malist:
    if x == 0:
        break
    print(x)

nurlist = ("nurlista")
lenghtn=len(nurlist)
for x in nurlist:
    print(x)

malist = [1,2,3,4,0,5,6,0,7,8,0,9]
#bbb=[]
#for x in malist:
 #   if x == 0:
  #      continue
  #  print(x)

#for x in malist:
   # if x == 0:
  #      continue
 #   malist=bbb.append(x)
#print(bbb)

for x in malist:
    if x == o:
        malist.remove(x)
print(malist)