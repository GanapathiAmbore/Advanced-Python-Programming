
class Employee:
    name="Suresh"
    role="Developer"
    print(name,role)

class EmpSalary(Employee):
    '''I am EmpSalary'''
    salary='1000$'


print(EmpSalary.__dict__['salary'])
