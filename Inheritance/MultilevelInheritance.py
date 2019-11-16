class Parent:
    def __init__(self):
        print("Parent Class Constructor")
    def connectToDB(self):
        print("Connect to DB")

    def stimulateAPIService(self):
        print("Stimulate API")

class Child1(Parent):

    def __init__(self):
        super().__init__()
        print("Child1 Constructor")
    def getData(self):
        print("Get Document Data")

class SubChild(Child1):

    def __init__(self):
        super().__init__()
        print(" iam a constructor")


obj=SubChild()

obj.connectToDB()