class Walker(object):
    def __init__(self):
        self.x = width/2
        self.y = height/2
    
    def display(self):
        stroke(0)
        point(self.x, self.y)
        
    def step(self):
        # self.x += int(random(3)-1)
        # self.y += int(random(3)-1)
        
        self.x += random(-1, 1)
        self.y += random(-1, 1)
        