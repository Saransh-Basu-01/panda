import pandas as pd
data={"months":["january","february","march","april"]}
a=pd.DataFrame(data)
print(a)
def extract(value):
    return value[0:3]
a["short_months"]=a["months"].map(extract)
print(a)