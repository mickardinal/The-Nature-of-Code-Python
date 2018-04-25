from mover import Mover
from liquid import Liquid

def setup():
    size(800, 200)
    randomSeed(1)
    
    global movers
    movers = [Mover(random(1, 4), random(width), 0) for i in range(100)]
    
    global liquid
    liquid = Liquid(0, height/2, width, height/2, 0.1)

def draw():
    background(255)
    liquid.display()

    for mover in movers:
        
        if mover.isInside(liquid):
            mover.drag(liquid)

        m = 0.1*mover.mass
        gravity = PVector(0, m)
        
        mover.applyForce(gravity)

        mover.update()
        mover.display()
        mover.checkEdges()