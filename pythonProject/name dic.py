name =["john work", "nur james", "henry jeremiah", "john wick", "henry wick"]
mymapp={}
for x in name:
    spltted_name=x.split()
    first_name=spltted_name[0]
    if first_name not in mymapp:
        mymapp[first_name]=1

    else:
        mymapp[first_name] += 1
print(mymapp)