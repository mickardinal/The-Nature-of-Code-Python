class Attractor(object):
    def __init__(self):
        self.mass = 20
        self.location = PVector(width/2, height/2)
        global G
        G = 1
    
    def display(self):
        stroke(0)
        fill(175, 200)
        ellipse(self.location.x, self.location.y, self.mass*2, self.mass*2)
    
    def attract(self, m):
        force = PVector.sub(self.location, m.location)
        distance = force.mag()
        distance = constrain(distance, 5, 25)
        force.normalize()
        strength = (G * self.mass * m.mass) / float(distance * distance)
        
        force.mult(strength)
        return force