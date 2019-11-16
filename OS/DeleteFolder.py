import os
import datetime

# today_date=datetime.datetime.now().strftime("%x").replace("/","-")
#
# path=r"C:\Users\Hanshik\Desktop\Python\Results\{0}".format(today_date)
# os.removedirs(path)
src=r"C:\Users\Hanshik\Desktop\Python\New folder"
dest=r"C:\Users\Hanshik\Desktop\Python\Prathap"
os.rename(src,dest)