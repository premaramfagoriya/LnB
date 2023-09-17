#Task 2
#addition till n number
def sum():
    number=int(input("numer for factorial addition"))
    add=0
    while number>0:
        add=add+number
        number=number-1
    print("sum = ",add)
sum()