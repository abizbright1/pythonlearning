my1 = [2,3,4,5,6,7,8,9,10,11,12,13]
my2 = []
i=0
while i < len(my1):
    if my1[i] %2==0:
        my2.append(my1[i])
    i+= 1
print(my1)

l=["a", "aws", "bp", "mango"]

index=0
longest = l[index]
while index < len(l):
    if len(l[index]) > len(longest):
        longest = l[index]
    index += 1
print(longest)

l3 = [10,20,30,40,50]
sum = 0
i = 0
while i < len(l3):
    sum = sum + l3[i]
    i += 1
print(sum)
l4 = [2,3,1,1,2,1,3,1,1]
count = 0
i = 0
while i < len(l4):
    if l4[i] == 1:
        count = count + 1

    i += 1
print(count)

indexc=110
while index <= 120:
    print(index)
    index += 1

i = 6
summ = 1
while i >= 1:
    summ = summ * i
    i = i-1
print(summ)



bull = [1,2,3,4,5,6,7,8]
sum_odd=0
count_odd=0
count_even=0
sum_even=0
i = 0
while i < len(bull):
    if bull[i] %2==0:
        sum_even = sum_even + bull[i]
        count_even = count_even + 1

    else:
        sum_odd = sum_odd + bull[i]
        count_odd = count_odd + 1
    i += 1
print("this is the sum of odd number", sum_odd)
print("this is the sum of even numbers", sum_even)
print("this is he count of even numbers ",count_odd)
print("this is the count of odd numbers",count_even)


mystring = "Python"
i = len(mystring)


while i > 0:
    if mystring[i-1] > len(mystring):
        mystring[i] = 1

    i -= 1
print(mystring)




