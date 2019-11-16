class Parent1:

    def m1(self):
        print("from parent 1")

class Parent2:

    def m1(self):
        print("from parent 2")


class child(Parent2,Parent1):

    def m(self):
        print("from child class")


obj=child()
obj.m1()
