from manim import *

def peek(self, string_of_text = None, fs = 35, latex = False, img_path = None):
    # Create the stick figure parts
    head = Circle(radius=0.2, color=WHITE)
    body = Line(head.get_bottom(), head.get_bottom() + DOWN * 0.6, color=WHITE)
    left_arm = Line(body.get_start(), body.get_start() + LEFT * 0.4 + DOWN * 0.3, color=WHITE)
    right_arm = Line(body.get_start(), body.get_start() + RIGHT * 0.4 + DOWN * 0.3, color=WHITE)
    left_leg = Line(body.get_end(), body.get_end() + LEFT * 0.3 + DOWN * 0.5, color=WHITE)
    right_leg = Line(body.get_end(), body.get_end() + RIGHT * 0.3 + DOWN * 0.5, color=WHITE)
    
    # Bubble body   
    speech_bubble = Group(ImageMobject("./images/speech_bubble.png").scale(0.1).next_to(head).shift(UP*0.5 + LEFT*0.2))
    if string_of_text != None:
        if latex:
            bubble_text = MathTex(string_of_text, font_size = fs).set_color("BLACK")
        else:
            bubble_text = Tex(string_of_text, font_size = fs).set_color("BLACK")
    if (img_path != None):
        img = ImageMobject(img_path).scale(0.1);
       

    # Group all parts to form the stick figure
    stick_figure = Group(head, body, left_arm, right_arm, left_leg, right_leg, speech_bubble).scale(1.5).shift(DOWN*1.5);
    stick_figure.shift(LEFT * 10)  # Start off-screen



    # Make the stick figure peek
    def peek_animation():
            self.play(stick_figure.animate.shift(RIGHT * 4), runt_time = 1.5)  # Peek in
            if (string_of_text != None):
                self.play(Write(bubble_text.move_to(speech_bubble.get_center())))
            if (img_path != None):
                self.play(FadeIn(img.move_to(speech_bubble.get_center())))
            self.wait(1.5)  # Pause while peeking
            if (string_of_text != None):
                self.play(FadeOut(bubble_text))
            if (img_path != None):
                self.play(FadeOut(img.move_to(speech_bubble.get_center())))
            self.play(stick_figure.animate.shift(LEFT * 4))  # Move out of view
    
    # Do the animation
    peek_animation();

def setup(self, txt):
    self.camera.background_color = "#DE8F5F"
    title = Text(txt, font_size=48)
    title.to_edge(UP*0.9)
    self.play(Write(title))