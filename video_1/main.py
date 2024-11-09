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
        
        \"God created the natural numbers; all else is the work of man.\"\n
        \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t - Leopold Kronecker
        
        """).scale(0.6)
        # self.add(text)
        self.play(Write(text), time_frame = 2)
        self.wait(3);

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = "#DE8F5F"
        # Load the PNG images

        # Create the numbers from 1 to 10
        numbers = VGroup(*[
            Text(str(i)).set_color(WHITE) for i in range(1, 11)
        ])
        
        # Arrange the numbers in a line from left to right
        numbers.arrange(RIGHT, buff=0.5).move_to(ORIGIN)

        # Animate the appearance of each number one by one
        self.play(LaggedStart(*[FadeIn(num) for num in numbers], lag_ratio=0.25))
        self.wait(2);

        self.play(LaggedStart(*[FadeOut(num) for num in numbers], lag_ratio=0.25))
        self.wait(1)

        # Fade in the stick figure 
        stick_figure = ImageMobject("./images/stick_figure.png").scale(1.5).shift(DOWN)
        speech_bubble = ImageMobject("./images/speech_bubble.png").scale(0.25).next_to(stick_figure).shift(UP * 3 + LEFT)
        question_mark = Text("?").set_color("BLACK").move_to(speech_bubble.get_center())
        sad_face = Text(":(").set_color("BLACK").move_to(speech_bubble.get_center())
        apple = ImageMobject("./images/apple.png").scale(0.025);
        

        self.play(FadeIn(stick_figure), FadeIn(speech_bubble), Write(question_mark), time_frame = 2.5);
        self.wait(1);
        self.play(FadeOut(question_mark));
        
        # Speech bubble
        # # Create numbers popping up above apples
        numbers = VGroup(
            Text("1"), Text("2"), Text("3"), 
            Text("One"), Text("Two"), Text("Three")
        )

        for text in numbers:
            self.play(Write(text.set_color("BLACK").move_to(speech_bubble.get_center()), time_frame = 1));
            self.wait(0.5);
            self.play(FadeOut(text));
        for i in range(3):
            apples = Group(*[
                apple.copy() for j in range(i + 1)  # Adjust the range for the number of apples
            ]).arrange(RIGHT, buff = 0.2)
            apples.move_to(speech_bubble.get_center());
            self.play(LaggedStart(*[FadeIn(apple) for apple in apples], lag_ratio = 0.5))
            self.wait(0.5);
            self.play(FadeOut(apples));
    
        self.play(Write(question_mark), time_frame = 2);
        self.play(FadeOut(question_mark));

        self.play(Write(sad_face))
        self.wait(4);

class TitlePage(Scene):
    
    def construct(self):

        self.camera.background_color = "#DE8F5F"
        # Title
        title = Text("Topics", font_size=48)
        title.to_edge(UP*0.9)

        # List of topics
        topics = [
            "1. Definition of a set",
            "2. von Neumann construction of ordinals",
            "3. Definition of a successor",
            "4. Construction of the natural numbers",
            "5. Definition of addition",
            "6. Definition of multiplication",
            "7. Functions",
            "8. Conclusion"
        ]

        # Create Text objects for each topic
        topic_texts = [Text(topic, font_size=30) for topic in topics]

        # Arrange them vertically below the title
        topic_group = VGroup(*topic_texts).arrange(DOWN, aligned_edge=LEFT, buff = 0.4)
        topic_group.next_to(title, DOWN, buff=0.75)
        # Animate the title
        self.play(Write(title))
        self.wait(1)

        # Animate each topic one by one
        for i, topic in enumerate(topic_group):
            self.play(FadeIn(topic, shift=RIGHT))
            self.wait(1)

        # Hold the final scene for a moment before ending
        self.wait(2)

class SetDefinition(Scene):
    def construct(self):
        self.camera.background_color = "#DE8F5F"

        first_text = Text("Definition of a set", font_size = 40);
        self.play(Write(first_text));
        self.wait(3);
        self.play(FadeOut(first_text));


        set_definition = Text("Set is a collection of different items", font_size=40)
        self.play(Write(set_definition))
        self.wait(3)
        self.play(set_definition.animate.shift(UP * 3))

        # Define examples
        set_example_1 = Text("{hey, math, love}", font_size=35, t2c={"hey": YELLOW, "math": BLUE, "love": RED})
        set_example_2 = Text("{math, hey, love}", font_size=35, t2c={"hey": YELLOW, "math": BLUE, "love": RED})
        set_example_3 = Text("{love, hey, math}", font_size=35, t2c={"hey": YELLOW, "math": BLUE, "love": RED})

        set_example_0 = Text("{}", font_size= 40)

        # Display the first example
        self.play(Write(set_example_0))
        self.wait(2)
        self.play(ReplacementTransform(set_example_0, set_example_1))
        self.wait(2)

        # Shift the first example to the left
        self.play(set_example_1.animate.shift(LEFT * 4.5))
        self.wait(0.5)

        # Create equal signs and additional set examples
        equal_sign_1 = Text("=", font_size=35).next_to(set_example_1, RIGHT, buff=0.3)
        equal_sign_2 = Text("=", font_size=35).next_to(set_example_2, RIGHT, buff=0.3)

        # Position the new examples next to each other with equal signs
        set_example_2.next_to(equal_sign_1, RIGHT, buff=0.3)
        set_example_3.next_to(equal_sign_2, RIGHT, buff=0.3)

        # Display the additional examples and equal signs
        self.play(Write(equal_sign_1), Write(set_example_2), Write(equal_sign_2), Write(set_example_3))
        self.wait(5)

        # Fade out elements from left to right
        self.play(
            FadeOut(set_example_1),
            FadeOut(equal_sign_1),
            FadeOut(set_example_2),
            FadeOut(equal_sign_2),
            FadeOut(set_example_3),
            lag_ratio=0.15  # Controls the delay between each fade
        )

        # Load emoji images
        emoji1 = ImageMobject("./images/emoji_1.png").scale(0.15)  # Replace with your actual emoji image path
        emoji2 = ImageMobject("./images/emoji_2.png").scale(0.1)  # Replace with your actual emoji image path

        # Text elements for braces and comma
        left_brace = Text("{", font_size=40)
        right_brace = Text("}", font_size=40)
        comma = Text(",", font_size=40)

        # Position the elements to form a set-like structure
        left_brace.next_to(emoji1, LEFT, buff=0.1)
        emoji2.next_to(emoji1, RIGHT, buff=0.5)
        comma.next_to(emoji1, RIGHT, buff=0.1).shift(DOWN*0.2)
        right_brace.next_to(emoji2, RIGHT, buff=0.1)

        # Group all elements together
        emoji_set = Group(left_brace, emoji1, comma, emoji2, right_brace).shift(LEFT*0.5).scale(0.8)

        # Display the emoji set
        self.play(FadeIn(emoji_set))
        self.wait(2)
        self.play(FadeOut(emoji_set));


        set_example_4 = Text("{&, *, (, ), /, $}", font_size=35)
        self.play(Write(set_example_4))
        self.wait(2);

        set_example_5 = Text("{{hey}, {hey, love}}", font_size=35)
        self.play(ReplacementTransform(set_example_4, set_example_5));
        self.wait(2);

        set_example_6 = Text("{{hey}, (, ), &, #, {hey, love}, *}", font_size=35)
        self.play(ReplacementTransform(set_example_5, set_example_6))
        self.wait(6);


        set_example_8 = Text("{hey, hey}", font_size = 35)

        # Create the cross (X)
        line1 = Line(LEFT + UP, RIGHT + DOWN, color=RED, stroke_width=8)
        line2 = Line(LEFT + DOWN, RIGHT + UP, color=RED, stroke_width=8)
        cross = VGroup(line1, line2).scale(0.7).move_to(set_example_8)  # Position cross over text

        # Perform the transformation and add the cross
        self.play(ReplacementTransform(set_example_6, set_example_8))
        self.wait(4)
        self.play(FadeIn(cross))
        self.wait(0.5)
        # Optional emphasis animation on the cross
        self.play(cross.animate.scale(1.4), rate_func=there_and_back)  # Briefly enlarge the cross
        self.wait(2)

        self.play(set_example_8.animate.shift(DOWN*2), cross.animate.shift(DOWN*2))
        set_example_9 = Text("{hey}", font_size = 35);
        self.play(Write(set_example_9))
        self.wait(2)
        self.play(FadeOut(set_example_9), FadeOut(cross), FadeOut(set_example_8))
        

        # Add new label
        set_definition_1 = Text("The empty set").move_to(set_definition.get_center());
        self.play(ReplacementTransform(set_definition, set_definition_1));

        set_example_10 = Text("{}", font_size = 40)
        self.wait(2)
        self.play(Write(set_example_10))
        self.play(set_example_10.animate.shift(LEFT))
        equal_sign_3 = Text("=", font_size=40).next_to(set_example_10, RIGHT, buff=0.3)
        set_example_11 = MathTex(r"\emptyset", font_size = 60).next_to(equal_sign_3, RIGHT, buff = 0.3);
        self.play(Write(set_example_11))
        self.wait(2)
        self.play(Write(equal_sign_3))
        self.wait(3)
        self.play(FadeOut(set_example_10), FadeOut(equal_sign_3), FadeOut(set_example_11),  lag_ratio = 0.2)
        # Finally, some operations
        set_definition_2 = Text("Union of sets").move_to(set_definition).move_to(set_definition_1.get_center())
        self.play(ReplacementTransform(set_definition_1, set_definition_2))
        self.wait(10)

        set_A_equal = MathTex(r"A = \{a\}", font_size = 60)
        set_B_equal = MathTex(r"B = \{b\}", font_size = 60)
        set_A = MathTex(r"A", font_size = 60).shift(LEFT*3)
        set_B = MathTex(r"B ", font_size = 60).shift(LEFT)
        union_sign = MathTex(r"\cup", font_size = 60).shift(LEFT*2);
        set_AB = MathTex(r"=  \{a, b\}",font_size = 60).next_to(set_B, buff = 0.5)
        
        self.play(Write(set_A_equal), set_A_equal.animate.shift(LEFT*2), lag_ratio = 0.2);
        self.wait(1)
        self.play(Write(set_B_equal), set_B_equal.animate.shift(RIGHT*2), lag_ratio = 0.2);
        self.wait(1)
        self.play(set_A_equal.animate.shift(UP*1.5), set_B_equal.animate.shift(UP*1.5))
        self.wait(1)


        # Create copies of the elements 'a' and 'b' to move toward the union set
        element_a = set_A_equal[0][3].copy()
        element_b = set_B_equal[0][3].copy()
        
        # Position copies over the union set location and color them
        element_a_target = MathTex(r"a", font_size=60).set_color(YELLOW).move_to(set_AB[0][3]).shift(LEFT*0.25 + UP*0.15)
        element_b_target = MathTex(r"b", font_size=60).set_color(BLUE).move_to(set_AB[0][5]).shift(LEFT*0.28 + UP*0.06)

        # Create a copy of set_A_equal and transform it to set_A without removing set_A_equal
        # Create a copy of set_B_equal and transform it to set_B without removing set_B_equal
        set_A_copy = set_A_equal.copy()
        self.play(ReplacementTransform(set_A_copy, set_A))
        set_B_copy = set_B_equal.copy()
        self.play(ReplacementTransform(set_B_copy, set_B))
        self.wait(1)

        self.play(Write(union_sign))
        self.wait(1)
        self.play(Write(set_AB))
        self.wait(1)

        self.play(
            ReplacementTransform(element_a, element_a_target),
            ReplacementTransform(element_b, element_b_target),
            time_frame = 1
        )
        
        self.wait(1)

        self.play(FadeOut(element_a_target, element_b_target))

        set_A_equal_2 = MathTex(r"A = \{a, c\}", font_size = 60).move_to(set_A_equal.get_center());
        set_B_equal_2 = MathTex(r"B = \{b, c, \emptyset\}", font_size = 60).move_to(set_B_equal.get_center());
        set_AB_2 = MathTex(r"=  \{a, b, c, \emptyset\}", font_size = 60).next_to(set_B, buff = 0.5)
        self.play(ReplacementTransform(set_A_equal, set_A_equal_2), ReplacementTransform(set_B_equal, set_B_equal_2))
        self.wait(2);
        self.play(ReplacementTransform(set_AB, set_AB_2))
        self.wait(1)

class NeumannConstruction(Scene):
    def construct(self):
        self.camera.background_color = "#DE8F5F"
        
        self.wait(10)
        first_text = Text("Set-theoretic definition of natural numbers", font_size = 40);
        self.play(Write(first_text));
        self.wait(3);
        self.play(first_text.animate.to_edge(UP));
        
        # Add the example with number 0
        text_0 = MathTex("0", " = ", r"\emptyset", " = \{\}", font_size = 60);
        self.play(Write(text_0));
        self.wait(2);
        self.play(FadeOut(text_0[-1]), text_0[0:3].animate.move_to(ORIGIN));
        self.wait(2.5);
        self.play(text_0[0:3].animate.shift(2*UP))

        # Add the example with number 1
        text_1 = MathTex(r"1"," = ", r"\{",  "0", r"\}", font_size = 60);
        text_11 = MathTex(" = ", r"\{", r"\emptyset", r"\}", font_size = 60).next_to(text_1, RIGHT);
        text_1_group = Group(text_1, text_11)
        self.play(Write(text_1));
        self.wait(2)

        # Create the frames around 0
        framebox_0 = SurroundingRectangle(text_0[0], buff = 0.1)
        framebox_1 = SurroundingRectangle(text_1[3], buff = 0.1)

        self.play(Create(framebox_0));
        self.wait(1);
        self.play(ReplacementTransform(framebox_0, framebox_1));
        self.wait(1);
        self.play(FadeOut(framebox_1), time_frame = 0.5);
        self.play(Write(text_11), text_1_group.animate.move_to(ORIGIN), time_frame = 1, lag_ratio = 0.2);
        self.wait(2)

        # Create the frames around empty sets
        framebox_0_2 = SurroundingRectangle(text_0[2], buff = 0.1)
        framebox_1_2 = SurroundingRectangle(text_11[2], buff = 0.1)
        self.play(Create(framebox_0_2))
        self.wait(2);
        self.play(ReplacementTransform(framebox_0_2, framebox_1_2));
        self.wait(2);

        # Move the text to the top
        self.play(FadeOut(framebox_1_2), time_frame = 0.5);
        self.play(text_1_group.animate.shift(UP));

        # Add the example with number 2
        text_2 = MathTex(r"2", " = ", r"\{", "0", ",", "1", r"\}", font_size=60)
        text_22 = MathTex(" = ", r"\{", r"\emptyset", ",", r"\{ \emptyset \}", r"\}", font_size=60).next_to(text_2, RIGHT)
        text_2_group = Group(text_2, text_22)

        # Display text for "2" and move to origin
        self.play(Write(text_2))
        self.wait(2)

        # Highlight "0" and "1" across the texts
        framebox_0_next = SurroundingRectangle(text_0[0], buff=0.1)
        framebox_0_final = SurroundingRectangle(text_2[3], buff=0.1)
        framebox_1_next = SurroundingRectangle(text_1[0], buff=0.1)
        framebox_1_final = SurroundingRectangle(text_2[5], buff=0.1)

        # Highlight "0" moving to its new position in text_2
        self.play(Create(framebox_0_next))
        self.wait(1)
        self.play(ReplacementTransform(framebox_0_next, framebox_0_final))
        self.wait(1)

        # Highlight "1" moving to its new position in text_2
        self.play(Create(framebox_1_next))
        self.wait(1)
        self.play(ReplacementTransform(framebox_1_next, framebox_1_final))
        self.wait(1)

        # Move the group of text_2 upwards
        self.play(FadeOut(framebox_0_final, framebox_1_final))

        self.play(Write(text_22), text_2_group.animate.move_to(ORIGIN), time_frame=1)
        self.wait(2)

        framebox_0_2next = SurroundingRectangle(text_0[2], buff=0.1)
        framebox_0_2final = SurroundingRectangle(text_22[2], buff=0.1)
        framebox_1_2next = SurroundingRectangle(text_11[1:], buff=0.1)
        framebox_1_2final = SurroundingRectangle(text_22[4], buff=0.1)

        # Highlight "0" moving to its new position in text_2
        self.play(Create(framebox_0_2next))
        self.wait(1)
        self.play(ReplacementTransform(framebox_0_2next, framebox_0_2final))
        self.wait(1)

        # Highlight "1" moving to its new position in text_2
        self.play(Create(framebox_1_2next))
        self.wait(1)
        self.play(ReplacementTransform(framebox_1_2next, framebox_1_2final))
        self.wait(1)
        self.play(FadeOut(framebox_1_2final), FadeOut(framebox_0_2final));

        # Add the example with number 3
        text_3 = MathTex(r"3", " = ", r"\{", "0", ",", "1", ",", "2", r"\}", font_size=60).shift(DOWN)
        text_33 = MathTex(" = ", r"\{", r"\emptyset", ",", r"\{ \emptyset \}", ",", r"\{", r"\emptyset", ",", r"\{ \emptyset \}", r"\}", r"\}", font_size=60).next_to(text_3, RIGHT)
        text_3_group = Group(text_3, text_33)

        # Display text for "3" and move to origin
        self.play(Write(text_3))
        self.wait(2)
        self.play(Write(text_33), text_3_group.animate.move_to(ORIGIN).shift(DOWN) , time_frame=1)
        self.wait(2)

        # Create frames around the numbers to highlight and transition them
        # Frame for "0" in text_3 to text_33
        framebox_0_3 = SurroundingRectangle(text_0[2], buff=0.1)
        framebox_0_3_final = SurroundingRectangle(text_33[2], buff=0.1)
        
        # Frame for "1" in text_3 to text_33
        framebox_1_3 = SurroundingRectangle(text_11[1:], buff=0.1)
        framebox_1_3_final = SurroundingRectangle(text_33[4], buff=0.1)
        
        # Frame for "2" in text_3 to text_33
        framebox_2_3 = SurroundingRectangle(text_22[1:], buff=0.1)
        framebox_2_3_final = SurroundingRectangle(text_33[6:-1], buff=0.1)
        
        # Frame for "3" in text_3 to text_33
        framebox_3 = SurroundingRectangle(text_3[0], buff=0.1)
        framebox_3_final = SurroundingRectangle(text_33[0], buff=0.1)

        # Animate frames moving between texts
        self.play(Create(framebox_0_3))
        self.wait(1)
        self.play(ReplacementTransform(framebox_0_3, framebox_0_3_final))
        self.wait(1)

        self.play(Create(framebox_1_3))
        self.wait(1)
        self.play(ReplacementTransform(framebox_1_3, framebox_1_3_final))
        self.wait(1)

        self.play(Create(framebox_2_3))
        self.wait(1)
        self.play(ReplacementTransform(framebox_2_3, framebox_2_3_final))
        self.wait(1)


        # Fade out all frames and move the text group upwards
        self.play(FadeOut(framebox_0_3_final, framebox_1_3_final, framebox_2_3_final), lag_ratio = 0.5)


        # Pulsating effect to highlight text_33
        highlight_box = SurroundingRectangle(text_33[1:], color=RED, buff=0.15, fill_opacity = 0.1)
        self.play(Create(highlight_box))
        
        # Pulsating animation with expanding and contracting
        pulsate_times = 2  # Number of pulsations
        for _ in range(pulsate_times):
            self.play(highlight_box.animate.scale(1.1), run_time=1.5)  # Expand
            self.play(highlight_box.animate.scale(0.9), run_time=1.5)  # Contract



        # Fade out the highlight box
        self.play(FadeOut(highlight_box))
        self.wait(1)
        
        # Add vertical dots to indicate continuation
        text_4 = MathTex(r"\vdots", font_size = 60).scale(1.5).shift(DOWN*2.5)
        self.play(Write(text_4))
        self.wait(5)

class SuccessorFunction(Scene):
    def construct(self):
        self.camera.background_color = "#DE8F5F"
        
        text_successor = Text("Successor Function", font_size = 40);
        self.play(Write(text_successor));
        self.wait(10);
        self.play(text_successor.animate.shift(3*UP));
        self.wait(1);

        text_function = MathTex(r"S", "(", "n", ")", "=", "n", r"\cup", r"\{", "n", r"\}", font_size = 60);
        self.play(Write(text_function));
        self.wait(12)
        self.play(text_function.animate.shift(1.5*UP), time_frame = 1)
        text_n = MathTex("n = ", "0", font_size = 60);
        self.play(Write(text_n));
        self.wait(3);
        framebox_n = SurroundingRectangle(text_n, buff = 0.2, color = BLACK);
        self.play(Create(framebox_n))
        self.wait()
        text_n_rec = Group(framebox_n, text_n)
        self.play(text_n_rec.animate.to_corner(UL));
        self.wait();

        text_function_0 = text_function[0:4].copy();
        

        for i in range(0, 4):
            text_n[1].become(MathTex(str(i), font_size=60).move_to(text_n[1].get_center()))

            text_function_n = text_function.copy();
            text_function_x =  MathTex(r"S", "(", str(i), ") =", str(i), r"\cup", r"\{", str(i), r"\}", font_size = 60);
            text_function_x_right = MathTex(r"= \{", ",".join(str(num) for num in range(0, i + 1)), r"\} =", str(i + 1), font_size = 60).next_to(text_function_x)
            self.play(ReplacementTransform(text_function_n, text_function_x));
            self.wait(1);
            text_group = Group(text_function_x, text_function_x_right)
            self.play(Write(text_function_x_right), text_group.animate.move_to(ORIGIN), run_time = 2, lag_ratio = 0.2);
            if i == 0:
                self.wait(5)
            elif i == 3:
                self.wait(5)
            else:
                self.wait(2)
            self.play(FadeOut(text_group))
            self.wait(2)

        self.play(FadeOut(text_n_rec), time_frame = 1);

        self.wait(1)
        text_function_1 = MathTex(r"S", "(", "n", ")", "=", "n + 1", font_size = 60);
        self.play(ReplacementTransform(text_function, text_function_1))
        self.wait(7);

class ConstructingNaturalNumbers(Scene):
    def construct(self):
        self.camera.background_color = "#DE8F5F"

        text_function_0 = Text("Constructing Natural Numbers", font_size = 40);
        self.play(Write(text_function_0));
        self.wait(6);
        self.play(text_function_0.animate.to_edge(UP))


        text_function = MathTex(r"S", "(", "n", ")", "=", "n + 1", font_size = 60);

        self.play(Write(text_function), time_frame = 1);
        self.wait(8);
        self.play(text_function.animate.shift(2*UP))
        self.wait(1)

        number_line = NumberLine(
            x_range = [0, 10, 1],
            length = 10, 
            color = BLUE, 
            include_numbers = True
        ).scale(1)

        self.play(Create(number_line), run_time = 5)
        self.wait()

        text_number_line = MathTex(r"\cdots", font_size = 60, color = BLUE).next_to(number_line, buff = 0.5).shift(UP*0.2)
        self.play(Write(text_number_line));
        self.wait(1)

        # Loop to add circular arrows with labels
        for i in range(10):  # Adjust range according to the x_range of the number line
            start_pos = number_line.number_to_point(i)
            end_pos = number_line.number_to_point(i + 1)
            
            # Create a circular arrow from the current tick to the next
            arc = ArcBetweenPoints(start_pos, end_pos, radius=-0.6, color=YELLOW)  # Arc radius controls curve size

            # Create an arrowhead at the end of the arc to make it look like an arrow
            arrowhead = Triangle(color = YELLOW, fill_color=YELLOW, fill_opacity=1).scale(0.1)
            arrowhead.rotate(arc.get_angle() + PI / 2)  # Adjust angle by 90 degrees
            arrowhead.move_to(arc.point_from_proportion(1))  # Position it at the end of the arc
            
            # Add text label to the arc arrow (e.g., "Transition")
            label = MathTex(r"S(", str(i), ")", font_size=30).next_to(arc, UP)
            
            # Add the circular arrow and label to the scene
            if (i < 5): time = 1
            else: time = 0.25
            self.play(Create(arc), FadeIn(arrowhead), Write(label), run_time = time)
            self.wait(1)


        text_below = MathTex(r"10 = ", "S("*10, "0", ")"*10, font_size = 60).shift(2*DOWN);
        text_below_2 = MathTex("10 = 0", " + 1" * 10, font_size = 60).shift(2*DOWN);
        self.play(Write(text_below), run_time = 3);
        self.wait(2)
        self.play(ReplacementTransform(text_below, text_below_2))
        self.wait(2)    

        self.clear();
        self.camera.background_color = "#DE8F5F"
        self.wait(2)


        # Title text to introduce the set definition
        title = Text("Defining the Set of all natural numbers", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP));
        self.wait(1)

        # Step 1: Show that 0 is in X
        item1 = Tex(r"$\bullet$ 0 is in X", font_size=45)
        item2 = Tex(r"$\bullet$ If $n$ is in X, then $S(n)$ is in X", font_size=45)
        item3 = Tex(r"$\bullet$ X can contain infinite amount of elements", font_size=45)

        # Arrange the items in a vertical group
        item_group = VGroup(item1, item2, item3).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        # Display the itemized list on the screen
        self.play(Write(item_group))
        self.wait(10)

        # Optional: Move the list up
        self.play(item_group.animate.shift(1.4 * UP))
        self.wait(6)

        # Step 3: Illustrate the successor rule with some examples
        examples = VGroup()
        for i in range(4):  # Show a few terms
            example_text =  MathTex(r"S", "(", str(i), ") =", str(i + 1), r"\text{ in }", "X", font_size = 40);
            example_text.next_to(item_group, DOWN, buff=0.75 * (i + 1))
            examples.add(example_text)
        
        # Display each successor example one by one
        for example_text in examples:
            self.play(Write(example_text))
            self.wait(1)
        self.play(Write(MathTex(r"\vdots", font_size = 40).next_to(examples, DOWN, buff = 0.25)));

        # Clear the screen for the next part of your animation, if needed
        self.wait(7)
        peek(self, r"\mathbb{N} = X", 40, True)

        self.clear();

        # Define the initial title for the natural numbers set
        title = MathTex(r"\mathbb{N} = X = \{", font_size=48).to_edge(UP)
        num = 240
        # Create the sequence of numbers from 0 to 50, grouped for each row
        numbers = [str(i) for i in range(num)]
        rows = []
        for i in range(0, num, 20):
            # Create a row with 20 numbers (or fewer for the last row)
            row_content = ", ".join(numbers[i:i+20])
            
            # Check if it's the last row, then add the ellipsis
            if i + 20 >= num:
                row_content += r" \dots"
            
            # Append to rows list as a MathTex object
            rows.append(MathTex(row_content, font_size=32))
        
        # Arrange rows vertically below the title
        numbers_display = VGroup(*rows).arrange(DOWN, buff=0.2)
        numbers_display.next_to(title, DOWN, buff=0.5)
        
        last_bracket = MathTex(r"\}", font_size=48).next_to(numbers_display, DOWN, buff = 0.2)
        
        # Display title, numbers in rows, and ellipsis
        self.play(Write(title))
        for row in rows:
            self.play(Write(row), run_time = 0.5)
        self.play(Write(last_bracket))

        self.wait(2)

        self.play(FadeOut(title), FadeOut(numbers_display), FadeOut(last_bracket), run_time = 1)

        # Final remark, making natural numbers with actual sets
        peek(self, r" 0, 1, \dots 24 ", 35, True);

class ConstructingNaturalNumbers2(Scene):
    
    def construct(self):
        self.camera.background_color = "#DE8F5F"

        # Read lines from the file
        file_path = "natural_numbers_8.txt"
        with open(file_path, "r") as file:
            lines = file.readlines()
            
        line_texts = [];
        for line in lines:
            line = line.replace("{", "\\{")
            line = line.replace("}", "\\}")
            line = line.replace("0", "\\emptyset}")
            line_texts.append(MathTex(line, font_size = 30))

        # Create Text mobjects for each line in the file

        # Position each line as if they were part of a document
        for i, line_text in enumerate(line_texts):
            line_text.to_edge(UP).shift(DOWN * (i * 0.75))

        # Group the lines and add them to the scene
        file_content = VGroup(*line_texts)
        self.play(Write(file_content), run_time = 5)
        self.wait(1);
        # Simulate scrolling by shifting the lines upward
        scroll_distance = 52# Adjust this for the length of scroll
        self.play(file_content.animate.shift(UP * scroll_distance), run_time = 10, rate_func=linear)
        self.wait(2)

class DefiningAddition(Scene):
    def construct(self):
        self.camera.background_color = "#DE8F5F"

        first_text = Text("Defining addition of two natural numbers", font_size = 40);
        self.play(Write(first_text), run_time = 1);
        self.wait(11);
        self.play(first_text.animate.shift(3 * UP));
        self.wait(1)

        # # Defining addition
        item1 = Tex(r"$\bullet$ \;",  r"$a + 0 = a$", font_size=45)
        item2 = Tex(r"$\bullet$ \;",  r"$a + S(b) = S(a + b)$", font_size=45)

        # Arrange the items in a vertical group
        item_group = VGroup(item1, item2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        # # Display the itemized list on the screen
        self.play(Write(item_group[0]))
        self.wait(10)
        self.play(Write(item_group[1]))
        self.wait(5)

        peek(self, "What!?", 30, False)

        self.wait(5);

        # Optional: Move the list up
        self.play(item_group.animate.shift(1.8 * UP))
        self.wait(2)

        peek(self, "2 + 3", 35, True);

        self.wait(1)

        computation_steps = MathTex(
            r"2 + 3 &= 2 + S(2) \\",
            r"&= S(2 + 2) \\",
            r"&= S(2 + S(1)) \\",
            r"&= S(S(2 + 1)) \\",
            r"&= S(S(2 + S(0))) \\",
            r"&= S(S(S(2 + 0))) \\",
            r"&= S(S(S(2))) \\",
            r"&= 5",
            font_size=35,
        ).shift(1.5*DOWN)
        computation_steps[-1].set_color(YELLOW)
        computation_steps[0][0:3].set_color(YELLOW)
        example_box_computations = SurroundingRectangle(computation_steps, color=BLACK, buff=0.3, fill_color = GRAY, fill_opacity = 0.5)

        self.play(FadeIn(example_box_computations))

        cnt = 0;
        for step in computation_steps:
            self.play(Write(step), run_time = 1)
            if cnt == 1 or cnt == 3 or cnt == 5:
                example_box = SurroundingRectangle(item2[1], color=YELLOW, buff=0.2)
                self.play(Create(example_box))
                self.wait(3);
                self.play(FadeOut(example_box))
            elif cnt == 6:
                example_box = SurroundingRectangle(item1[1], color=YELLOW, buff=0.2)
                self.play(Create(example_box))
                self.wait(3);
                self.play(FadeOut(example_box))
            else:
                self.wait(3);
            cnt += 1;
        # Display the aligned computation steps
        self.wait(5)

        self.play(FadeOut(computation_steps), ShrinkToCenter(example_box_computations), item_group.animate.move_to(ORIGIN));
        self.wait(2);

class DefiningMultiplication(Scene):
    def construct(self):
        self.camera.background_color = "#DE8F5F"

        # Title
        first_text = Text("Defining multiplication of two natural numbers", font_size=40)
        self.play(Write(first_text), run_time=1)
        self.wait(2)
        self.play(first_text.animate.shift(3 * UP))
        self.wait(1)

        # Recursive definition of multiplication
        item1 = MathTex(r"\bullet \;",  r" a \cdot 0 = 0", font_size=45)
        item2 = MathTex(r"\bullet \;",  r" a \cdot S(b) = a + a \cdot b", font_size=45)

        # Arrange definitions in a vertical group
        item_group = VGroup(item1, item2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        self.play(Write(item_group[0]))
        self.wait(2)
        self.play(Write(item_group[1]))
        self.wait(2)
        # Adding a brief "What!?" prompt
        # peek(self, "What!?", 30, False)

        # Move the list up
        self.play(item_group.animate.shift(1.8 * UP))
        self.wait(2)

        # Example prompt
        peek(self, "2 \\times 3", 35, True)
        self.wait(1)

        # Detailed computation steps
        computation_steps = MathTex(
            r"2 \cdot 3 &= 2 + (2 \cdot 2) \\",
            r"&= 2 + (2 + (2 \cdot 1)) \\",
            r"&= 2 + (2 + (2 + (2 \cdot 0))) \\",
            r"&= 2 + (2 + (2 + 0)) \\",
            r"&= 2 + (2 + 2) \\",
            r"&= 2 + 4 \\",
            r"&= 6",
            font_size=40,
        ).shift(1.5 * DOWN)
        computation_steps[-1].set_color(YELLOW)
        computation_steps[0][0:4].set_color(YELLOW)
        example_box_computations = SurroundingRectangle(computation_steps, color=BLACK, buff=0.3, fill_color=GRAY, fill_opacity=0.5)

        # Display the computation steps box
        self.play(FadeIn(example_box_computations))

        cnt = 0
        for step in computation_steps:
            self.play(Write(step), run_time=1)
            if cnt <= 2:
                example_box = SurroundingRectangle(item2[1], color=YELLOW, buff=0.2)
                self.play(Create(example_box))
                self.wait(3)
                self.play(FadeOut(example_box))
            elif cnt == 3:
                example_box = SurroundingRectangle(item1[1], color=YELLOW, buff=0.2)
                self.play(Create(example_box))
                self.wait(3)
                self.play(FadeOut(example_box))
            else:
                self.wait(3)
            cnt += 1
        # Display the aligned computation steps
        self.wait(5)

        # Fade out the computation steps and reset items
        self.play(FadeOut(computation_steps), ShrinkToCenter(example_box_computations), item_group.animate.move_to(ORIGIN))
        self.wait(2) 

class MultiplicationAdditionFunctions(Scene):
    def construct(self):
        self.camera.background_color = "#DE8F5F"        
        # Define the machine (rectangle) with an operation symbol
        machine_box = Rectangle(width=3, height=2, color=BLACK, fill_color=GREY, fill_opacity=0.3)
        
        # Operation symbols for addition and multiplication
        addition_symbol = MathTex("+").scale(2).set_color(BLACK).move_to(machine_box.get_center())
        
        # Labels for machine
        machine_label = Text("Function", font_size=30, color=BLACK).move_to(machine_box.get_center())
        
        # Grouping machine elements
        addition_machine = VGroup(machine_box, machine_label).move_to(ORIGIN)
        multiplication_symbol = MathTex(r"\cdot").scale(2).set_color(BLACK).move_to(machine_box.get_center())
        multiplication_machine = VGroup(machine_box.copy(), multiplication_symbol).move_to(ORIGIN)
        
        # Inputs a and b
        a_label = MathTex("a", font_size = 60, color = YELLOW).next_to(machine_box, LEFT, buff=1.5).shift(0.5 * UP);
        b_label = MathTex("b", font_size = 60, color = YELLOW).next_to(machine_box, LEFT, buff=1.5).shift(0.5 * DOWN)
        
        # Output c
        c_label = MathTex("c", color=YELLOW).next_to(machine_box, RIGHT, buff=1.5)
        
        # Example with 2 and 3 input, output 5 for addition
        example_a = MathTex("2", color=YELLOW).next_to(machine_box, LEFT, buff=1.5).shift(0.5 * UP)
        example_b = MathTex("3", color=YELLOW).next_to(machine_box, LEFT, buff=1.5).shift(0.5 * DOWN)
        example_c_addition = MathTex("5", color=YELLOW).next_to(machine_box, RIGHT, buff=1.5)
        
        # Example with 2 and 3 input, output 6 for multiplication
        example_c_multiplication = MathTex("6", color=YELLOW).next_to(machine_box, RIGHT, buff=1.5)
        
        # Arrows for inputs and output
        arrow_a = Arrow(start=a_label.get_right(), end=machine_box.get_left(), color=BLACK)
        arrow_b = Arrow(start=b_label.get_right(), end=machine_box.get_left(), color=BLACK)
        arrow_c = Arrow(start=machine_box.get_right(), end=c_label.get_left(), color=BLACK)
        
        # Group for labels and arrows
        labels_group = VGroup(a_label, b_label, c_label, arrow_a, arrow_b, arrow_c)
        
        # Show the addition function machine
        self.play(FadeIn(addition_machine), Write(labels_group), lag_ration = 2)
        self.wait(3)

        self.play(ReplacementTransform(machine_label, addition_symbol));
        self.wait(3)
        
        # Show the example with 2, 3 as input, and output 5 for addition
        self.play(Transform(a_label, example_a), Transform(b_label, example_b), Transform(c_label, example_c_addition))
        self.wait(3)
        
        # Transition to multiplication function machine
        self.play(ReplacementTransform(addition_machine, multiplication_machine), Transform(c_label, example_c_multiplication))
        self.wait(3)
        
class Conclusion(Scene):
    def construct(self):
        self.camera.background_color = "#DE8F5F"

        # Title for Conclusion
        conclusion_title = Text("Conclusion", font_size=48)
        self.play(Write(conclusion_title))
        self.wait(1)
        self.play(conclusion_title.animate.to_edge(UP))
        self.wait(1)

        # 1. Collection of items
        collection_text = Text("Collection of items", font_size=40)
        collection_example = MathTex(r"\{ \text{apple, book, chair, ...} \}", font_size=40).next_to(collection_text, DOWN)
        self.play(Write(collection_text))
        self.play(Write(collection_example))
        self.wait(2)
        self.play(FadeOut(collection_text), FadeOut(collection_example))

        # 2. Successor Function: S(n) = n U {n}
        successor_text = Text("Successor Function", font_size=40)
        successor_function = MathTex(r"S(n) = n \cup \{n\}", font_size=40).next_to(successor_text, DOWN)
        self.play(Write(successor_text))
        self.play(Write(successor_function))
        self.wait(2)
        self.play(FadeOut(successor_text), FadeOut(successor_function))

        # 3. Axioms of Natural Numbers
        axioms_text = Text("Axioms of Natural Numbers", font_size=40)
        axiom1 = MathTex(r"\bullet \; 0 \; \text{is a natural number}", font_size=40).next_to(axioms_text, DOWN, aligned_edge=LEFT)
        axiom2 = MathTex(r"\bullet \; \text{If} \; n \; \text{is in} \; \mathbb{N} \text{, then} \; S(n) \; \text{is in} \; \mathbb{N}", font_size=40).next_to(axiom1, DOWN, aligned_edge=LEFT)
        axiom3 = MathTex(r"\bullet \; \text{Axiom of Infinity}", font_size=40).next_to(axiom2, DOWN, aligned_edge=LEFT)
        self.play(Write(axioms_text))
        self.play(Write(axiom1), run_time = 0.5)
        self.play(Write(axiom2), runt_time = 0.5)
        self.play(Write(axiom3), run_time = 0.5)
        self.wait(1)
        self.play(FadeOut(axioms_text), FadeOut(axiom1), FadeOut(axiom2), FadeOut(axiom3))

        # 4. Natural Numbers Set Construction
        natural_numbers_text = Text("Constructing Natural Numbers", font_size=40)
        natural_set = MathTex(r"\mathbb{N} = \{0, S(0), S(S(0)), \dots \}", font_size=40).next_to(natural_numbers_text, DOWN)
        self.play(Write(natural_numbers_text))
        self.play(Write(natural_set))
        self.wait(2)
        self.play(FadeOut(natural_numbers_text), FadeOut(natural_set))


        # 5. Defined Addition
        addition_text = Text("Defined Addition", font_size=40)
        addition_example = MathTex(r"a + 0 = a, \quad a + S(b) = S(a + b)", font_size=40).next_to(addition_text, DOWN)
        self.play(Write(addition_text))
        self.play(Write(addition_example))
        self.wait(2)
        self.play(FadeOut(addition_text), FadeOut(addition_example))

        # 6. Multiplication as Repeated Addition
        multiplication_text = Text("Multiplication as Repeated Addition", font_size=40)
        multiplication_example = MathTex(r"a \cdot 0 = 0, \quad a \cdot S(b) = a + (a \cdot b)", font_size=40).next_to(multiplication_text, DOWN)
        self.play(Write(multiplication_text))
        self.play(Write(multiplication_example))
        self.wait(2)
        self.play(FadeOut(multiplication_text), FadeOut(multiplication_example))

        # 7. Functions
        functions_text = Text("Functions", font_size=40)
        functions_example = Text("Producing outputs given inputs", font_size=30).next_to(functions_text, DOWN)
        self.play(Write(functions_text))
        self.play(Write(functions_example))
        self.wait(2)
        self.play(FadeOut(functions_text), FadeOut(functions_example))


        text_commutativity_1 = MathTex(r"a + b", "=", r"b + a");
        text_associativity_1 = MathTex(r"(a + b) + c", "=", r"a + (b + c)");
        text_commutativity_2 = MathTex(r"a \cdot b", "=", r"b \cdot a");
        text_associativity_2 = MathTex(r"(a \cdot b) \cdot c", "=", r"a \cdot (b \cdot c)");
        text_distributivity = MathTex(r"a \cdot (b + c)", "=", r"a \cdot b + a \cdot c");
        
        text_next_video = VGroup(text_commutativity_1, text_associativity_1, text_commutativity_2, text_associativity_2, text_distributivity).arrange(DOWN, aligned_edge = LEFT, buff = 0.25).move_to(ORIGIN);

        self.play(Write(text_next_video), run_time = 5);

        self.wait(1);

        peek(self, "Why?", 50, False);

        self.play(FadeOut(text_next_video));
        self.wait(1);
        self.play(conclusion_title.animate.move_to(ORIGIN))
        self.wait(1);
        self.play(FadeOut(conclusion_title));

class EndScene(Scene):
    def construct(self):
        # Create an orange rectangle that covers the entire screen
        background_rectangle = FullScreenRectangle(fill_color="#DE8F5F", fill_opacity=1)
        background_rectangle.set_stroke(color ="#DE8F5F")
        self.add(background_rectangle)
        
        # Wait for a moment to let the audience see the full orange screen
        self.wait(1)

        # Animate the rectangle shrinking to the center and fading out
        self.play(
            background_rectangle.animate.scale(0).set_opacity(0),
            rate_func=smooth,
            run_time=2,

        )

        # Pause briefly on the final black screen
        self.wait(1)

class ThumbNail(Scene):
    def construct(self):
        self.camera.background_color = "#DE8F5F"

        title = MathTex(r"\emptyset + \emptyset = \emptyset", font_size=200)
        self.add(title);




