import numpy as np
import matplotlib.pyplot as plt

#Ingreso de datos
x=np.array([-3,-1,1,3,5,7])
y=np.array([14,4,2,8,22,44])
n=len(x)

#grafica inicial
plt.figure(1)
plt.plot(x,y,'ro')
plt.grid(True)
plt.title('Datos')

#Calculos
sqx=np.zeros(n); xfour=np.zeros(n); 
xthree=np.zeros(n); doublexy=np.zeros(n)
xy=np.zeros(n); z=np.zeros(n); e=np.zeros(n)
smy=0; smx=0; smsq=0; smxy=0; smfour=0 
smthree=0; smdouble=0

for i in range(n):
    sqx[i]=x[i]*x[i]
    xy[i]=x[i]*y[i]
    doublexy[i]=x[i]*x[i]*y[i]
    xthree[i]=x[i]*x[i]*x[i]
    xfour[i]=x[i]*x[i]*x[i]*x[i]
    smy=smy+y[i]
    smx=smx+x[i]
    smsq=smsq+sqx[i]
    smxy=smxy+xy[i]
    smfour=smfour+xfour[i]
    smthree=smthree+xthree[i]
    smdouble=smdouble+doublexy[i]


a=np.array([[smfour,smthree,smsq],
            [smthree,smsq,smx],
            [smsq,smx,n]])
b=np.array([smdouble,smxy,smy])
solution=np.linalg.solve(a,b)

prom=0
for i in range(n):
    z[i]=solution[0]*x[i]*x[i]+solution[1]*x[i]+solution[2]
    e[i]=abs(((y[i]-z[i])/y[i])*100)
    if e[i]==float('inf'):
        prom=prom
    else: 
        prom=prom+e[i]       
prom=prom/n

#Impresion de datos obtenidos
print('\nDAjuste de datos\n')
print('x\ty\tx^2\tx^3\tx^4\t\txy\tx^2y')
for i in range (n):
    print(x[i],f'\t{y[i]:.0f}\t{sqx[i]:.0f}\t{xthree[i]:.0f}'
    f'\t{xfour[i]:.0f}\t',end=' ')
    if i<=7:
        print(f'\t{xy[i]:.0f}\t{doublexy[i]:.1f}')
    else:
       print(f'{xy[i]:.0f}\t{doublexy[i]:.1f}') 


print('\nSumatoria de x: ',smx,
    '\nSumatoria de y: ',smy,
    '\nSumatoria de x^2: ',smsq,
    '\nSumatoria de x^3: ',smthree,
    '\nSumatoria de x^4: ',smfour,
    '\nSumatoria de xy: ',smxy,
    '\nSumatoria de x^2y: ',smdouble)

print('\nx\ty\ty calc\teror')
for i in range (n):
    print(x[i],f'\t{y[i]:.1f}\t{z[i]:.2f}\t{e[i]:.2f}')

print(f'\nEcuación de ajuste: {solution[0]:.4f} x^2 + {solution[1]:.4f} x + {solution[2]:.4f}')
print(f'\nPorcentaje de error: {prom:.2f}')
print('\n')

#segunda grafica
plt.figure(2)
plt.plot(x,y,'ro',x,z,'b')
plt.title('Ajuste no lineal')
plt.grid(True)
plt.show()
