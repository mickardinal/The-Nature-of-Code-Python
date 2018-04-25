from attractor import Attractor
from mover import Mover

def setup():
    size(640, 360)

    global m
    m =  Mover(1, 400, 50)
    global a
    a = Attractor()
    
def draw():
    background(255)
    
    f = a.attract(m)
    m.applyForce(f)
    
    a.display()
    
    m.update()
    m.display()
    