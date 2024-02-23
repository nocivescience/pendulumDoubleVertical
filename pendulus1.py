from manim import *
class PendulusGroup(VGroup):
    CONFIG={

    }
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        dot=self.put_dot()
        line=self.put_line(dot)
        self.add(line)
    def put_dot(self, dot):
        dot=Dot().move_to(self.get_center())
        return dot
    def put_line(self, dot):
        line=Line(self.get_center(), self.get_center()+DOWN*2)
        dot.move_to(line.get_end())
        line.dot=dot
        return line
class PendulusScene(Scene):
    def construct(self):
        pendulus=PendulusGroup()
        self.add(pendulus)
        self.wait()