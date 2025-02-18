import numpy as np
import statistics as stats
baked_food=[200,300,150,130,200,280,188,170]
a=np.array(baked_food)
print(np.mean(a))
print(np.sort(a))
print(np.median(a))
print(stats.mode(a))
print(np.std(a))