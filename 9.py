import numpy as np
a=np.array([10,20,30,40,5])
b=np.array([100,200,30,40,400])
price=np.array(a)
quantity=np.array(b)
print(price,"\n",quantity)
c=np.cumprod([price,quantity],axis=0)
print(c)
print(np.sum(c[1])) #c[1].sum()

