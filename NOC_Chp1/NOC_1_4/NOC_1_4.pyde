import math

class PVector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, PVector):
        self.y += PVector.y
        self.x += PVector.x
        
    def sub(self, PVector):
        self.y -= PVector.y
        self.x -= PVector.x
        
    def mult(self, n):
        self.y *= n
        self.x *= n
    
    def mag(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))
        
def setup():
    size(800, 200)
    smooth()

def draw():
    background(255)
    
    mouse = PVector(mouseX, mouseY)
    center = PVector(width/2, height/2)
    
    mouse.sub(center)
    
    m = mouse.mag()
    fill(0)
    rect(0, 0, m, 10)
    
    translate(width/2, height/2)
    line(0, 0, mouse.x, mouse.y)