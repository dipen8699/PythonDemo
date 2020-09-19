a = int(input("Enter num:"))
b = int(input("enter 1 or 0"))
c = bool(b)
if c==True :
    for i in range(1,a+1):
            print("*"*int(i))
elif c==False:
    for i in range(a,o,-1):
            print("*"*int(i))
