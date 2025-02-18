#creation of dataframe using panda in python
import pandas as pd
from typing import List
#using list
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # Creating a DataFrame with appropriate column names
    df = pd.DataFrame(student_data, columns=["ID", "Marks"])
    return df

# Example Usage
data = [[1, 85], [2, 90], [3, 78]]  # Sample student data (ID, Marks)
df = createDataframe(data)
print(df)
#using dictionary
data={"name":["john","peter","lisa"],
      "age":[25,30,12],
      "salary":[3000,4000,50000]
     }
df=pd.DataFrame(data)
print(df)