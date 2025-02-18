import numpy as np
arr=np.array([10,2,3,4,1,0])
fa=arr%2==0
new=arr[fa]
print(new)
s=np.where(arr==10)
print(s)
print(np.sort(arr))
s=np.where(arr==10)
print(s)
