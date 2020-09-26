class Team:
    def __init__(self,team_name,player_name,player_type,centures,highscore):
        self.TeamName=team_name
        self.PlayerName=player_name
        self.PlayerType=player_type
        self.Centures=centures
        self.HighScore=highscore

class IPL(Team):
    print("I am derived from Team class")


team_obj=Team('India','Rohith','Batsman','40','262')
team_obj1=Team('Austrailia','Warner','Batsman','30','160')
team_obj2=Team('SouthAfrica','ABDeviliars','Batsman','35','200')
print(team_obj.TeamName)
ipl_obj=Team('MI','Rohith','Batsman','40','262')
print(ipl_obj.TeamName)
print(dir(ipl_obj))

name="Python"
print(name.__init__())
print(name.__str__())
print(name.__dir__())
name.__delattr__()