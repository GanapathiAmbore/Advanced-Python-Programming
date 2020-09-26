class Employee:
    name="Suresh"
    role="Developer"
    #print(name,role)

class EmpSalary(Employee):
    salary='1000$'




emp_sal=EmpSalary()
print(emp_sal.salary,emp_sal.name,emp_sal.role)
