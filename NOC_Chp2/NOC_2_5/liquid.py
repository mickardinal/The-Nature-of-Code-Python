class Liquid(object):
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
    
    def display(self):
        noStroke()
        fill(175)
        rect(self.x, self.y, self.w, self.h)