import  pandas as pd

import  numpy as np

csvData=pd.read_csv(r"C:\Users\Hanshik\Downloads\MSFT.csv")

#print(csvData)

#print(csvData.shape)

#print(csvData.describe())

#print(csvData.head(5))

#print(csvData.loc[5])

#print(csvData.iloc[1:10])

data=csvData[(csvData["Volume"]==55523100)]


print(csvData[(csvData.Volume==55523100)& (csvData.Open==78.0000)])
#print(data)


