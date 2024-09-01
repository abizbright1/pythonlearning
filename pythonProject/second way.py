mylist12=[12,200,400,32,5000,450,600,420,300]
maximum = 200
maximum_index = 0
maximum = mylist12[0]
lenght = len(mylist12)
for x in range(lenght):
    if mylist12[x] > maximum:
        maximum = mylist12[x]
        maximum_index = x
print(maximum)
print(maximum_index)


minimum = 400
minimum_index = 1
minimum = mylist12[1]
lenght = len(mylist12)
for x in range(lenght):
    if mylist12[x] < minimum:
        minimum = mylist12[x]
        minimum_index = x
print(minimum)
print(minimum_index)

mylist = [2,3,4,5,6,7,8,9,10]
newlist = []
oddlist =[]
for x in mylist:
    if x % 2==0:
        newlist.append(x)
    else:
        oddlist.append(x)
print(newlist)
print(oddlist)

sum = 0
for x in mylist:
    sum = sum + x
print(sum)

evensum=0
oddsum=0

for x in mylist:

    if x % 2==0:
        evensum = evensum + x
    else:
        oddsum = oddsum + x
print(oddsum)
print(evensum)

a = ["ws", "amazon", "aws", "microsoft"]
max = a[0]
max_index=1
for x in a:
    if max > len(a[x]):
        max = len(a[x])
    print(max)