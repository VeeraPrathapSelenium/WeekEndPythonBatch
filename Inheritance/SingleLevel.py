class School:

    def __init__(self,name,id):

        self.name=name
        self.id=id
        print(name)
        print(id)

    def addStudent(self):
        print("Student {0} is added to DB".format(self.name))

    def delStudent(self):
        print("Student Deleted")

class DPS_HYD(School):

    def __init__(self,name,id):

       super().__init__(name,id)
    def addStudentToMusic(self):
        print(self.name)
        print(self.id)


obj=DPS_HYD("Prathap",102)
obj.addStudentToMusic()