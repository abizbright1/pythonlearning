name =["john jame work", "nur age james", "henry jerico jeremiah", "john eze wick", "henry chisom wick"]
mymapp={}
for x in name:
    spltted_name=x.split()
    first_name=spltted_name[-1]
    if first_name not in mymapp:
        mymapp[first_name]=1

    else:
        mymapp[first_name] += 1
print(mymapp)