
class Employee:

    def __init__(self,name,role,salary,department):
        self.name=name
        self.role=role
        self.salary=salary
        self.department=department

    def company(self,company):#instance method
        print(self.name+' Belongs to:'+company)

    @classmethod
    def place(cls):
        print("I belongs to Class method!!")

    @staticmethod
    def home(*n):
        for i in n:
            print("I am  static method",i)

emp_obj=Employee('Jhon','Developer','599$','Software')
emp_obj.company("Google")
print(dir(emp_obj))
emp_obj.home([1,2,3,4,5])