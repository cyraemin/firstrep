#merge two disctionaries
d1={10:100,20:200,30:300}
d2={40:400,50:500,60:600}
for i in d2:
    d1[i]=d2[i]
print(d1)
#sum all values in a dictionary
d1={10:100,20:200,30:300}
sum=0
for i in d1:
    sum=sum+d1[i]
print(sum)
#count frequency of each element in list
a=[1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7,7]
d={}
for i in a:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
print(d)
#combine two dictionaries by adding values for common keys
d1={10:100,20:200,30:300}
d2={40:400,50:500,60:600}
for i in d2:
    if i in d1.keys():
        d1[i]+=d2[i]
    else:
        d1[i]=d2[i]
print(d1)
