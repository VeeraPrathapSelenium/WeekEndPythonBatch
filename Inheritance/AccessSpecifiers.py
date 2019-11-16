class CheckAceess():

    def __init__(self,name,age):
        self._bankpassword="123456895"
        self.name=name
        self.age=age

class Userclass(CheckAceess):
    pass



obj=Userclass("prathap",29)
print(obj.name)
print(obj._bankpassword)

partobj=CheckAceess()


