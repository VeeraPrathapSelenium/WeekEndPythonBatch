import  datetime

import os

print(datetime.datetime.now().strftime("%x").replace("/","-"))

today_date=datetime.datetime.now().strftime("%x").replace("/","-")

path=r"C:\Users\Hanshik\Desktop\Python\Results\{0}".format(today_date)

if not os.path.exists(path):
    print("No Folder is exist with Todays Date, Creating a new Folder")
    os.makedirs(path,exist_ok=True)
else:
    print("Folder already exist")