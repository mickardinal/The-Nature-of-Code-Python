from mover import Mover

movers = []
moverCount = 200

def setup():

    size(800, 600)
    smooth()
    
    for x in range(moverCount):
        movers.append(Mover())
    
def draw():
    background(255, 204, 0)
    
    for mover in movers:
        line(mover.location.x, mover.location.y, width/2, height/2)
        stroke(255, 255, 255, 0.1)
        fill(255, 255, 255, 0.1)
        mover.update()
        mover.display()
        # mover.checkEdges()