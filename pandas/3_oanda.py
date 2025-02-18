#how to merge dataframe in pandas
import pandas as pd
a={"names":["saransh","anshu","samri","prajwal"],
   "age":[20,20,19,21],
   "emid":[100,200,300,400]}
b={"salary":[10000000,10000000,1000000,1000000],
   "emid":[100,200,300,400]}
df1=pd.DataFrame(a)
df2=pd.DataFrame(b)
print(pd.merge(df1,df2,on="emid"))
