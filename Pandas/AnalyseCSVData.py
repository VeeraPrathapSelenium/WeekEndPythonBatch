import  pandas as pd

import  numpy as np

csvData=pd.read_csv(r"C:\Users\Hanshik\Downloads\Table_14.1_2016.csv")

#print(csvData.head(5))

data=(csvData.Cases_Reported>=300)&(csvData.Cases_Reported<=500)

print(csvData[data])


