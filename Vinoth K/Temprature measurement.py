import random
l=0
while(l<=200):
    temp=random.randrange(1,200)
    hum=1/temp
    if(temp>190):
        print("The temperature",temp,"is too high")
    else:
        print("The temperature",temp,"is normal")
    l+=1