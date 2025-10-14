import random
x=[]
y=[]
for i in range(0,20):
    x.append(random.randint(0,10))
    y.append(random.randint(0,10))

x_massimo=0
massimo=x[0]
for i in range(0,20):
    if x[i] > massimo:
        x_massimo=x[i]
        massimo=i

y_massimo=0
massimo=y[0]
for i in range(0,20):
    if y[i] > massimo:
        y_massimo=y[i]
        massimo=i

x_minimo=0
minimo=x[0]
for i in range(0,20):
    if x[i] < minimo:
        x_minimo=x[i]
        minimo=i



y_minimo=0
minimo=y[0]
for i in range(0,20):
    if y[i] < minimo:
        y_minimo=y[i]
        minimo=i
        
print(x_massimo)
print(y_minimo)
print(y_massimo)
print(x_minimo)
