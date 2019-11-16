lst=[1,2,23]

try:
    print(lst[28])


except:
    print("Exception is handled")# try writting the  controlling code here
else:
    print("No Exception arised in try block")

finally:
    print("I am execution 100% sucessfully irrespective of exceptions")