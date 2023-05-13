
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
        elif (self.rad<=0):
            print("DEPRESS DIE")
    def dayover(self):
        print("Your happiness level is {0}\n Your progess level is {1}".format(self.rad, self.progress))