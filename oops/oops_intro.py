#OOPS:Object Oriented Programming System
#Class
#Object
#attribute
#method
#class---->9th
#students------->20
#students name,age,rollnumber,section,medium
#class Movies
#telugu movies
#hindi movies
#movie------->director,musicdirector,producer,
#Example:1
'''class Student:
    def __init__(self,first_name,age,rollnumber,section,last_name):
        print("passed parameters--->",first_name,age,rollnumber,section,last_name)
        self.name=first_name
        self.age=age
        self.hallticketnumber=rollnumber
        self.section=section
        self.lastname=last_name
stu_obj=Student('Ganapathi',12,12,'A','Ambore')
stu_obj1=Student('Gopi',12,12,'C','Sunder')
print(stu_obj.name)
print(stu_obj.lastname)
print(stu_obj.hallticketnumber)
print(stu_obj1.name)
print(stu_obj1.section)'''
#Example2:
class Movie:
    def __init__(self,name,director,producer,release):
        self.name=name
        self.director=director
        self.producer=producer
        self.release_date=release

    def movies_info(self,budget):
        print("Moviebudget:", budget)
        return "Name:"+self.name+'\n'+"Director:"+self.director

movie_obj=Movie('BB1','SSR','SYG','2017')
movie_obj1=Movie('BB2','SSR','SYG','2017')
movie_obj2=Movie('BB3','SSR','SYG','2017')
print(movie_obj.movies_info("10M"))


