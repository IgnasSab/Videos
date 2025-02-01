from manim import *
from assets.ignas_manim import *
import math

def introduction(self, topics):
    self.camera.background_color = "#DE8F5F"
    # Title
    title = Text("Topics", font_size=48)
    title.to_edge(UP*0.9)
    
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
        self.wait(2)

    # Hold the final scene for a moment before ending
    self.wait(2)

class Quote(Scene):
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

        title = Text("Introduction", font_size=48)
        title.to_edge(UP*0.9)
        self.play(Write(title));
        
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

class TitlePage(Scene):
    
    def construct(self):
        
        # List of topics
        topics = [
            "1. Cartesian Product",
            "2. Relations",
            "3. Integer definition",
            "4. Integer addition and multiplication",
            "5. Conclusion"
        ]
        introduction(self, topics)

class CartesianProduct(Scene):
    def construct(self):
        self.camera.background_color = "#DE8F5F"
        title = Text("Cartesian Product", font_size=48)
        title.to_edge(UP*0.9)
        self.play(Write(title))
        # Step 1: Introduce Set A (Yellow) and Set B (Blue)
        set_a = MathTex(r"A = \{1, 2, 3\}").shift(LEFT * 2)
        set_b = MathTex(r"B = \{3, 4\}").shift(RIGHT * 2)

        self.play(Write(set_a))
        self.wait(1)
        self.play(Write(set_b))
        self.wait(1)

        self.play(set_a.animate.set_color(YELLOW))
        self.play(set_b.animate.set_color(BLUE))
        self.wait(1)

        # Move sets up to make space for the Cartesian product
        self.play(set_a.animate.shift(UP * 2), set_b.animate.shift(UP * 2))
        self.wait(1)

        # Extract "A" and "B" letters for animation
        letter_A = set_a[0][0] # "A"
        letter_B = set_b[0][0]  # "B"

        # Cartesian Product text
        cartesian = MathTex(
            r"A \times B = \{ (1,3), (1,4), (2,3), (2,4), (3,3), (3,4) \}"
        ).shift(DOWN * 0.5)

        cartesian_c = cartesian.copy();

        cartesian[0][0].set_color(YELLOW)  # A
        cartesian[0][2].set_color(BLUE)    # B
        cartesian[0][6].set_color(YELLOW)  # 1
        cartesian[0][8].set_color(BLUE)   # 3
        cartesian[0][12].set_color(YELLOW) # 1
        cartesian[0][14].set_color(BLUE)   # 4
        cartesian[0][18].set_color(YELLOW) # 2
        cartesian[0][20].set_color(BLUE)   # 3
        cartesian[0][24].set_color(YELLOW) # 2
        cartesian[0][26].set_color(BLUE)   # 4
        cartesian[0][30].set_color(YELLOW) # 3
        cartesian[0][32].set_color(BLUE) # 3
        cartesian[0][36].set_color(YELLOW) # 3
        cartesian[0][38].set_color(BLUE)   # 4

        cartesian_1 = cartesian[0][0:3]
        cartesian_2 = cartesian[0][3:]


        # Transform "A" and "B" to the Cartesian product equation
        self.play(ReplacementTransform(letter_A.copy(), cartesian_1[0]), ReplacementTransform(letter_B.copy(), cartesian_1[2]))
        self.wait(2)

        # Write the rest of the Cartesian Product
        self.play(Write(cartesian_1[1:2]))
        self.wait(2)
        self.play(Write(cartesian_2))
        self.wait(2)
        
        self.play(FadeOut(cartesian), FadeOut(set_a), FadeOut(set_b))

        # Intermezzo
        formal = MathTex (
            r"A \times B = \{ (a, b) \; | \; a \in A \text{ and } b \in B\}"
        )
        self.play(Write(formal));
        self.wait(2);
        self.play(formal.animate.shift(UP * 0.5))
        
        not_equal = MathTex (
            r"(a, b) \neq (b, a)"
        ).shift(DOWN * 0.5)
        self.play(Write(not_equal))

        self.wait(2);
        self.play(FadeOut(not_equal), FadeOut(formal));

        # Taking back and visualizing 
        self.play(Write(cartesian_c));
        self.play(cartesian_c.animate.shift(UP * 2.5));
    
        # Create a NumberPlane (Grid) for Visualization
        grid = NumberPlane(
            x_range=[0, 5, 1], y_range=[0, 5, 1], axis_config={"include_numbers": True}
        ).move_to(ORIGIN).shift(DOWN).scale(0.8);

        self.play(Create(grid))
        self.wait(2)

        # Step 5: Plot Cartesian Product Points
        points = [
            (1, 3),
            (1, 4),
            (2, 3),
            (2, 4),
            (3, 3),
            (3, 4),
        ]
        dots = VGroup(*[Dot(grid.c2p(x, y), color=RED).scale(1.2) for x, y in points])


        # Label the points
        labels = VGroup(
            *[
                MathTex(f"({x},{y})", font_size = 25).next_to(Dot(grid.c2p(x, y)), UR, buff=0.15)
                for x, y in points
            ]
        )

        # Fade in dots and labels one by one
        # Fade in dots and labels one by one with surrounding rectangles
        for i, (dot, label) in enumerate(zip(dots, labels)):
            rect = SurroundingRectangle(cartesian_c[0][6 + i * 6 - 1:11 + i * 6 - 1], color=RED)
            self.play(Create(rect))
            self.play(FadeIn(dot), FadeIn(label))
            self.wait(1)
            self.play(FadeOut(rect))
        self.wait(2)

        self.play(*[FadeOut(mobj) for mobj in self.mobjects if mobj != title])

        # Step 1: Display the definition of the Cartesian product
        NN = MathTex(
            r"\mathbb{N} \times \mathbb{N} = \{ (a, b) \; | \; a \in \mathbb{N} \text{ and } b \in \mathbb{N}\}"
        )
        self.play(Write(NN))
        self.wait(2)

        NN2 = MathTex(
            r"\mathbb{N} \times \mathbb{N} = \{ (0, 0), (0, 1), (0, 2), \dots , (1, 0), (1, 1), (1, 2) \dots \}"
        )

        self.play(ReplacementTransform(NN, NN2))
        self.wait(2)

        self.play(NN2.animate.shift(2 * UP))

        # Step 2: Create and animate the first grid (6x6)
        self.create_grid(6, scale_factor=0.8, shift_amount=DOWN)


    def create_grid(self, grid_size, scale_factor, shift_amount):
        """
        Function to create a grid with fading dots and infinite arrows.
        - grid_size: Size of the grid (e.g., 6x6, 20x20, etc.)
        - scale_factor: Controls the grid scaling for visualization
        - shift_amount: Moves the grid down to fit scene
        """
        # Create number plane
        plane = NumberPlane(
            x_range=[0, grid_size, 1],
            y_range=[0, grid_size, 1],
            background_line_style={"stroke_color": BLUE, "stroke_width": 1, "stroke_opacity": 0.3},
            axis_config={"include_numbers": grid_size <= 10}  # Only show numbers for small grids
        ).scale(scale_factor).shift(shift_amount)

        self.play(Create(plane))

        # Create and animate dots with fading effect
        dots = VGroup()
        for x in range(grid_size):
            for y in range(grid_size):
                fade_factor = 1 - ((x + y) / (4 * grid_size))  # Control fading based on distance
                dot = Dot(plane.c2p(x, y), color=RED, radius=0.05)
                dot.set_opacity(fade_factor)  # Reduce opacity for distant points
                dots.add(dot)

        self.play(FadeIn(dots, run_time=2))

        self.wait(1)







