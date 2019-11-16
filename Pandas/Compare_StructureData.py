import  pandas as pd

import numpy as nm

before_Prod=pd.read_csv(r"C:\Users\Hanshik\Desktop\Python\Before_Prod.csv")

after_Prod=pd.read_csv(r"C:\Users\Hanshik\Desktop\Python\After_Prod.csv")


after_Prod["Cases_Reported_Changed?"]=nm.where(before_Prod.Cases_Reported==after_Prod.Cases_Reported,"True","False")

print(after_Prod)