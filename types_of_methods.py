class Movie:
    #Instance method
    def __init__(self,name,director,proucer):
        self.name=name
        self.director=director
        self.producer=proucer
    #Instance method
    def movie_info(self,budget):
        print("movie name:",self.name+"Director name:",self.director)
        print("Budget-------->",budget)
    #Class method
    @classmethod
    def industry(cls,movie):
        print("movie name is---->",movie)
        print("Its belogns to Tollywood!")

    #static method
    @staticmethod
    def student():
        print("I am not belongs any method!!")

movie_obj=Movie("BB2",'SSR','SYG')
movie_obj.student()#its method without argument
movie_obj.industry("ALVP")#its method without argument
movie_obj.movie_info(250)

'''#Inbuilt method
name = "Python"
print(type(name))
print(dir(name))
print(name.upper())  # its method without arguments
print(name.find("P"))  # its method need pass arguments
print(name.replace("n", "m"))  # its method need pass arguments'''
