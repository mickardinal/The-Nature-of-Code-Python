class PVector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def sub(self, PVector):
        self.y -= PVector.y
        self.x -= PVector.x
        
def setup():
    size(200, 200)
    
def draw():
    background(255)
    mouse = PVector(mouseX, mouseY)
    center = PVector(width/2, height/2)

    mouse.sub(center)
    
    translate(width/2, height/2)
    line(0, 0, mouse.x, mouse.y)