import random
i=0
while(i<=200):
    t=random.randrange(1,200)
    h=1/t
    if(t>190):
        print("The temperature",t,"is too high")
    else:
        print("The temperature",t,"is normal")
    i+=1
