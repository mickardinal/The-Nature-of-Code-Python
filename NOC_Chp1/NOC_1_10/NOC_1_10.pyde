from mover import Mover

def setup():
    size(800, 200)
    smooth()
    
    global mouse, dir
    
    global mover
    mover = Mover()
    
def draw():
    background(255)
    
    mover.update()
    mover.checkEdges()
    mover.display()