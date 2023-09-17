#Task 3
#Reverse the string word by word
def rev():
    line="MY NAME IS PREMARAM"
    list=line.split()[::-1]
    return list
print(rev())