class School:
    place="Hyderabad"
    location="KPHB"
    def addStudent(self):

        print("Add Student to the school")

    def delStudent(self):
        print("deflete student from the school")


obj=School()

obj.addStudent()
obj.delStudent()
print(obj.place)
print(obj.location)


