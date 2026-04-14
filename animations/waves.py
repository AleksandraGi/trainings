# source: https://www.youtube.com/watch?v=5anTYHWuMSA
from manim import *

class Hello(Scene):
    def construct(self):
        self.play(Write(Text("Hello Manim!")))
        self.wait(1)