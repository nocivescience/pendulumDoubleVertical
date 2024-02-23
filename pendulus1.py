from manim import *
import itertools as it

class PendulusGroup(VGroup):
    CONFIG={
        'time': 0,
    }
    def __init__(self, longitud, **kwargs):
        super().__init__(**kwargs)
        self.time=self.CONFIG['time']
        self.derecha=True
        self.frequency=0.5
        self.color=BLUE
        self.longitud=longitud
        self.put_dot()
        self.put_line()
        self[1].add_updater(self.update_pendulus)
    def put_dot(self):
        self.dot=Dot(color=self.color, radius=.04).move_to(self.get_center())
        self.add(self.dot)
    def put_line(self):
        self.line=Line(self.get_center(), self.get_center()+DOWN*self.longitud, stroke_width=0.07)
        self.dot.add_updater(lambda d: d.move_to(self.line.get_end()))
        self.add(self.line)
    def update_pendulus(self, mob, dt):
        direccion=1
        if self.derecha: 
            angle_range=np.radians([1, 179])
        else:
            angle_range=np.radians([359, 181])
        if angle_range[0]<3:
            direccion=1
        elif angle_range[0]>357:
            direccion=-1
        self.time+=dt*self.frequency*direccion
        angle=np.mean(angle_range)+np.diff(angle_range)/2*np.sin(2*np.pi*0.5*self.time)
        mob.set_angle(angle+PI/2)
        self.dot.move_to(self.line.get_end())
class PendulusScene(Scene):
    CONFIGURATION={
        'colors': [BLUE, RED, GREEN, YELLOW, PURPLE, ORANGE, PINK, TEAL, WHITE, GREY]
    }
    def construct(self):
        frequencies= [freq for freq in np.linspace(0.1, 1, 20)]
        longitudes= ([l for l in np.linspace(2, .2, 20)])
        colors=it.cycle(self.CONFIGURATION['colors'])
        pendulos=VGroup()
        for side in [True, False]:
            for freq, long in zip(frequencies, longitudes):
                pendulus=PendulusGroup(longitud=long)
                pendulus.derecha=side
                pendulus.frequency=freq/4
                pendulus[0].color=next(colors)
                pendulus[0].set_z_index(-1)
                pendulos.add(pendulus)
        self.add(pendulos)
        self.wait(90)