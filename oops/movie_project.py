class Movie:
    def __init__(self, movie_name, director, music):
        self.name = movie_name
        self.director = director
        self.music = music

    def movie_info(self):
        print(self.name, self.director, self.music)

class Actor(Movie):

    def __init__(self,actor_name,movie_name,director,music,movies=None):#This are attributes of defined child class

        super().__init__(movie_name,director,music)#This are the attributes derived from parent class
        self.movies=movies
        self.actor_name=actor_name
        if self.movies is None:
            self.movies=[]
        else:
            self.movies=movies

    def add_movies(self,movies_list):
        if movies_list not in  self.movies:
            self.movie=self.movies.append(movies_list)
        print(movies_list)



actor_obj = Actor('AA','ALVP', 'TS', 'SST',['test','test1'])
actor_obj.add_movies(['asdf','asdf','asf'])
help(Actor)
print(isinstance(Actor,Actor))
#print(issubclass(Actor,Movie))


