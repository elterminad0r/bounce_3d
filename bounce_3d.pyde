from ball import Ball

def setup():
    size(800, 800, P3D)
    
    for _ in xrange(30):
        Ball()

def draw():
    background(0)
    colorMode(HSB, 255, 255, 255)
    lights()
    noStroke()
    pushMatrix()
    translate(400, 400)
    rotateY(QUARTER_PI)
    rotateZ(QUARTER_PI)
    pushMatrix()
    translate( *([-Ball.BOXW * 0.5] * 3))
    Ball.update()
    Ball.draw()
    popMatrix()
    fill(255, 50)
    stroke(0)
    box(Ball.BOXW)
    popMatrix()