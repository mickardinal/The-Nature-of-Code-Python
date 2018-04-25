from mover import Mover

def setup():
    size(800, 200)
    global m
    m = Mover(1, width/2, height/2)
    
def draw():
    
    background(255)
    fill(175)
    stroke(0)
    
    m.update()
    m.display()
    m.checkEdges()
