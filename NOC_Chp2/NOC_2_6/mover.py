class Mover(object):
    def __init__(self, m, x, y):
        self.location = PVector(x, y)
        self.velocity = PVector(1,0)
        self.acceleration = PVector(0,0)
        self.mass = m
    
    def applyForce(self, force):
        f = PVector.div(force, self.mass)
        self.acceleration.add(f)
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.location.add(self.velocity)
        self.acceleration.mult(0)
    
    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(0, 127)
        ellipse(self.location.x, self.location.y, self.mass*16, self.mass*16)
    
    def checkEdges(self):
        if self.location.x > width:
            self.location.x = width
            self.velocity.x *= -1
        elif self.location.x < 0:
            self.location.x = 0
            self.velocity.x *= -1

        if self.location.y > height:
            self.location.y = height
            self.velocity.y *= -1
    
    def isInside(self, liquid):
        if self.location.x > liquid.x and self.location.x < liquid.x + liquid.w and self.location.y > liquid.y and self.location.y < liquid.y + liquid.h:
            return True
        else:
            return False
        
    def drag(self, liquid):
        speed = self.velocity.mag()
        dragMagnitude = liquid.c * speed * speed
        
        drag = self.velocity.get()
        
        drag.mult(-1)
        drag.normalize()
        drag.mult(dragMagnitude)
        
        self.applyForce(drag)