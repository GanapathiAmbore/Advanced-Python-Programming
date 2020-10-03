'''x=10+20
print(x)
y="ganapathi"+" python"
print(y)

a="School"
b=20
print(b*10)
print(a*2)'''

class Book:
    def __init__(self,name,number_of_pages):
        self.name=name
        self.numberofpages=number_of_pages

    def bookinfo(self):
        print("Book",self.name,"has",self.numberofpages,"pages")

    def __add__(self, other):
        print(self.numberofpages+other.numberofpages)


name=["Python","DS"]
number_of_pages=[120,200]
book_obj=Book(name[0],number_of_pages[0])
book_obj1=Book(name[1],number_of_pages[1])
book_obj.bookinfo()
book_obj1.bookinfo()
book_obj+book_obj1
