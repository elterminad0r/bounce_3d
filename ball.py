def apply_to(l):
    def to_all(func):
        def f(*args, **kwargs):
            for i in list(l):
                func(i, *args, **kwargs)
        return f
    return to_all

class Ball(object):
    SPEED = 3
    MINR = 15
    MAXR = 20
    BOXW = 400
    inst = []

    def __init__(self):
        self.loc = PVector(*(random(self.BOXW) for _ in range(3)))
        self.vel = PVector.random3D().mult(
            random(self.SPEED * 0.5, self.SPEED))
        self.inst.append(self)
        self.r = random(self.MINR, self.MAXR)
        self.c = random(255)

    @staticmethod
    @apply_to(inst)
    def update(self):
        self.loc = self.loc.add(self.vel)
        for o in "xyz":
            v = self.loc.__getattribute__(o)
            vv = self.vel.__getattribute__(o)
            if v - self.r < 0 or v + self.r > self.BOXW:
                self.vel.__setattr__(o, -vv)

    @staticmethod
    @apply_to(inst)
    def draw(self):
        pushMatrix()
        translate(self.loc.x, self.loc.y, self.loc.z)
        fill(self.c, 255, 255)
        sphere(self.r)
        popMatrix()
