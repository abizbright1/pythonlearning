print('hello')
age = 50
print(id(age))
age = 55
_a = 'work'
print(_a)
print(type(age))
print(type(_a))
print("hello my name is nur and how old are you", age)
number = "12345"
number1 = "67890"
number3 = int(number)
number4 = int(number1)
print(number3)
print(number4)
print(type(number4))
a = 10
print(str(a))
#x = 22
#print(x)
#whoyou()

age = 15
def agefn():
    global age
    age=20
    print(age)
agefn()
print(2/3)
print(2//3)
x = 3


x+=3
print(x)
x-=3
print(3)
y = 20
print(y == 3)
u = 'hello word'
print("h" in u)
print("hello" in u)

t = [5,6,7,8]
print(6 in t)

r=7
z=5
#print(r^z)
#print(~z)
print(bin(z))####

zork = 0
print('before', zork)
#for thing in

##Strings

d =  "what's your name"
print(d)
r = '''it's "morning"'''
print(r)
mystring =      '     hello world      '
print(len(mystring))
print(mystring[2])

w = 5
for k in mystring:
    print(k)
for i in range(w):
    print(i)
print("h" not in mystring)
print(mystring[1:4])
print(mystring.upper()) # upper case
print(mystring.lower()) # lower case
print(mystring.strip()) # remove spaces
print(mystring.replace("h","w")) #change words
fruits = "mango, orange, cherry, gover, garri"
print(fruits.split(","))#slip yhe variables friuts
age = 15
print(mystring + "what the fuck are you doing please" + fruits)

#print(mystring.split(" "))
txt = 'what the fuck is this now ' + str(age)

#making use of the f" ans {} to make variable dynamic
txt = f"what are you doing right now at {age} ?,"
print(txt)

###boolean

print(100>20)
print(100+20)

# If condition
a = 20
b = 40
if a > b :
    print("a is greater")
else:
    print("b is greater")
mylist = [1,2,3,4,5,5,6,6]
print(len(mylist))
print(type(mylist))
newlist = [1,2,3,'work',40]
print(type(newlist))
print(mylist[3])
if 5 in mylist:
    print("ÿes it is")
else:
    print("not in it")
#add_new=newlist101[3:5]=[200,909]

#print(add_new)
#print(newlist101)
#insert and append prompts
mylist[2] = [2000,333,3333,3333]
print(mylist)
mylist[1:5] = [100]
#print(mylist)
mylist.insert(2, 2000)# the position is the first number and the last one is the value you want to add to the varibale
print(mylist)
mylist.append(88)#remove only takes away the object without stating the index or position
print(mylist)
#pop for index remover
#remove is to remove the object
mylist.pop(2)
print(mylist)
#delete
del mylist[2] #del works like the pop and it can be used to delete everything in the list
print(mylist)
#del mylist  # this is used to delete everything on my mylsit or everything in the mylist
print(mylist)
#.clear
mylist.clear()
print(mylist)
print(id(mylist))

#loop
mylist1 = (1,2,3,4,5,6)
for x in mylist:
    print(x)

##print(range(10))
#for x in mylist1:
#    print(range)
    lenght=len(mylist1)
#for i in range(lenght):
    print(mylist1[i])
#mylist2 = [100,200,300,400]
#lenght1 = len(mylist2)

#maxi = mylist2[0]
#for x in mylist(maxi):
#    if x>maxi :
 #       maxi=x
#print(maxi)
#printing maximum code

#mymylist = [300,400,240,660,700]
#maximum = mymylist[0]
for x in mymylist:
    if x>maximum:
        maximum=x
#print(maximum)

mini = mymylist[0]
for x in mymylist:
    if x < mini:
        mini=x
print(mini)
