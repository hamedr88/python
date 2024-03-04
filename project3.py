class moviefather:
    pass

class film(moviefather):
    def __init__ (self,name,cargardan,tahey_conande):
        self.name=name
        self.cargardan=cargardan
        self.tahey_conande=tahey_conande
    def Print(self):
        print("nam film :%s" % self.name)
        print("nam cargardan :%s " % self.cargardan)
        print("nam taheye conande :%s" % self.tahey_conande)
        print("%s is a film" % self.name)
class mostanad(moviefather):
    pass

class film_amozeshe(film):
    def __init__ (self,name,cargardan,tahey_conande,ostad):
        film.__init__(self,name,cargardan,tahey_conande)
        self.ostad=ostad
    def Print(self):
        print("nam film :%s" % self.name)
        print("nam cargardan :%s " % self.cargardan)
        print("nam taheye conande :%s" % self.tahey_conande)
        print("nam ostad :%s" % self.ostad)
        print("%s is a film_amozeshe" % self.name)

class film_senamaye(film):
    pass
#ostad man akharaye projeye 3 ro ce __main__ dare nemefahmam lotfan tozeh dahed.