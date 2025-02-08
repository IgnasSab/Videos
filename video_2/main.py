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
        setup(self, "Cartesian Product")
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

        # Fade in dots and labels one by one with surrounding rectangles
        for i, (dot, label) in enumerate(zip(dots, labels)):
            rect = SurroundingRectangle(cartesian_c[0][6 + i * 6 - 1:11 + i * 6 - 1], color=RED)
            self.play(Create(rect))
            self.play(FadeIn(dot), FadeIn(label))
            self.wait(1)
            self.play(FadeOut(rect))
        self.wait(2)

        self.play(FadeOut(*self.mobjects))

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

class Relations(Scene):
    def construct(self):
        setup(self, "Relations")

        # Step 2: Define set A
        set_a = MathTex(r"A = \{1, 2, 3\}")
        A = set_a[0][0].copy();
        self.play(Write(A.move_to(ORIGIN)))
        self.wait(2)

        self.play(A.animate.shift(2 * UP))

        relation = MathTex(r"R \subseteq A \times A").move_to(ORIGIN);

        self.play(Write(relation[0][0]));
        self.wait(2);
        self.play(Write(relation[0][1:]));
        self.wait(2)
        
        # Lets see an example...
        set_a.shift(2 * UP)
        self.play(Transform(A, set_a));

        # Step 3: Show Cartesian Product A × A
        cart_product_text = MathTex(
            r"A \times A = \{ (1,1), (1,2), (1,3),",
            r"(2,1), (2,2), (2,3),",
            r"(3,1), (3,2), (3,3) \}"
        ).shift(UP)

        self.play(Write(cart_product_text))
        self.wait(2)

        # Step 7: Define Relation R
        relationc = relation.copy()
        relation_r_text = MathTex(r"R = \{ (1,1), (1,2), (2,1), (2,2), (3,3) \}").move_to(ORIGIN);
        self.play(Transform(relation, relation_r_text))
        self.wait(2)
        self.play(Write(relationc[0][1:].next_to(relation_r_text)))

        self.wait(2);
        self.play(FadeOut(relationc[0][1:], relation, set_a, cart_product_text, A), relation_r_text.animate.shift(2 * UP))

    
        # Step 4: Transition to a 2D Grid for Cartesian Product
        grid = NumberPlane(x_range=[0, 4, 1], y_range=[0, 4, 1], axis_config={"include_numbers": True, "font_size":35}).scale(0.8).shift(DOWN)
        self.play(Create(grid))
        self.wait(1)

        # Step 6: Show all pairs in A × A with dots
        pairs = [
            (1,1), (1,2), (1,3),
            (2,1), (2,2), (2,3),
            (3,1), (3,2), (3,3),
        ]
        all_dots = VGroup(*[Dot(grid.c2p(x, y), color=GRAY) for x, y in pairs])
        self.play(FadeIn(all_dots))
        self.wait(2)


        # Step 8: Highlight Relation R on the Grid
        relation_pairs = [(1,1), (1,2), (2,1), (2,2), (3,3)]
        relation_dots = VGroup(*[Dot(grid.c2p(x, y), color=RED) for x, y in relation_pairs])
        self.play(FadeIn(relation_dots))
        self.wait(2)

        # Step 10: Transition to Non-Numeric Example
        self.play(FadeOut(grid, all_dots, relation_dots))
        self.wait(2)

        # There is another way to look at it:
        # Step 2: Define the tuples manually (positions in the MathTex string)
        tuples = ["(1,1)", "(1,2)", "(2,1)", "(2,2)", "(3,3)"]
        tuple_positions = [3, 9, 15, 21, 27]  # Indices of each tuple in the MathTex string
        remove = []
        for i, (tup, pos) in enumerate(zip(tuples, tuple_positions)):
            # Highlight the tuple with a SurroundingRectangle
            rect = SurroundingRectangle(relation_r_text[0][pos:pos+5], color=YELLOW)

            # Extract numbers from tuple "(a,b)"
            a, b = tup[1], tup[3]  # Extracting numbers from string format "(a,b)"
            if i >= 2:
                relation_text = MathTex(f"{a} \\: R \\: {b}")
                remove.append(relation_text);
            else:
                relation_text = MathTex(f"({a},{b}) \\in R")
                remove.append(relation_text);
                        
            relation_text.shift(2 * UP + (i+1) * DOWN)

            # Animate highlight and display relation statement
            self.play(Create(rect))
            self.wait(1)
            self.play(Write(relation_text))
            self.wait(1)

            # Fade out before moving to the next tuple
            self.play(FadeOut(rect))
        
        self.wait(2)

        self.play(FadeOut(*remove), FadeOut(relation_r_text))

        # # Example: People and Objects (Alice, Bob → Books, TVs)
        bob = Text("Bob", font_size = 40).move_to(ORIGIN);
        alice = Text("Alice", font_size = 40).move_to(ORIGIN);
        bob2 = bob.copy();
        alice2 = alice.copy();

        alice.shift(LEFT * 3 + 2 * UP)
        bob.shift(LEFT * 3)
        book = Text("Book", font_size = 40).shift(RIGHT * 3 + 2 * UP)
        TV = Text("TV",  font_size = 40).shift(RIGHT * 3)
        bob2.shift(LEFT * 3 + 2 * DOWN)
        alice2.shift(RIGHT * 3 + 2 * DOWN)

        self.play(Write(alice), Write(bob), Write(book), Write(TV), Write(alice2), Write(bob2))
        self.wait(2)

        # Draw arrows for relations (e.g., Alice → Book, Bob → TV)
        arrow1 = Arrow(start=alice.get_right(), end=book.get_left(), buff=0.2, color=YELLOW)
        arrow2 = Arrow(start=bob.get_right(), end=TV.get_left(), buff=0.2, color=YELLOW)
        arrow3 = Arrow(start=bob2.get_right(), end=alice2.get_left(), buff=0.2, color=YELLOW)
        self.play(Create(arrow1), Create(arrow2), Create(arrow3))
        self.wait(2)   

        self.play(FadeOut(arrow1, arrow2, arrow3, bob, alice, bob2, alice2, TV, book))

        # Step 1: Creating the relation
        set_a = MathTex(r"A = \{ \text{Bob}, \text{Alice}, \text{Book}, \text{TV} \}")

        self.play(Write(set_a))
        self.wait(2)
        self.play(set_a.animate.shift(2 * UP)) 

        # Define relation R
        set_r = MathTex(r"R", r"= \{(\text{Alice}, \text{Book}), (\text{Bob}, \text{TV}), (\text{Bob}, \text{Alice}) \}", r" \subseteq A \times A").move_to(ORIGIN)

        # New text "Likes" replacing "R"
        likes_text = MathTex(r"\text{Likes}").move_to(set_r[0])  # Position it where "R" was
        likes_text.set_color(YELLOW)  # Make "Likes" yellow

        self.play(Write(set_r))
        self.wait(1)

        # Transform "R" into "Likes"
        self.play(ReplacementTransform(set_r[0], likes_text), set_r[1:].animate.next_to(likes_text))
        self.wait(2)

        self.wait(2)
        self.play(FadeOut(set_a, likes_text), set_r.animate.shift(2 * UP))

        # Now we can say that... which gives it an unexpected meaning
        # This was a deviation from the actual content of this video, but nevertheless interesting to consider

        tuples = ["Alice", "Book", "Bob", "TV", "Bob", "Alice"]
        remove2 = []
        for i in range(0, 5, 2):
            # Extract names from tuple "(a,b)"
            a, b = tuples[i], tuples[i+1]
            
            # Create text "a Likes b"
            relation_text = VGroup(
                Text(a, font_size=35),
                Text(" Likes ", font_size=35, color=YELLOW),  # "Likes" in yellow
                Text(b, font_size=35)
            ).arrange(RIGHT)

            remove2.append(relation_text)
            mult = 0.75
            if i == 0:
                mult = 1
            relation_text.shift(2 * UP + (i + 1) * DOWN * mult)

            # Animate highlight and display relation statement
            self.play(Write(relation_text))
            self.wait(1)

        # Fade out all elements
        self.play(FadeOut(*remove2, set_r))

        # Function
                # Step 1: Create Axes
        axes = Axes(
            x_range=[-2, 2, 1],  # From -3 to 3 with tick marks every 1 unit
            y_range=[-8, 8, 2],  # From -10 to 10 with tick marks every 2 units
            axis_config={"include_numbers": True}
        ).scale(0.75).shift(1.25 * DOWN);

        # Labels for Axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("f(x)")

        # Step 2: Define the function f(x) = x^3
        def cubic_function(x):
            return np.clip(x**3, -9, 9) 

        graph = axes.plot(cubic_function, color=BLUE)

        # Step 3: Display the function equation
        equation = MathTex(r"f(x) = x^3").next_to(axes, UP + LEFT, buff = -0.5).set_color(BLUE)
        # Step 4: Show (x, f(x)) as a Relation
        relation_text = MathTex(r"f = \{ (x, x^3) \mid x \in \mathbb{R} \} \subseteq \mathbb{R} \times \mathbb{R}")

        # Step 5: Plot some example points
        sample_x_values = [-1, 0, 1]
        dots = VGroup()
        labels = VGroup()

        self.play(Write(relation_text))
        self.wait(2)
        self.play(relation_text.animate.shift(2 * UP))
        self.wait(1)

        for x in sample_x_values:
            y = cubic_function(x)
            dot = Dot(axes.c2p(x, y), color=RED)
            label = MathTex(f"({x}, {y})", font_size = 35).next_to(dot, UR, buff=0.2)
            dots.add(dot)
            labels.add(label)

        # Animate the scene
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(1)

        self.play(Write(equation))
        self.play(Create(graph))
        self.wait(1)

        self.play(FadeIn(dots), Write(labels))
        self.wait(2)

        self.play(FadeOut(dots, labels, relation_text, equation, graph, axes, x_label, y_label))

class EquivalenceRelations(Scene):
    def construct(self):
        self.camera.background_color = "#DE8F5F"
        # Step 1: Title
        title = Text("Equivalence Relations").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Step 2: Define Reflexivity, Symmetry, Transitivity
        reflexive_text = Tex(r"1. Reflexive: $(a, a) \in R$ for all $a \in A$")
        symmetric_text = Tex(r"2. Symmetric: If $(a, b) \in R$, then $(b, a) \in R$")
        transitive_text = Tex(r"3. Transitive: If $(a, b) \in R$ and $(b, c) \in R$, then $(a, c) \in R$")
        denoted_as = Tex(r"If $ (a, b) \in R $ and $R$ is equivalence relation, then $a \sim b$")


        properties = VGroup(reflexive_text, symmetric_text, transitive_text, denoted_as).arrange(DOWN, buff=0.5, aligned_edge = LEFT).move_to(ORIGIN)

        self.play(Write(properties, time_frame = 2))
        self.wait(2)

        # Lets see an example of each of them
        self.play(FadeOut(symmetric_text, transitive_text, denoted_as), reflexive_text.animate.next_to(title, DOWN, buff = 0.5));
        set_a = MathTex(r"A = \{1, 2, 3\}")

        self.play(Write(set_a))
        self.wait(2)

        symmetric_text.next_to(title, DOWN, buff = 0.5)
        transitive_text.next_to(title, DOWN, buff = 0.5)

        self.play(set_a.animate.to_corner(UL).shift(0.1 * DOWN))
        surround_rec = SurroundingRectangle(set_a, color = BLACK, stroke_width = 4)
        background_rec = BackgroundRectangle(set_a, color=BLACK, fill_opacity=0.2, buff = 0.1)
        self.play(FadeIn(surround_rec, background_rec))


        r_1 = MathTex(r"R =", r" \{ (1, 1), (2, 2), (1, 2), (3, 3) \}")
        r_2 = MathTex(r"R =", r" \{ (1, 1), (2, 2), (1, 2), (2, 1) (3, 3) \}")
        r_3 = MathTex(r"R =", r" \{ (1, 2), (2, 3) \}")
        r_4 = MathTex(r"R =", r" \{ (1, 2), (2, 3), (1, 3) \}")
        
        self.play(Write(r_1))

        recs = hgh([0, 1, 3], r_1, YELLOW)
        for rec in recs:
            self.play(FadeIn(rec));
            self.wait(1);
        for rec in recs:
            self.play(FadeOut(rec))

        recs = hgh([2], r_1, RED)
        for rec in recs:
            self.play(FadeIn(rec));
            self.wait(1);
        for rec in recs:
            self.play(FadeOut(rec))    

        self.play(ReplacementTransform(r_1, r_2), ReplacementTransform(reflexive_text, symmetric_text))
        self.wait(2)
        
        recs = hgh([2, 3], r_2, YELLOW)
        for rec in recs:
            self.play(FadeIn(rec));
            self.wait(1);
        for rec in recs:
            self.play(FadeOut(rec))

        self.play(ReplacementTransform(symmetric_text, transitive_text), ReplacementTransform(r_2, r_3))
        self.wait(2)
        recs = hgh([0, 1], r_3, RED)
        for rec in recs:
            self.play(FadeIn(rec));
            self.wait(1);
        for rec in recs:
            self.play(FadeOut(rec))

        self.play(ReplacementTransform(r_3, r_4))
        recs = hgh([0, 1, 2], r_3, YELLOW)
        for rec in recs:
            self.play(FadeIn(rec));
            self.wait(1);
        for rec in recs:
            self.play(FadeOut(rec))
        self.wait(2)
        
        self.play(FadeOut(transitive_text, r_4, background_rec, surround_rec, set_a))
        
        # Step 3: Example - Set A and Relation R
        set_a = MathTex(r"A = \{ 1, 2, 3, 4, 5\}").shift(UP * 2)
        relation_r = MathTex(r"R = \{ (a, b) \mid a + b \text{ is even} \}").shift(UP)

        self.play(Write(set_a));
        self.wait(1)
        self.play(Write(relation_r))
        self.wait(2)

        self.play(FadeOut(set_a), relation_r.animate.shift(UP))

        # Step 4: Cartesian Plane Representation
        axes = NumberPlane(
            x_range=[0, 6, 1], y_range=[0, 6, 1], axis_config={"include_numbers": True}
        ).set_opacity(1).scale(0.8).shift(DOWN)


        # Step 5: Plot Relation (a, b) where a + b is even
        points = [(1,1), (1,3), (1,5), (2,2), (2,4), (3,1), (3,3), (3,5), (4,2), (4,4), (5,1), (5,3), (5,5)]
        dots = VGroup(*[Dot(axes.c2p(a, b), color=RED) for a, b in points])
        labels = VGroup(
            *[
                MathTex(f"({a},{b})", font_size = 30).next_to(Dot(axes.c2p(a, b)), UR, buff=0.1)
                for a, b in points
            ]
        )

        self.play(Create(axes))
        self.wait(1)
        self.play(FadeIn(dots), Write(labels))
        self.wait(2)

        # Step 6: Highlight Reflexivity
        reflexive_pairs = [(1,1), (2,2), (3,3), (4,4), (5,5)]
        reflexive_dots = VGroup(*[Dot(axes.c2p(a, a), color=GREEN) for a, _ in reflexive_pairs])
        self.play(FadeIn(reflexive_dots))
        self.wait(2)
        self.play(FadeOut(reflexive_dots))
        self.wait(2)

        # Step 7: Highlight Symmetry
        symmetric_pairs = [(1,3), (3,1), (1,5), (5,1), (2,4), (4,2), (3,5), (5,3)]
        symmetric_dots = VGroup(*[Dot(axes.c2p(a, b), color=GREEN) for a, b in symmetric_pairs])
        for i in range(0, 8, 2):
            self.play(FadeIn(symmetric_dots[i], symmetric_dots[i+1]))
            self.wait(2);
            self.play(FadeOut(symmetric_dots[i], symmetric_dots[i+1]))

        self.wait(2)

        # Step 8: Highlighst Transitivity
        transitive_triplets = [(1,3), (3,5), (1,5), (3, 1), (5, 3), (5, 1)]
        transitive_dots = VGroup(*[Dot(axes.c2p(a, b), color=GREEN) for a, b in transitive_triplets])
        for i in range(0, 6, 3):
            self.play(FadeIn(transitive_dots[i], transitive_dots[i+1], transitive_dots[i+2]))
            self.wait(2);
            self.play(FadeOut(transitive_dots[i], transitive_dots[i+1], transitive_dots[i+2]))
        self.wait(2)

        self.play(FadeOut(axes, dots, labels, relation_r))

        # Why are equivalence relations useful
                # Step 9: Introduce Equivalence Classes Definition
        eq_class_def = Tex(
            r"For $a \in A$, the equivalence class $[a]$ is defined as:", 
            r"\[ [a] = \{ b \in A \mid a \sim b \} \]"
        ).move_to(ORIGIN)

        self.play(Write(eq_class_def))
        self.wait(3)

        self.play(FadeOut(eq_class_def[0]), eq_class_def[1].animate.next_to(title, DOWN, buff = 0.5))

        # Step 10: Show Equivalence Classes for the Given Relation
        class_1 = MathTex(r"[1] = \{1, 3, 5\}").set_color(BLUE).to_edge(LEFT)
        class_2 = MathTex(r"[2] = \{2, 4\}").set_color(YELLOW).next_to(class_1, DOWN, buff=0.5)

        self.play(Write(class_1))
        self.play(Write(class_2))
        self.wait(2)



        # Step 11: Group the Elements in A According to Equivalence Classes
        odd_numbers = [(1,1), (1,3), (1,5), (3,1), (3,3), (3,5), (5,1), (5,3), (5,5)]
        even_numbers = [(2,2), (2,4), (4,2), (4,4)]

        odd_dots = VGroup(*[Dot(axes.c2p(a, b), color=BLUE) for a, b in odd_numbers])
        even_dots = VGroup(*[Dot(axes.c2p(a, b), color=YELLOW) for a, b in even_numbers])

        self.play(FadeIn(axes, labels, odd_dots, even_dots))
        self.wait(2)

        
        # Step 11: Show that choosing 3 as the representative is valid
        class_1_new = MathTex(r"[3] = \{1, 3, 5\}").set_color(BLUE).to_edge(LEFT)
        class_2_new = MathTex(r"[4] = \{2, 4\}").set_color(YELLOW).next_to(class_1_new, DOWN, buff=0.5)

        self.play(Transform(class_1, class_1_new), Transform(class_2, class_2_new))
        self.wait(2)

        # Step 12: Show that choosing 5 as the representative also works
        class_1_final = MathTex(r"[5] = \{1, 3, 5\}").set_color(BLUE).to_edge(LEFT)
        class_2_final = MathTex(r"[2] = \{2, 4\}").set_color(YELLOW).next_to(class_1_final, DOWN, buff=0.5)

        self.play(Transform(class_1, class_1_final), Transform(class_2, class_2_final))
        self.wait(2)

        # Step 13: Fade Out Everything
        self.play(FadeOut(axes, eq_class_def[1], class_1, class_2, odd_dots, even_dots, labels))
        self.wait(2)

        # Addition of classes:

                # Step 2: Define Addition
        addition_def = MathTex(r"[a] + [b] = [a + b]").shift(UP)
        self.play(Write(addition_def))
        self.wait(1)

        # Step 3: Define Multiplication
        multiplication_def = MathTex(r"[a] \cdot [b] = [a \cdot b]").shift(DOWN)
        self.play(Write(multiplication_def))
        self.wait(2)

        # Step 4: Transition to Example (Parity Equivalence Classes)
        self.play(FadeOut(addition_def, multiplication_def))

        # Step 5: Write Equivalence Classes
        odd_class = MathTex(r"[1] = \{\text{odd numbers}\}").set_color(BLUE).shift(LEFT * 3 + UP)
        even_class = MathTex(r"[2] = \{\text{even numbers}\}").set_color(YELLOW).shift(LEFT * 3 + DOWN)

        self.play(Write(even_class), Write(odd_class))
        self.wait(2)

        addition_rule = MathTex(
            r"\begin{aligned}"
            r"\left[2\right] + \left[2\right] &= \left[4\right] = \left[2\right] \\"  
            r"\left[1\right] + \left[1\right] &= \left[2\right] \\"  
            r"\left[2\right] + \left[1\right] &= \left[3\right] = \left[1\right]"
            r"\end{aligned}"
        ).shift(RIGHT * 3 + UP * 1)


        multiplication_rule = MathTex(
            r"\begin{aligned}"
            r"\left[2\right] \times \left[2\right] &= \left[4\right] = \left[2\right] \\"  # Even * Even = Even
            r"\left[1\right] \times \left[1\right] &= \left[1\right] \\"  # Odd * Odd = Odd
            r"\left[2\right] \times \left[1\right] &= \left[2\right]"
            r"\end{aligned}"
        ).next_to(addition_rule, DOWN, buff=1)

        # Step 6: Show Addition Rules
        addition_rule_2 = MathTex(
            r"\begin{aligned}"
            r"\text{even} + \text{even} &= \text{even} \\"
            r"\text{odd} + \text{odd} &= \text{even} \\"
            r"\text{even} + \text{odd} &= \text{odd}"
            r"\end{aligned}"
        ).shift(RIGHT * 3 + UP * 1)

        # Step 7: Show Multiplication Rules
        multiplication_rule_2 = MathTex(
            r"\begin{aligned}"
            r"\text{even} \times \text{even} &= \text{even} \\"
            r"\text{odd} \times \text{odd} &= \text{odd} \\"
            r"\text{even} \times \text{odd} &= \text{even}"
            r"\end{aligned}"
        ).next_to(addition_rule_2, DOWN, buff=1)



        self.play(Write(addition_rule))
        self.wait(2)
        self.play(Write(multiplication_rule))
        self.wait(2)


        self.play(Transform(addition_rule, addition_rule_2))
        self.wait(3)
        self.play(Transform(multiplication_rule, multiplication_rule_2))
        self.wait(3);

        # Step 8: Fade Out Everything
        self.play(FadeOut(title, even_class, odd_class, addition_rule, multiplication_rule))
        self.wait(2)

class ConstructingIntegers(Scene):
    def construct(self):
        self.camera.background_color = "#DE8F5F"
        title = Text("Constructing Integers").to_edge(UP);
        self.play(Write(title))

        N = MathTex(r"\mathbb{N} = \{0, 1, 2, \dots \}")
        self.play(Write(N))
        self.wait(2)
        self.play(N.animate.shift(2* UP))

        set_a = MathTex("(", r"\mathbb{N} \times \mathbb{N}", r") \times (", r"\mathbb{N} \times \mathbb{N}", ")")

        tup = [1, 3]
        tup2 = [0, 2, 4]

        self.play(Write(set_a[1]), Write(set_a[3]))
        self.wait(2)
        self.play(Write(set_a[0]), Write(set_a[2]), Write(set_a[4]))
        self.wait(2)

        self.play(FadeOut(N), set_a.animate.shift(2 * UP))

        set_ac = set_a.copy()

        tuples_a = MathTex(r"(", "(a, b)", r",", r"(c, d)", r")")
        self.play(ReplacementTransform(set_ac[1], tuples_a[1]))
        self.wait(2);
        self.play(ReplacementTransform(set_ac[3], tuples_a[3]))
        self.wait(2)
        self.play(ReplacementTransform(set_ac[0], tuples_a[0]), ReplacementTransform(set_ac[2], tuples_a[2]), ReplacementTransform(set_ac[4], tuples_a[4]))
        self.wait(2)
        
        subset = MathTex(r"\in").next_to(tuples_a)
        self.play(Write(subset), set_a.animate.next_to(subset));
        group = VGroup(subset, set_a, tuples_a)
        self.play(group.animate.move_to(ORIGIN));
        self.wait(2)
        self.play(group.animate.shift(UP))
        self.wait(2);
        set_b = MathTex(r"A = \mathbb{N} \times \mathbb{N}").shift(2 * UP);
        self.play(Write(set_b));
        group.remove(subset, tuples_a)
        relation = MathTex(r"R \subseteq").next_to(set_a, LEFT)
        self.play(FadeOut(subset, tuples_a), FadeIn(relation))
        group.add(relation)
        self.wait(2);

        self.play(FadeOut(group, set_b))

                # Defining the relation
        relation = MathTex(r"R = \{ ((a, b), (c, d)) \mid a + d = b + c \}")

        # Color 'a' and 'b' Yellow
        relation[0][5].set_color(YELLOW)
        relation[0][7].set_color(YELLOW)
        relation[0][11].set_color(BLUE)
        relation[0][13].set_color(BLUE)
        relation[0][17].set_color(YELLOW)
        relation[0][19].set_color(BLUE)
        relation[0][21].set_color(YELLOW)
        relation[0][23].set_color(BLUE)
        self.play(Write(relation))
        self.wait(2)
        self.play(relation.animate.shift(2 * UP))

        # Firstly we prove that it is an equivalence relation, so it satisfies all the required properties
            
        proof_title = MathTex(r"1. \text{ Reflexivity:}").to_edge(LEFT).shift(UP)
        self.play(Write(proof_title))
        # Reflexivity: (a, b) R (a, b)
        reflexivity = MathTex(r"\text{For all pairs we have } (a, b) \; R \; (a, b), \text{since }  a + b = b + a")
        self.play(Write(reflexivity))
        self.wait(1)
        self.wait(1)
        self.play(FadeOut(reflexivity))

        ### Symmetry: (a, b) R (c, d) → (c, d) R (a, b)
        proof_title_2 = MathTex(r"2. \text{ Symmetry:}").move_to(proof_title)
        symmetry = MathTex(r"\text{If } (a, b) \; R \; (c, d) \text{ then } (c, d) \; R \; (a, b)")
        step1 = MathTex(r"a + d = b + c").next_to(symmetry, DOWN);
        step2 = MathTex(r"c + b = d + a").next_to(step1, DOWN)
        step3 = MathTex(r"(c, d) \; R \; (a, b)").next_to(step2, DOWN)
        self.play(ReplacementTransform(proof_title, proof_title_2))
        self.play(Write(symmetry))
        self.wait(1);
        self.play(Write(step1))
        self.wait(1);
        self.play(Write(step2))
        self.wait(1)
        self.play(Write(step3))
        self.wait(1)
        self.play(FadeOut(symmetry, step1, step2, step3))

        proof_title_3 = MathTex(r"3. \text{ Transitivity:}").move_to(proof_title_2)
        # Transitivity: If (a, b) R (c, d) and (c, d) R (e, f), then (a, b) R (e, f)
        transitivity = MathTex(
            r"\text{If } (a, b) \; R \; (c, d) \text{ and } (c, d) \; R \; (e, f) \text{ then } (a, b) \; R \; (e, f)"
        )
        self.play(ReplacementTransform(proof_title_2, proof_title_3))
        self.play(Write(transitivity))
        self.wait(1)

        step1 = MathTex(r"a + d = b + c, c + f = d + e").next_to(transitivity, DOWN)
        step2 = MathTex(r"a + d + c + f = b + c + d + e").next_to(step1, DOWN)
        step3 = MathTex(r"a + f = b + e").next_to(step2, DOWN)
        step4 = MathTex(r"(a, b) \; R \; (e, f)").next_to(step3, DOWN)

        self.play(Write(step1))
        self.wait(1)
        self.play(Write(step2))
        self.wait(1)
        self.play(Write(step3))
        self.wait(1)
        self.play(Write(step4))
        self.wait(1)

        self.wait(1)
        self.play(FadeOut(transitivity, step1, step2, step3, step4, proof_title_3))

        # Intuition (before we look at what equivalence classes can offer to us, lets get some intuition on what does this relation tell us)
        example = MathTex(r"(a, b)", r" \sim ", r"(c, d)", r"\; \Leftrightarrow \;" , r"a + c = b + d")
        self.play(Write(example))
        transformed_example = MathTex(r"a - b", "=", "d - c").move_to(example[-1])
        self.play(ReplacementTransform(example[-1], transformed_example))
        self.play(Indicate(example[0]), Indicate(transformed_example[0]))
        self.wait(2)
        self.play(Indicate(example[2], color = BLUE), Indicate(transformed_example[2], color = BLUE))
        self.wait(2)

        self.play(FadeOut(example, transformed_example))
        self.wait(1)

        # Create a number line from -5 to 5
        number_line = NumberLine(
            x_range=[-5, 5, 1],  # From -5 to 5 with step 1
            length=10,
            include_numbers=True
        )

        # Add the number line to the scene
        self.play(Write(number_line))
        self.wait(1)

        # Define positions and corresponding tuples
        points = [0, 3, -2]  # Example positions on the number line
        tuples = [(0, 0), (2, 2), (3, 0), (4, 1), (0, 2), (1, 3)]  # Corresponding (a, b)

        # Create a dot to move along the line
        dot = Dot().move_to(number_line.n2p(points[0]))
        dot.set_color(RED)
        tuple_text = MathTex(f"({tuples[0][0]}, {tuples[0][1]})", font_size = 35).next_to(dot, UP, buff = 0.1)
        tuple_text2 = MathTex(f"({tuples[1][0]}, {tuples[1][1]})", font_size = 35).move_to(tuple_text)
        self.play(FadeIn(dot), Write(tuple_text))
        self.wait(2);
        self.play(Transform(tuple_text, tuple_text2))
        self.wait(2)
        # Move dot from one point to another, updating (a, b)
        for i in range(1, len(points)):
            new_position = number_line.n2p(points[i])
            new_tuple = MathTex(f"({tuples[i * 2][0]}, {tuples[i * 2][1]})", font_size = 35).next_to(new_position, UP)
            self.play(dot.animate.move_to(new_position), ReplacementTransform(tuple_text, new_tuple))
            self.wait(2)
            tuple_text = MathTex(f"({tuples[i * 2 + 1][0]}, {tuples[i * 2 + 1][1]})", font_size = 35).move_to(new_tuple)
            self.play(ReplacementTransform(new_tuple, tuple_text))
            self.wait(2)

        self.wait(2)

        self.play(FadeOut(number_line, dot, tuple_text, relation))
        
        ##########################################################################################################
        # It would be nice to group, and this is where the equivalence classes come 

        # Definition of equivalence class
        definition = MathTex(r"[(a, b)] = \{(c, d) \in \mathbb{N} \times \mathbb{N} \mid \;",  r"(a, b) \sim (c, d)", r"\}")
        definition2 = MathTex(r"a + d = b + c").move_to(definition[-2]);


        self.play(Write(definition))
        self.wait(2)
        self.play(ReplacementTransform(definition[-2], definition2))
        self.wait(2)
        self.play(definition.animate.shift(2 * UP))
        self.wait(2)
        definition3 = MathTex(r"\mathbb{Z} = \{ [(a, b)] \mid a, b \in \mathbb{N} \}").move_to(definition)

        ### Example 1: [(3,1)]
        example1 = MathTex(r"[(3,1)] = \{ (2,0), (3,1), (4,2), (5,3), \dots \}")
        self.play(Write(example1))
        self.wait(1)

        # Show that [(3,1)] represents 2
        result1 = MathTex(r"[(3,1)] = 3 - 1 = \overline{2}").next_to(example1, DOWN)
        
        self.play(Write(result1))
        group1 = VGroup(result1, example1)
        self.wait(2)
        self.play(group1.animate.shift(UP))
    

        # Example 2: [(1,3)]
        example2 = MathTex(r"[(1,3)] = \{ (0,2), (1,3), (2,4), (3,5), \dots \}")
        self.wait(1)
        # Show that [(1,3)] represents -2
        result2 = MathTex(r"[(1,3)] = 1 - 3 = \overline{-2}").next_to(example2, DOWN)

        group2 = VGroup(result2, example2).shift(DOWN)
        self.play(Write(group2))
        self.wait(2)

        self.play(FadeOut(group1, group2))


        # Create a number line from -5 to 5
        number_line = NumberLine(
            x_range=[-5, 5, 1],  # From -5 to 5 with step 1
            length=12,
            include_numbers=True
        )

        self.play(ReplacementTransform(definition, definition3))

        # Add the number line to the scene
        self.play(Write(number_line))
        self.wait(1)

        # Define equivalence class representations for each integer
        equivalence_classes = {
            -5: [r"[(0,5)]", r"[(1,6)]", r"[(2,7)]"],
            -4: [r"[(0,4)]", r"[(1,5)]", r"[(2,6)]"],
            -3: [r"[(0,3)]", r"[(1,4)]", r"[(2,5)]"],
            -2: [r"[(0,2)]", r"[(1,3)]", r"[(2,4)]"],
            -1: [r"[(0,1)]", r"[(1,2)]", r"[(2,3)]"],
             0: [r"[(0,0)]", r"[(1,1)]", r"[(2,2)]"],
             1: [r"[(0,1)]", r"[(1,2)]", r"[(2,3)]"],
             2: [r"[(0,2)]", r"[(1,3)]", r"[(2,4)]"],
             3: [r"[(0,3)]", r"[(1,4)]", r"[(2,5)]"],
             4: [r"[(0,4)]", r"[(1,5)]", r"[(2,6)]"],
             5: [r"[(0,5)]", r"[(1,6)]", r"[(2,7)]"]
        }

        # Add primary labels (first equivalence class) above the number line
        labels = []
        for number, eq_classes in equivalence_classes.items():
            label = MathTex(eq_classes[0], font_size = 32).next_to(number_line.n2p(number), UP)
            if (number % 2 == 0):
                label.set_color(YELLOW)
            else:
                label.set_color(BLUE)
            labels.append(label)

        self.play(*[Write(label) for label in labels])
        self.wait(2)

        group_ = Group(*labels, number_line)
        self.play(group_.animate.shift(DOWN * 1.5))

        # Add second equivalence class representations with delay
        extra_labels1 = []
        for number, eq_classes in equivalence_classes.items():
            label = MathTex(eq_classes[1], font_size = 32).next_to(number_line.n2p(number), UP * 4)
            extra_labels1.append(label)

        self.play(*[Write(label) for label in extra_labels1], run_time=2)
        self.wait(2)

        # Add third equivalence class representations with delay
        extra_labels2 = []
        for number, eq_classes in equivalence_classes.items():
            label = MathTex(eq_classes[2], font_size = 32).next_to(number_line.n2p(number), UP * 7)
            extra_labels2.append(label)

        self.play(*[Write(label) for label in extra_labels2], run_time=2)
        self.wait(2)

        self.play(FadeOut(number_line, *labels, *extra_labels1, *extra_labels2, group_, definition3))
        self.wait(2)
        self.play(FadeOut(title))

class Addition(Scene):
    def construct(self):
        




        
        