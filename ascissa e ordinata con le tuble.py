import random
punti_cartesiani=[]
for i in range(0,20):
    punto=(random.randint(0,10),random.randint(0,10))
    punti_cartesiani.append(punto)
    
massimo=punti_cartesiani[0]
for i in range(1,20):
    if punti_cartesiani[i][0] > massimo[0]:
        massimo=punti_cartesiani[i]
print(massimo)

minimo=punti_cartesiani[1]
for i in range(1,20):
    if punti_cartesiani[i][1] < minimo[1]:
        minimo=punti_cartesiani[i]
print(minimo)