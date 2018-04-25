from mover import Mover

def setup():
    size(640, 360)
    global movers
    movers = []
    for i in range(20):
        movers.append(Mover(random(1, 4), 0, 0))

def draw():
    background(255)

    for m in movers:
        wind = PVector(0.01, 0)
        gravity = PVector(0, 0.1*m.mass)
        
        c = 0.05
        normal_ = 1
        frictionMag = c*normal_
        
        friction = m.velocity.get()
        friction.mult(-1)
        friction.normalize()
        friction.mult(frictionMag)
        
        m.applyForce(wind)
        m.applyForce(gravity)
        m.applyForce(friction)

        m.update()
        m.display()
        m.checkEdges()