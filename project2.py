class person:
    def __init__(self,nam,shomare,addres):
        self.nam=nam
        self.shomare=shomare
        self.addres=addres
    def set_name(self):
        self.nam=input("name khod ra vred coned :")
    def set_addres(self):
        self.addres=input("addres ra vared coned :")
    def set_shomare(self):
        self.shomare=input("shomare ra vared coned :")
    def get_name(self):
         print("esm shoma %s ast." % self.nam)
    def get_addres(self):
         print("addres %s ast." % self.addres)
    def get_shomare(self):
         print("shomare ye shoma %s ast." % self.shomare)


class Student(person):
    def __init__(self,nam,shomare,addres,status):
        person.__init__(self,nam,shomare,addres)
        self.status=status
    def set_status(self):
        x=input("status ravared coned :")
        if (x=="freshman"):
            x=self.status
        elif(x=="sophomore"):
             x=self.status
        elif(x=="junior"):
             x=self.status
        elif(x=="senior"):
             x=self.status
        else:
            print("dobare vared coned :")
    def get_status(self):
        print("status shoma %s ast." % self.status)
student=Student()
student.set_name()
student.set_addres()
student.set_shomare()
student.set_status()
student.get_name
student.get_addres()
student.get_shomare()
student.get_status()


#ostad khat 38 che moshcele dare?





class Employee(person):
        pass
