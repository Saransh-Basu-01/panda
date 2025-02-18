import pandas as pd
dict={
    "keys":["k1","k2","k1","k2"],
    "names":["john","saransh","anshu","samri"],
    "houses":["green","blue","red","yellow"],
    "grades":["3rd","1st","2nd","4th"]}
df=pd.DataFrame(dict)
print(df)
print(df.pivot(index="keys",columns="names",values=["houses","grades"]))