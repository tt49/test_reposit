import random
class Human:
    def __init__(self):
        self.life= True
        self.progress=1
        self.rad = 0
    def sleep(self):
        print("GO SLEEP")
        self.rad+=1
    def study(self):
        print("GO STUDY")
        self.progress+=1
        self.rad-=0.5
    def chill(self):
        self.rad+=1
        self.progress-=0.5
    def check(self):
        if(self.progress<=0):
            print("DEGROD DIE")
            self.life = False
        elif (self.rad<=0):
            print("DEPRESS DIE")
            self.life = False
    def dayover(self):
        print("Your happiness level is {0}\n Your progess level is {1}".format(self.rad, self.progress))
    def simulate(self):
        rnd=random.randint(1,3)
        if (rnd==1):
            self.study()
        elif(rnd==2):
            self.chill()
        else:
            self.chill()
        self.check()
        self.dayover()

for i in range(10):

    Human().simulate()
    if(Human().life==False):
        break