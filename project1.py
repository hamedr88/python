class student:
    def __init__ (self,name_of_student,nomre_math_student,nomre_Science_student):        
        self.name_of_stunent=name_of_student
        self.nomre_math_student=nomre_math_student
        self.nomre_Science_student=nomre_Science_student
    def get_moadel(self):
        x=(self.nomre_math_student + self.nomre_Science_student)/2
        print(x)
    def get_moadel_hardo(self):
        y=(mohamad.nomre_math_student + ali.nomre_math_student + mohamad.nomre_Science_student + ali.nomre_Science_student)/4
        print(y)

mohamad=student("mohamad",17,19)
sadfas=0
ali=student("ali",15,20)

ali.get_moadel()
mohamad.get_moadel()
ali.get_moadel_hardo()

# Hamed rajabzadeh 2/24/2024 poroje_aval



