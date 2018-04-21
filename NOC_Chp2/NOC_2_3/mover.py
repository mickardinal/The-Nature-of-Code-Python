class Mover(object):
    def __init__(self, mass, x, y):
        self.mass = mass
        self.location = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)
        
    def applyForce(self, force):
        f = PVector.div(force, self.mass)
        self.acceleration.add(f)
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.location.add(self.velocity)
        self.acceleration.mult(0)
    
    def display(self):
        stroke(0)
        fill(175)
        ellipse(self.location.x, self.location.y, self.mass, self.mass)
        
    def checkEdges(self):
        if (self.location.x > width):
            self.location.x = width
            self.velocity.x *= -1
        elif (self.location.x < 0):
            self.location.x = 0
            self.velocity.x *= -1

        if (self.location.y > height):
            self.location.y = height
            self.velocity.y *= -1
        