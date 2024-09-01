#b = int(input("base number:"))
#c = int(input("power of the number"))
#print(b**c)

#l1 = [1,1,2,2,3,3,3,4,4,4,4,5,5,5,5]
#l2 = []
#index = 0
#while index < len(l1):
#    if l1[index] not in l2:
#        l2.append(l1[index])
#        else:
#        index = index + 1
#print(l2)

ll=[1,2,3,4,5,6]
index = 0
llw=[]
duplicate = 0
while index < len(ll):
    if ll[index] in llw:
        print("duplicate")
        break
    else:
        llw.append(ll[index])
if index == len(ll):
    print("unique")


#b = int(input("number bro:"))

index=1

#while index <=10:
 #   print(f"{b}*{index}={b*index}")
 #   index += 1
t=int(input("your numeber :"))
sum_total=0

while index <= t:
    sum_total=sum_total+index

    index += 1

print(sum_total)


grade = int(input("my grade"))

if grade >= 90 and grade <= 100:
    print("A")
elif grade >= 80 and grade <90:
    print("B")
elif grade >= 70 and grade < 80:
    print("C")