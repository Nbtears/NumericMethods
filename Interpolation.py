#This program use the Lagrange method for interpolation
##Switch data of x, y and z values as need it

import numpy as np
import matplotlib.pyplot as plt

#Input data
x=np.array([150.,160.,170.,180.]) #data1
y=np.array([35.5,37.8,43.6,45.7]) #data2
z=162. #data we are looking for with interpolation
n= len(x)

print('Data 1\tData 2')
for i in range (n):
    print(' ',x[i],'\t',y[i])

#Calculations
poly=0
print('\ny = ', end=' ')
for i in range (n):
    num=1
    den=1
    print(y[i],end='[')
    for j in range(n):
        if (i!=j):
            print('(',z,'-',x[j],end=')')
            num=num*(z-x[j])
    print(']/',end='[')        
    for k in range(n):
        if (i!=k):
            print('(',x[i],'-',x[k],end=')')
            den=den*(x[i]-x[k])
    if (i!=n-1):
        print('] +')

    lg=(num/den)*y[i]
    poly=poly+lg

#Output data
print('\n\nThe result according from data 1 is',z,'=',poly)
print('\n')