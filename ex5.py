import datetime
def gettime():
    return datetime.datetime.now()

def take(b):
    if b==1:
        c = int(input(" press 1 for exercise press 2 for food"))
        if (c==1):
            value = input("type here\n")
            with open("dipen-ex.txt","a") as o:
                o.write(str([str(gettime())])+":"+value+"\n")
            print("writing successful")
        if (c==2):
            value=input("type here\n")
            with open("dipen-food.txt","a") as o:
                o.write(str(str[gettime()])+":"+value+"\n")
            print("write successfully")
    elif b==2:
        c = int(input(" press 1 for exercise press 2 for food"))
        if (c==1):
            value = input("type here\n")
            with open("yash-ex.txt","a") as o:
                o.write(str([str(gettime())])+":"+value+"\n")
            print("writing successful")
        if (c==2):
            value=input("type here\n")
            with open("yash-food.txt","a") as o:
                o.write(str(str[gettime()])+":"+value+"\n")
            print("write successfully")
    elif b==3:
        c = int(input(" press 1 for exercise press 2 for food"))
        if (c==1):
            value = input("type here\n")
            with open("sk-ex.txt","a") as o:
                o.write(str([str(gettime())])+":"+value+"\n")
            print("writing successful")
        if (c==2):
            value=input("type here\n")
            with open("sk-food.txt","a") as o:
                o.write(str(str[gettime()])+":"+value+"\n")
            print("write successfully")
def retrieve(b):
    if b==1:
        c= int(input("press 1 for exercise press 2 for food"))
        if (c==1):
            with open("dipen-ex.txt") as r:
                for i in r:
                    print(i)
        elif (c==2):
            with open("dipen-food.txt")as r:
                for i in r:
                    print(i)
    if b==2:
        c= int(input("press 1 for exercise press 2 for food"))
        if (c==1):
            with open("yash-ex.txt") as r:
                for i in r:
                    print(i)
        elif (c==2):
            with open("yash-food.txt")as r:
                for i in r:
                    print(i)
    if b==3:
        c= int(input("press 1 for exercise press 2 for food"))
        if (c==1):
            with open("sk-ex.txt") as r:
                for i in r:
                    print(i)
        elif (c==2):
            with open("sk-food.txt")as r:
                for i in r:
                    print(i)
    else:
        print("please insert valid input")

print("Health Management chart")

a = int(input(" press 1 for log and press 2 for retrieve"))
if a==1:
    b = int(input("1 for dipen 2 for yash 3 for sk"))
    take(b)
if a==2:
    b = int(input(' 1 for dipen 2 for yash 3 for sk'))
    retrieve(b)
 