import pandas as pd
# First dictionary
employees_A = {
    "names": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "emid": [101, 102, 103, 104, 105],
    "salary": [50000, 60000, 55000, 70000, 65000]
}

# Second dictionary
employees_B = {
    "names": ["Olivia", "Liam", "Sophia", "Mason", "Isabella"],
    "emid": [201, 202, 203, 204, 205],
    "salary": [75000, 80000, 72000, 85000, 78000]
}
df1=pd.DataFrame(employees_A)
df2=pd.DataFrame(employees_B)
print(pd.concat([df1,df2]))