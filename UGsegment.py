import math

class segment:
    def __init__(self, target=(0,0), length=1.0, angle=10.0):
        self.target = target
        self.length = length
        self.angle  = angle
        self.find_vector_origin(target,length,angle)


    def find_vector_origin(self, target:tuple, length:float, angle:float):
        x2,y2 = target
        x1 = int(x2 - length * math.cos(angle))
        y1 = int(y2 - length * math.sin(angle))
        self.origin = (200, 200)
        self.origin = (x1,y1)

    def update(self,new_target:tuple):
        dx = new_target[0]-self.origin[0]
        dy = new_target[1]-self.origin[1]

        if(dx==0 and dy>=0):
            self.angle = math.pi/2
        elif(dx==0 and dy<0):
            self.angle = math.pi/2*3
        elif((dx>0 and dy>=0) or (dx>0 and dy<0)):
            self.angle = math.atan(dy/dx)
        else:
            self.angle = math.atan(dy/dx)+math.pi
        self.target = new_target
        self.find_vector_origin(self.target, self.length, self.angle)
