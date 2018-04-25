angle = 0
aVelocity = 0
aAcceleration = 0.001

def setup():
    size(200, 200)
    
def draw():
    global angle, aVelocity, aAcceleration
    
    background(255)
    
    fill(175)
    stroke(0)
    rectMode(CENTER)
    translate(width/2, height/2)
    rotate(angle)
    line(-50, 0, 50, 0)
    ellipse(50, 0, 8, 8)
    ellipse(-50, 0, 8, 8)
    
    aVelocity += aAcceleration
    angle += aVelocity