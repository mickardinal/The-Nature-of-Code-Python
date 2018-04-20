class Mover(object):
    def __init__(self):
        self.location = PVector(random(width), random(height))
        self.velocity = PVector(random(-2, 2), random(-2, 2))
        self.acceleration = PVector.random2D()
        self.acceleration.mult(random(2))
        global topspeed
        topspeed = 10
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(topspeed)
        self.location.add(self.velocity)
    
    def display(self):
        stroke(0)
        fill(175)
        ellipse(self.location.x, self.location.y, 16, 16)
        
    def checkEdges(self):
        if self.location.x > width:
            self.location.x = 0
        elif self.location.x < 0:
            self.location.x = width
            
        if self.location.y > height:
            self.location.y = 0
        elif self.location.y < 0:
            self.location.y = height
        