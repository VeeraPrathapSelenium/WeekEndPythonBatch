class School:

    __stream="CBSE"
    def __init__(std,name,id,classname):

        std.name=name
        std.id=id
        std.classname=classname

    def getStudentName(self):

        return self.name
    def getStudentID(self):
        return self.id

    def getStudentClass(self):
        return self.classname




obj=School("Prathap",101,"Xth Class")
print(obj.getStudentName())
print(obj.stream)


