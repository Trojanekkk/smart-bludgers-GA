from random import randint

win_height = 400
win_width = 400

def setup():
  size(win_width, win_height)

class Population():
    def __init__ (self, n_bludgers):
        self.n_bludgers = n_bludgers
        self.bludgers = []
        
        for i in range(0,self.n_bludgers):
            self.bludgers.append(Bludger())
            
    def run (self):
        for i in range(0,self.n_bludgers):
            self.bludgers[i].fly()
            self.bludgers[i].display()

class Bludger():
    def __init__ (self):
        self.width = 10
        self.height = 10
        
        self.xpos = win_width / 2
        self.ypos = 0
        self.color = color(255)
        
        self.moves = []
        for i in range(0,3):
            self.moves.append(MoveVector(float(randint(-99,99)) / 100, float(randint(1,99)) / 100, randint(50,125)))
        
        self.move_n = 0    
        self.iter = 0
        
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
                    print(self.move_n)
            
    def display (self):
        rectMode(CENTER)
        fill(self.color)
        ellipse(self.xpos, self.ypos, self.width, self.height)
        
class MoveVector():
    def __init__ (self, xspeed, yspeed, length):
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.length = length

pop = Population(5)

def draw():
  background(255)
  pop.run()
