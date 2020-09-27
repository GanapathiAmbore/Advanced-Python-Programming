#Inheritance with Method
class Company:

    def company(self,name):
        print("I am company:",name)


class Brand(Company):

    def brand(self,brand):
        print("I am Brand:",brand)


class Product(Brand):
    def product(self,product):
        print("I am Product:",product)

prod_obj=Product()
prod_obj.product('Watch')
prod_obj.company('Titan')
prod_obj.brand('Titan')

