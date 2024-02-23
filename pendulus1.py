from manim import *
import numpy as np

class PendulusGroup(VGroup):
    CONFIG={
        'time': 0,
    }
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time=self.CONFIG['time']
        self.derecha=True
        self.frequency=0.5
        self.color=BLUE
        self.put_dot()
        self.put_line()
        self[1].add_updater(self.update_pendulus)
    def put_dot(self):
        self.dot=Dot(color=self.color).move_to(self.get_center())
        self.add(self.dot)
    def put_line(self):
        self.line=Line(self.get_center(), self.get_center()+DOWN*2)
        self.dot.add_updater(lambda d: d.move_to(self.line.get_end()))
        self.add(self.line)
    def update_pendulus(self, mob, dt):
        direccion=1
        if self.derecha: 
            angle_range=np.radians([3, 177])
        else:
            angle_range=np.radians([357, 183])
        if angle_range[0]<3:
            direccion=1
        elif angle_range[0]>357:
            direccion=-1
        self.time+=dt*self.frequency*direccion
        angle=np.mean(angle_range)+np.diff(angle_range)/2*np.sin(2*np.pi*0.5*self.time)
        mob.set_angle(angle+PI/2)
        self.dot.move_to(self.line.get_end())
class PendulusScene(Scene):
    def construct(self):
        pendulus1, pendulus2=PendulusGroup(), PendulusGroup()
        pendulus1.derecha=True
        pendulus2.derecha=False
        self.add(pendulus1, pendulus2)
        self.wait(8)