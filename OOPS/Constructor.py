class MyConstructor:

    def __init__(self):

        print("Here i am a zero argument constructor")
        return None

    def __mycons__(self,a,b):
        print("Parameterized constructor")



    def add(self):
        print("Add method")
    def sub(self):
        print("sub method")


obj=MyConstructor()
obj.__mycons__(10,20)

