from manim import *
class PendulusGroup(VGroup):
    CONFIG={

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
        dot.move_to(line.get_end())
        line.dot=dot
        return line
class PendulusScene(Scene):
    def construct(self):
        pendulus=PendulusGroup()
        pendulus.add_updater(self.update_pendulus)
        self.add(pendulus)
        self.wait(3)
    def update_pendulus(self, pendulus, dt):
        pendulus.put_line(pendulus[1].dot)
        pendulus[1].dot.move_to(pendulus[1].get_end())
        return pendulus