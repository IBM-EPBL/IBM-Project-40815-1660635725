import random
i=0
while(i<=100):
    temperature=random.randrange(1,100)
    humidity=1/temperature
    if(temperature>90):
        print("The temperature",temperature,"is too high")
    else:
        print("The temperature",temperature,"is normal")
    i+=1
