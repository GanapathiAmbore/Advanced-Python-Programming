#Type of variables in classes
#instance variable
#static or class variable
#User defind class
class Computer:
    Company="HP"#static or  class variable
    def __init__(self,RAM,CPU,Processor):
        self.ram=RAM#Instance variable
        self.cpu=CPU
        self.processor=Processor

    #Method (function it is inside the class)
    def graphiccard(self,graphic_card_size):
        print(self.ram+' '+self.cpu+'  '+self.processor+' '+"grapahic size for",graphic_card_size)

    @classmethod#decorator
    def name(cls):
        print("I am class method")

    @staticmethod
    def home(string):
        print(string)
        print(len(string))

comp_obj=Computer('16GB','INTEL','i7')
comp_obj1=Computer('8GB','INTEL','i5')

comp_obj1.graphiccard("2gb")
comp_obj.graphiccard("8gb")
Computer.name()
Computer.home("I am not a instance method nor a class method I am independent!")




