import os

#print(os.name)

print(os.getcwd())

# Create a new folder

path=r"C:\Users\Hanshik\Desktop\Python\MyFolder"

#os.mkdir(path)

#Check for folder existance

status=os.path.exists(path)

if not status:
    os.mkdir(path)
else:
    print("Folder is already exist")
