import  pandas as pd

import  numpy as np

data=pd.read_excel(r"C:\Users\Hanshik\Desktop\Testadata.xlsx",sheet_name='Data')

mydata=data.where(data['Gender']=='Male')

#print(mydata)

#dataframe[datafrme["Key"]!='value']

print(data[data['Gender']!='Female'])



