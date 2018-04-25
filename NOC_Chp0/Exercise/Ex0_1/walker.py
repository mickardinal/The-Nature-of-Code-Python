class Walker(object):
    def __init__(self):
        self.x = width/2
        self.y = height/2
    
    def display(self):
        stroke(0)
        point(self.x, self.y)
        
    def step(self):
        prop = random(0, 1)
        if prop < 0.9:
            self.x += random(-1, 1)
            self.y += random(-1, 1)
        elif prop >= 0.9:
            self.x += random(0, 1)
            self.y += random(0, 1)