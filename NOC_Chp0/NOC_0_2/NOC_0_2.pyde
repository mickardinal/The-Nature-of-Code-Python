def setup():
    size(640, 240)
    
    global randomCounts
    randomCounts = [0] * 20

def draw():
    background(255)
    stroke(0)
    fill(127)
    
    index = int(random(0, len(randomCounts)))
    randomCounts[index] += 1
    
    w = width/len(randomCounts)
    
    for x, k in enumerate(randomCounts):
        rect(x*w, height-k, w-1, k) 
