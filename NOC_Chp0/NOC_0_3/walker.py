class Walker(object):
    def __init__(self):
        self.x = width/2
        self.y = height/2
    
    def display(self):
        stroke(0)
        point(self.x, self.y)
        
    def step(self):
        r = random(0, 1)
        if r< 0.4:
            self.x += 1
        elif r < 0.6:
            self.x -= 1
        elif r < 0.8:
            self.y += 1
        else:
            self.y -= 1
        