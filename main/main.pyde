from random import randint

win_height = 400
win_width = 400

def setup():
  size(win_width, win_height)

class Population():
    def __init__ (self, target, n_bludgers):
        self.n_bludgers = n_bludgers
        self.bludgers = []
        
        for i in range(0,self.n_bludgers):
            self.bludgers.append(Bludger(target))
            
    def run (self):
        for i in range(0,self.n_bludgers):
            if hasattr(self.bludgers[i], 'score'):
                continue
            self.bludgers[i].fly()
            self.bludgers[i].display()

class Bludger():
    def __init__ (self, target):
        self.width = 10
        self.height = 10
        self.xpos = win_width / 2
        self.ypos = 0
        self.color = color(255)
            
        self.iter = 0
        self.move_n = 0
        self.moves = []
        for i in range(0,3):
            self.moves.append(MoveVector(float(randint(-99,99)) / 100, float(randint(1,99)) / 100, randint(50,125)))
        
        self.target = target
        
    def fly (self):
        if (self.xpos < win_width and self.xpos > -1 and self.ypos < win_height and self.ypos > -1):
            if (self.iter < self.moves[self.move_n].length):
                self.xpos = self.xpos + self.moves[self.move_n].xspeed
                self.ypos = self.ypos + self.moves[self.move_n].yspeed
                self.iter += 1
            else:
                if (self.move_n < len(self.moves) -1):
                    self.move_n += 1
                    self.iter = 0
                else:
                    self.calculate_score()
                    
    def calculate_score (self):
        x_distance = self.xpos - self.target.xpos
        y_distance = self.ypos - self.target.ypos
        self.score = sqrt((x_distance ** 2 + y_distance ** 2))
        return self.score
            
    def display (self):
        rectMode(CENTER)
        fill(self.color)
        ellipse(self.xpos, self.ypos, self.width, self.height)
        
class MoveVector():
    def __init__ (self, xspeed, yspeed, length):
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.length = length
        
class Harry_Potter():
    def __init__ (self, xpos=win_width / 2, ypos=win_height - win_height / 20):
        self.xpos = xpos
        self.ypos = ypos
        
    def display (self):
        rectMode(CENTER)
        fill(color(174,0,1))
        rect(self.xpos, self.ypos, 10, 10)

hp = Harry_Potter()
pop = Population(hp, 5)

def draw():
    background(255)
    hp.display()
    pop.run()
