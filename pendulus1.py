from manim import *
import numpy as np

class PendulusGroup(VGroup):
    CONFIG={
        'time': 0,
    }
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time=self.CONFIG['time']
        self.frequency=0.5
        self.put_dot()
        self.put_line()
        self[1].add_updater(self.update_pendulus)
    def put_dot(self):
        self.dot=Dot(color=BLUE).move_to(self.get_center())
        self.add(self.dot)
    def put_line(self):
        self.line=Line(self.get_center(), self.get_center()+DOWN*2)
        self.dot.add_updater(lambda d: d.move_to(self.line.get_end()))
        self.add(self.line)
    def update_pendulus(self, mob, dt):
        self.time+=dt*self.frequency
        angle_range=np.radians([3, 177])
        angle=np.mean(angle_range)+np.diff(angle_range)/2*np.sin(2*np.pi*0.5*self.time)
        mob.set_angle(angle+PI/2)
        self.dot.move_to(self.line.get_end())
class PendulusScene(Scene):
    def construct(self):
        pendulus=PendulusGroup()
        self.add(pendulus)
        self.wait(8)