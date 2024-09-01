inputt=[1,2,3,4,5,6]
mym ={}
sum_key = 0
sum_value = 0
for x in inputt:
        mym[x] = x*x
        sum_key += x
        sum_value += mym[x]
print(mym)
print(sum_key)
print(sum_value)
mystring = "this is a simple string used for testing vowels"
vowels = "a e i o u"
mymap ={}
count = 0
for x in mystring:
    if x not in mymap:
        if x in vowels:
            count=count+1
        # if x =="aeiou":
        #     continue
        mymap[x]=1
print(mymap)
print(count)
