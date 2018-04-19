class PVector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, PVector):
        self.y += PVector.y
        self.x += PVector.x
        
def setup():
    size(200, 200)
    smooth()
    global location, velocity
    location = PVector(100, 100)
    velocity = PVector(2.5, 5)

def draw():
    background(255)
    
    location.add(velocity)
    
    if location.x > width or location.x < 0:
        velocity.x = velocity.x * (-1)
    
    if location.y > width or location.y < 0:
        velocity.y = velocity.y * (-1)
    
    stroke(0)
    fill(175)
    ellipse(location.x, location.y, 16, 16)
    
    