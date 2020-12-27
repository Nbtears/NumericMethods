#Switch data of x and y values as need it 

import numpy as np
import matplotlib.pyplot as plt

#Input data
x=np.array([70,63,72,60,66,70,74,65,62,67,65,68])
y=np.array([155,150,180,135,156,168,178,160,132,145,139,152])
n=len(x)

#First graph
plt.figure(1)
plt.plot(x,y,'ro')
plt.grid(True)
plt.title('Datos ingresados')

#Calculations
sqx=np.zeros(n)
xy=np.zeros(n)
z=np.zeros(n)
e=np.zeros(n)
smy=0
smx=0
smsq=0
smxy=0

for i in range(n):
    sqx[i]=x[i]*x[i]
    xy[i]=x[i]*y[i]
    smy=smy+y[i]
    smx=smx+x[i]
    smsq=smsq+sqx[i]
    smxy=smxy+xy[i]

a=((n*smxy)-(smx*smy))/((n*smsq)-(smx*smx))
b=(smy-(a*smx))/n

prom=0
for i in range(n):
    z[i]=a*x[i]+b
    e[i]=abs(((y[i]-z[i])/y[i])*100)
    prom=prom+e[i]
prom=prom/n

#Output data 
print('\nTabla de datos\n')
print('x\ty\tx^2\txy\tycalc\terror\n')
for i in range (n):
    print(x[i],f'\t{y[i]:.2f}\t{sqx[i]:.2f}'
    f'\t{xy[i]:.2f}\t{z[i]:.2f}\t{e[i]:.2f}')

print('\nSumatoria de x: ',smx,
    '\nSumatoria de y: ',smy,
    '\nSumatoria de x^2: ',smsq,
    '\nSumatoria de xy: ',smxy)

print(f'\nEcuación de ajuste: {a:.4f} x + {b:.4f}')
print(f'\nPorcentaje de error: {prom:.2f}')
print('\n')

#Second graph
plt.figure(2)
plt.plot(x,y,'ro',x,z,'b')
plt.title('Ajuste lineal')
plt.grid(True)
plt.show()