
class Team:
    '''Instance Variables'''
    def __init__(self,name,matches,loss,won):
        self.name=name
        self.matches=matches
        self.loss=loss
        self.won=won

    '''Instance Method'''

    @property
    def average(self):
        print ("Averag:",self.won+self.loss/2)

    def percentage(self):
        print("Winning ratio of {} :".format(self.name),self.won/self.matches*100)


    def lossing(self):
        print("Lossing ration {} :".format(self.name),self.loss/self.matches*100)


class  IPLTeam:
    '''Instance Variables'''
    def __init__(self,name,matches,loss,won):
        self.name=name
        self.matches=matches
        self.loss=loss
        self.won=won

    '''Instance Method'''

    def average(self):
        print(self.won+self.loss/2)


team_obj=Team("India",120,80,40)
team_obj=Team('Pakisthan',200,78,122)
print("Team Name:",team_obj.name)#Accesing Name Attribute
print("No of Matches:",team_obj.matches)#Accesing matches Attribute
print("No of Wins:",team_obj.won)#Accesing Attribute
print("No of Loss:",team_obj.loss)#Accesing Attribute
team_obj.percentage()#Accesing percentage Method
team_obj.lossing()#Accesing loosing Method
print("Average is attribute now:",team_obj.average)#Accesing average Method



