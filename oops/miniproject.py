class Voter:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eligible(self,dob,state):
        if self.age>=18:
            print("{} is Eligible for voting and his age is {} and DOB is {} and his from {}".format(self.name,self.age,dob,state))
        else:
            print("{} is Not Eligible for voting and his age is {} and DOB is {} and his from {}".format(self.name,self.age,dob,state))

    @classmethod
    def vclass(cls,word):
        print("I belongs to Class method!!")
        print("length of given word is:",len(word))

    @staticmethod
    def vstatic(number,filename):
        even_number=[]
        odd_number=[]
        for num in range(number):
            if num%2==0:
                even_number.append(num)
            else:
                odd_number.append(num)
        import pandas as pd
        df=pd.DataFrame([even_number])
        df.to_csv(filename+'.csv')
