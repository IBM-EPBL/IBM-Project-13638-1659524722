import random
Temp = random.randrange(0,100)
Humid = random.randrange(0,100,10)
print("sensed Temperature:%d degree celsius" % Temp)
print("sensed Humidity:%d percentage" % Humid)
if Temp>=40:
    print("wake up the alarm...danger!")
else:
   print("Temperature  is normal")
if Humid<30:
 print("Low Humid")
elif Humid>30:
    if Humid<50:
       print("Humid is normal")
    if Humid>50:
       print("Humid is high")
    
       
        
