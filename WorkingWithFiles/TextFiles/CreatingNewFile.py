filepath1=r"C:\Users\Hanshik\Desktop\Python\TextFormat.txt"

filepath2=r"C:\Users\Hanshik\Desktop\Python\TextData.txt"


f1=open(filepath1,'rt')
data=f1.read()
f2=open(filepath2,'r')
f2.write(data)
f2.write("\\n")

f1.close()
f2.close()