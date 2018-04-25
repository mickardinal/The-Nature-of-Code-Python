from walker import Walker

def setup():
    size(640, 360)
    background(255)
    global w
    w = Walker()
    
def draw():
    w.step()
    w.display()