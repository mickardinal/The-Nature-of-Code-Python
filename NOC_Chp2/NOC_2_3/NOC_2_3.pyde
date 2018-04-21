from mover import Mover

movers = []
moverCount = 100

def setup():
    size(800, 600)
    smooth()
    
    for x in range(moverCount):
        movers.append(Mover(random(0.1, 4), 0, 0))
    
def draw():
    background(255)
    
    wind = PVector(0.01, 0)
    
    for mover in movers:
        mover.applyForce(wind)
        gravity = PVector(0, mover.mass * 0.1)
        mover.applyForce(gravity)
        mover.update()
        mover.display()
        mover.checkEdges()