class Walker(object):
    def __init__(self):
        self.x = width/2
        self.y = height/2
    
    def display(self):
        stroke(0)
        point(self.x, self.y)
        
    def step(self):
        r = random(0, 1)
        if r < 0.5:
            xdir = mouseX - self.x
            ydir = mouseY - self.y
            if xdir != 0:
                xdir /= abs(xdir)
            if ydir != 0:
                ydir /= abs(ydir)
            self.x += xdir
            self.y += ydir
        else:
            xdir = random(-2, 2)
            ydir = random(-2, 2)
            println(xdir)
            self.x += xdir
            self.y += ydir
        
        self.x = constrain(self.x, 0, width - 1)
        self.y = constrain(self.y, 0, width - 1)