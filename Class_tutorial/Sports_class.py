import datetime
class CricketPlayer:
    def __init__(self,fname,lname,birthyear,team):
        self.first_name = fname
        self.last_name = lname
        self.birthyear = birthyear
        self.team = team
        self.scores= []

    def get_age(self):
        now= datetime.datetime.now()
        return now.year - self.birthyear

    def add_score(self,score):
        self.scores.append(score)

    def get_avgscore(self):
        return sum(self.scores)/len(self.scores)

    def __lt__(self, other):
        my_score= self.get_avgscore()
        other_score= other.get_avgscore()
        return my_score < other_score

    def __gt__(self, other):
        my_score= self.get_avgscore()
        other_score=other.get_avgscore()
        return my_score > other_score
    def __str__(self):
        return f'{self.first_name} {self.last_name} is the cricket player of {self.team}'


virat= CricketPlayer('virat','kohli',1988,'india')
virat.add_score(80)
virat.add_score(100)
virat.add_score(0)

david= CricketPlayer('david','warner',1985,'england')
david.add_score(70)
david.add_score(100)
david.add_score(0)

print(david)


