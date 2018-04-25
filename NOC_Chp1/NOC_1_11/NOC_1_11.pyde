from mover import Mover

movers = []
moverCount = 200

def setup():

    size(800, 600)
    smooth()
    
    for x in range(moverCount):
        movers.append(Mover())
    
def draw():
    background(255)
    
    for mover in movers:
        
        mover.update()
        mover.display()
        # mover.checkEdges()