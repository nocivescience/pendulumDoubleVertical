from manim import *
import numpy as np

class PendulusGroup(VGroup):
    CONFIG={
        'time': 0,
    }
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        dot=self.put_dot()
        line=self.put_line(dot)
        self.add(line, dot)
    def put_dot(self):
        dot=Dot(color=BLUE).move_to(self.get_center())
        return dot
    def put_line(self, dot):
        line=Line(self.get_center(), self.get_center()+DOWN*2)
        dot.add_updater(lambda d: d.move_to(line.get_end()))
        line.add_updater(self.update_pendulus)
        line.dot=dot
        return line
    def update_pendulus(self, dt):
        self.time += dt
        angle_range = np.radians([120, 240])  # Oscilar entre el primer y cuarto cuadrante
        angle = np.mean(angle_range) + np.diff(angle_range)/2 * np.sin(2 * np.pi * 0.5 * self.time)
        self[1].set_angle(angle + PI / 2)

class PendulusScene(Scene):
    def construct(self):
        pendulus=PendulusGroup()
        self.add(pendulus)
        self.wait(8)