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
        self.camera.background_color = "#DE8F5F"

        peek(self, r"Welcome!")

        # Load the image
        prev_scene_1 = ImageMobject("images/prev_video_1.png").scale(0.6).move_to(ORIGIN)
        prev_scene_2 = ImageMobject("images/prev_video_2.png").scale(0.6).move_to(ORIGIN)

        # Create a frame with the same size as the image
        frame = SurroundingRectangle(prev_scene_1, color = WHITE, stroke_color=BLACK, stroke_width=4, buff = 0.05)

        # Add elements to the scene
        self.play(Create(frame), FadeIn(prev_scene_1))
        peek(self, img_path = "images/youtube.png");
        self.wait(2);
        self.play(FadeOut(prev_scene_1));
        self.play(FadeIn(prev_scene_2));
        self.wait(2);
        self.play(FadeOut(prev_scene_2), FadeOut(frame));

        # Create a number line from -5 to 5
        number_line = NumberLine(
            x_range=[-5, 5, 1],  # From -5 to 5 with step 1
            length=10,
            include_numbers=True
        )

        # Create a dot at the origin (0)
        dot = Dot(color=RED).move_to(number_line.number_to_point(0))
        
        # Label for the number
        number_label = MathTex("0").next_to(dot, UP)

        # Add elements to the scene
        self.play(Create(number_line), FadeIn(dot, number_label))
        self.wait(1)

        # Function to move the dot and update label
        def move_dot(target_x):
            target_point = number_line.number_to_point(target_x)
            new_label = MathTex(str(target_x)).next_to(target_point, UP)
            self.play(dot.animate.move_to(target_point), Transform(number_label, new_label))
            self.wait(0.5)

        # Move the dot left and right
        move_dot(2)   # Move to +2
        move_dot(-3)  # Move to -3
        move_dot(4)   # Move to +4
        move_dot(-2)  # Move to -2
        move_dot(0)   # Move back to 0

        self.wait(2)
        self.play(FadeOut(dot, number_label, number_line));
        # Create a MathTex object for the integers with dots
        integers_text = MathTex(r"\mathbb{Z} = \{ \dots, -3, -2, -1, 0, 1, 2, 3 \dots \}").move_to(ORIGIN);
        naturals_text = MathTex(r"\mathbb{N} = \{0, 1, 2, 3 \dots \}").move_to(ORIGIN);
        # Show the empty space first
        self.play(Write(naturals_text));
        self.wait(2)

        self.play(Transform(naturals_text, integers_text), time_frame = 2);
        self.wait(2); 
        

        


        
        