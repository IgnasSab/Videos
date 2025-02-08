from manim import *
from assets.ignas_manim import *

def hgh(pos, tuples, cl):
    remove = []
    for i, ind in enumerate(pos):
        rec = SurroundingRectangle(tuples[1][1 + ind * 6: 1 + ind * 6 + 5], color = cl, buff = 0.1)
        remove.append(rec);
    return remove

class Test(Scene):
    def construct(self):
        self.camera.background_color = "#DE8F5F"
        title = Text("Creating Integers").to_edge(UP);
        self.play(Write(title))



    









        


        
        
        




