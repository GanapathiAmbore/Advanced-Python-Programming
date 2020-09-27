class A:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print("I am init A","name is:",name,"Age is:",age)


class B(A):
    def __init__(self):
        print("I am init B")



class C():
    def __init__(self):
        super().__init__()
        print("I am init C")


obj = B
print(obj)
