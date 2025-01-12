from manim import *

def peek(self, string_of_text, fs, latex):
    # Create the stick figure parts
    head = Circle(radius=0.2, color=WHITE)
    body = Line(head.get_bottom(), head.get_bottom() + DOWN * 0.6, color=WHITE)
    left_arm = Line(body.get_start(), body.get_start() + LEFT * 0.4 + DOWN * 0.3, color=WHITE)
    right_arm = Line(body.get_start(), body.get_start() + RIGHT * 0.4 + DOWN * 0.3, color=WHITE)
    left_leg = Line(body.get_end(), body.get_end() + LEFT * 0.3 + DOWN * 0.5, color=WHITE)
    right_leg = Line(body.get_end(), body.get_end() + RIGHT * 0.3 + DOWN * 0.5, color=WHITE)

    # Bubble body
    speech_bubble = Group(ImageMobject("./images/speech_bubble.png").scale(0.1).next_to(head).shift(UP*0.5 + LEFT*0.2))
    if latex:
        bubble_text = MathTex(string_of_text, font_size = fs).set_color("BLACK")
    else:
        bubble_text = Tex(string_of_text, font_size = fs).set_color("BLACK")
    # Group all parts to form the stick figure
    stick_figure = Group(head, body, left_arm, right_arm, left_leg, right_leg, speech_bubble).scale(1.5).shift(DOWN*1.5);
    stick_figure.shift(LEFT * 10)  # Start off-screen

    # Make the stick figure peek
    def peek_animation():
            self.play(stick_figure.animate.shift(RIGHT * 4), runt_time = 1.5)  # Peek in
            self.play(Write(bubble_text.move_to(speech_bubble.get_center())))
            self.wait(1.5)  # Pause while peeking
            self.play(FadeOut(bubble_text))
            self.play(stick_figure.animate.shift(LEFT * 4))  # Move out of view
    
    # Do the animation
    peek_animation();


class BackgroundColorScene(Scene):
    def construct(self):
        # Set background color to #FFB38E
        self.camera.background_color = "#DE8F5F"
        
        # Add any other elements you want to the scene
        text = Text("""
        
        \"The definition of number, as that which is common to all collections of a given cardinal number, \n
        is purely logical and involves no assumption beyond the fundamental principles of logic.\"\n
        \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t - Bertrand Russell
        """).scale(0.45)
        # self.add(text)
        self.play(Write(text), time_frame = 2)
        self.wait(5);

class Introduction(Scene):
    def construct(self):
        # Set background color to #FFB38E
        self.camera.background_color = "#DE8F5F"
        
        