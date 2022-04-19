# class student(object):
#     def __init__(self,name,number):
#          self.name = name
#          self.number = number
#     def setName(self,name):
#         self.name = name
#     def getName(self):
#         return self.name
#     def setNumber(self,number):
#         self.number = number
#     def getNumber(self):
#         return self.number
#     def getInfo(self):
#         return "neme : %s \nnumber : %d\n"%(self.name,self.number0)
# st1 = student("siravit","thawornsap",21)
# st1.setName("beem")
# st1.setNumber(20)
# print(st1.getName(),st1.getNumber())

# em = []
# em.append(student("beem",21))
# em.append(student("nut",22))
# print(em[0].getName())
# print(em[0].getNumber())
# print(em[1].getName())
# print(em[1].getNumber())

# st=[]
# for i in range(0,5):
#     input_name = str(input("Enter name : "))
#     input_number = int(input("Enter number : "))
#     st.append(student(input_name,input_number))
# for i in range(0,5):
#     print(st[i].getInfo())




# class privait():
#     def __init__(self,):
#        self.__pv = 0 
#     def get_pv(self):
#         return self.__pv
       
# pt1 = privait()
# pt1.__pv = 10
# print(pt1.get_pv())




# class people() :
#     def __init__(self,fname,lname,id):
#         self.fname = fname
#         self.lname = lname
#         self.id = id
#     def eat(self):
#         return "eat"
#     def sleep(self):
#         return "sleep"
#     def get_info(self):
#         return str(self.fname) + str(self.lname) + str(self.id)
# class student(people):
#     def __init__(self,fname,lname,id,number,_class,school):
#         super().__init__(fname,lname,id)
#         self.number = number
#         self._class = _class
#         self.school = school
#     def study(self):
#         return "study"


# student1 = student("siravit","thawornsap",12345678,21,"m5","thk")
# print(student1)


print("hello world")