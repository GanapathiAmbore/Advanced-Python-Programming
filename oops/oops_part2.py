'''class Programming:
    def __init__(self,name,year,version,used):
        #Attriutes
        self.Name=name
        self.Year=year
        self.Version=version
        self.Used=used
    #method
    def usedfor(self,year):
        print(self.Name+' is Used for'+' '+self.Used+' Since '+year)
pro_obj=Programming("Python","1991","3.8",'AI')
pro_obj.usedfor('2016')'''

class News:
    def __init__(self,name,language,date,editor,no_of_pages):
        self.Name=name
        self.Language=language
        self.Date=date
        self.Editor=editor
        self.No_of_Pages=no_of_pages

news_obj=News('Eenadu','Telugu','23-09-2020','RamojiRao','12')
news_obj1=News('Hindu','Eng','23-09-2020','TestUser','20')

print(news_obj1.Name+' has '+news_obj1.No_of_Pages+' pages ')