a=int(input("Enter 1st no."))
b=int(input("Enter 2nd no."))
c=int(input("Enter 3rd no."))


if(a>b) & (a>c):
    print("a is greatest")
elif(b>c) & (b>a):
    print("b is greatest")
elif(c>a) & (c>b):
    print("c is greatest")