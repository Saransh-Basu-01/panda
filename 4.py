import numpy as np
a=np.array([[30,40],[60,10]])
b=np.array([[30,40],[60,10]])

print(np.concatenate([a,b],axis=1))
print(np.hstack([a,b])) #horizontal concatenation

print(np.vstack([a,b])) #vertical concatenation
print(np.concatenate([a,b],axis=0))