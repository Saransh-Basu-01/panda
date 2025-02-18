import numpy as np
a=np.array([30,40,50,60,10])
b=np.array([30,40,50,60,10])
print(a+b) 
print(np.add(a,b))
print(a-b)
print(np.subtract(a,b))

print(a/b)
print(np.divide(a,b))

print(np.multiply(a,b))
print(a*b)

a1=np.array([2,3,4,5])
b1=np.array([2])
print(np.power(a1,b1))

arr=np.array([4,9,25])
print(np.sqrt(arr))