import pandas as pd
data={"name":["john","peter","lisa"],
      "age":[25,30,12],
      "salary":[3000,4000,50000]
     }
df=pd.DataFrame(data)
print(df)