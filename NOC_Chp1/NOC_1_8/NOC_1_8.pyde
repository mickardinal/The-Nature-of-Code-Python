from mover import Mover

def setup():
    size(800, 200)
    smooth()
    
    global mover
    mover = Mover()
    
def draw():
    background(255)
    
    mover.update()
    mover.checkEdges()
    mover.display()