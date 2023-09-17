#Task1
#square of list and adding all the elementsof square list
l1=[2,4,6,8,10]
sum=0
square=[]
for i in l1:
    i=i**2
    square.append(i)
    sum=sum+i

print("list is :",l1)
print("square of list is :",square)
print("sum of the square of the elements if :",sum)