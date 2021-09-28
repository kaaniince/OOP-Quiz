# #class

# class Person:
#     # class attributes
#     adress = 'no information'

#     # constructor (yapıcı metod)
#     def __init__(self,name,year):
#         # object attributes
#         self.name = name 
#         self.year = year
        
        
#     #instance methods
#     def intro(self):
#         print("Hello " + self.name)
#     def calculateAge(self):
#         return 2021 - self.year

# #object (instance)

# p1 = Person("Kaan", 2000) #obje
# p2 = Person("Yağmur", 1999)

# #updating

# #p1.name="Ömer"

# #accessing object attributes
# #print(f'p1:name:{p1.name} year:{p1.year} adress:{p1.adress}')

# p1.intro()
# p1.calculateAge()

# print(f'p1:yaşım:{p1.calculateAge()}')


# class Circle:
    
#     pi = 3.14
    
#     def __init__(self,yaricap=1):
#         self.yaricap = yaricap
    
#     def cevre_hesapla(self):
#         return 2 * self.pi + self.yaricap
    
#     def alan_hesapla(self):
#         return self.pi*(self.yaricap**2)
    
# c1 = Circle()
# c2 = Circle(5)

# print(f'c1:alan = {c1.alan_hesapla()}')

# print(f'c2:alan = {c2.alan_hesapla()}')


#Inheritance(Kalıtım): Miras alma

# class Person:
#     def __init__(self, fname,lname) :
#         self.firstName = fname
#         self.lastName = lname
#         print("Person Created")
#     def who_am_i(self):
#         print("I am a person")
#     def eat(self):
#         print("I am a eating")
        
# class Student(Person):
#     def __init__(self,fname,lname,number):
#         Person.__init__(self,fname,lname) #Person daki yazıyı almış oldu.
#         self.studentNumber = number
#         print("Student Created")
#     #override satır 87 de var
#     def who_am_i(self):
#         print("I am a student")
#     def sayHello(self):
#         print("I am a Student")
        
# class Teacher(Person):
#     def __init__(self, fname, lname,branch):
#         super().__init__(fname, lname) # student ile yapılan işlemin aynısıdır.
#         self.branch = branch
#     def who_am_i(self):
#         print(f'I am a {self.branch} teacher')
    
# p1 = Person("ali","korn")
# s1 = Student("yilmaz","bö",3243)
# t1 = Teacher("Ceyda","İnce","Sınıf Öğretmeni")

# t1.who_am_i()

# print(p1.firstName +' ' +p1.lastName)

# print(s1.firstName +' ' +s1.lastName)

# p1.eat()
# s1.who_am_i() # aynı isimli metod temeldeki metodu ezer.

# class Movie():
    
#     def __init__(self,title,director,duration):
#          self.title =title
#          self.director = director
#          self.duration = duration
#     def __str__(self) -> str:
#         return  f"{self.title} by {self.director}"  
     
#     def __len__(self):
#         return self.duration    
    
#     def __del__(self):
#         print("Film silindi")
         
# m = Movie("Aşk","Burak",120)
    
# print(len(m))
    
# del m
    
