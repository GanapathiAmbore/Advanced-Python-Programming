'''#Parent class
class A:
    """To get the range of number"""

    def __init__(self,numbers):
        self.numbers =numbers
        for num in range(numbers):
            print(num)

#Child class
class B(A):
    """To get the even and odd numbers"""

    def __init__(self,numbers):
        print("I am in class B!!")




class C(A,B):

    def __init__(self):
        print("I am in class C")


#obj1 = A(21)
obj2 = B(21)


# obj3=C()
'''

class A:
    def featureA(self):
        print("I am init A")

class B(A):

    def featureB(self):
        print("I am init B")

class C(B):
    def featureC(self):
        print("I am init C")

#obj=A()
#obj.featureA()
#obj1=B()
#obj1.featureB()
#obj1.featureA()
obj2=C()
obj2.featureC()
obj2.featureB()
obj2.featureA()