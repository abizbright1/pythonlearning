a = ["ws", "amazon", "aws", "microsoft"]
max = a[0]

for x in a:
    if  len(x) > len(max):
        max = x
print(max)

#mylist=[2,1,6,1,7,1,1,2,3,4]
mylisy=[2,4,6,7,8]
count=0
for x in mylisy:
    if x==1:
        count = count + 1
print(count)

mylist=[1,2,3,4,5,6,7,8,9,10]
newlist101=[x for x in mylist if x % 2 == 0]
print(newlist101)

