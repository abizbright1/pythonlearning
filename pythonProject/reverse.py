mystring = "Python"
i = len(mystring)-1
reverse= mystring[i]

while i > 0:
    reverse = reverse+""+mystring[i-1]

    i -= 1
print(reverse)


i = len(mystring[5])
myreverse = " "
while i >= 0:
    myreverse =myreverse+mystring[i]
    i=i-1
print(reverse)


l1=[-1,1,2,-2,-5,5,-6,6,-7,7,-100]
pos = 0
neg = 0
index =0
while index < len(l1):
    if l1[index] >= 0:
        pos = pos + 1
    else:
        neg = neg + 1
    index += 1
print(neg)
print(pos)

l2 = [2,0,0,0,3,9,5,0,0,6]
index = l2[0]
while index < l2):
    if l2[index] == 0:
        l2.remove(l2[index])
    index += 1
print(l2)