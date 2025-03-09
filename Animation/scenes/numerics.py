import manim as m
class scene(m.Scene):
    def construct(self):

        ias15 = m.Text("IAS-15").to_edge(m.LEFT)
        whfast = m.Text("WHFAST").to_edge(m.RIGHT)
        self.play(m.Write(ias15))
        self.play(m.Write(whfast))
        
        self.wait(2)

        source3 = m.Text("Rein, H. and D Tamayo (Sept. 2015). ‘WHFAST: a fast and unbiased implementation of a symplectic Wisdom-Holman integrator for long-term gravitational simulations", font_size = 16).to_edge(m.DOWN)
        source2 = m.Text("Rein, H. and D. S. Spiegel (Jan. 2015). ‘IAS15: a fast, adaptive, high-order integrator for gravitational dynamics, accurate to machine precision over a billion orbits’", font_size = 16).next_to(source3, m.UP)
        source1 = m.Text("Rein, H. and S. -F. Liu (Jan. 2012). ‘REBOUND:an open-source multi-purpose N-body code forcollisional dynamics’", font_size = 16).next_to(source2, m.UP)
        self.play(m.Write(source1))
        self.play(m.Write(source2))
        self.play(m.Write(source3))

        self.wait(2)

        self.play(m.Unwrite(source1))
        self.play(m.Unwrite(source3))
        
        self.wait(2)

        self.play(m.Unwrite(whfast))

        eq1 = m.MathTex(r"\frac{d^2\vec r}{dt^2}", r'=',  r'\frac1m', r'\sum_i \vec F_i ')
        self.play(m.Write(eq1))

        self.wait(2)

        eq2 = m.MathTex(r"\frac{d\vec r}{dt}", r'=',  r'\frac1m', r'\int' + r'\sum_i \vec F_i\ ', r'\ dt')
        
        self.play(m.TransformMatchingTex(eq1, eq2))
        
        self.wait(4)
        
        source3 = m.Text("Rein, H. and D Tamayo (Sept. 2015). ‘WHFAST: a fast and unbiased implementation of a symplectic Wisdom-Holman integrator for long-term gravitational simulations", font_size = 16).to_edge(m.DOWN)
        whfast = m.Text("WHFAST").to_edge(m.UP)
        self.play(
            m.Unwrite(eq2),
            m.Unwrite(ias15),
            m.Unwrite(source2),
            m.Write(whfast),
            m.Write(source3),
        )
        eq1 = m.MathTex(r"H",  r"=", r"H_{Kepler}", r"+", r"H_{Orbiral}", r"+", r"H_{Resonant}", r"+", r"H_{Secular}")
        self.play(m.Write(eq1))

        self.wait(2)

        eq2 = m.MathTex(r"H",  r"=", r"H_{Kepler}", r"+", r"H_{Other \ Planets}", r"+", r"H_{Other \ Effects}")
        self.play(m.Transform(eq1, eq2))

        self.wait(2)

        eq3 = m.MathTex(r"H",  r"=", r"H_{Kepler}").next_to(eq2, m.UP)
        eq4 = m.MathTex(r"H",  r"=", r"H_{Kepler}", r"+", r"H_{GR}").next_to(eq2, m.DOWN)
        self.play(
            m.Write(eq3),
            m.TransformMatchingTex(eq2, eq4),
        )

        self.wait(2)
        
        self.play(
            eq3.animate.set_color(m.ORANGE),
            eq4.animate.set_color(m.BLUE),
        )

        self.wait(2)
        self.play(
            m.Unwrite(eq1),
            m.Unwrite(eq2)
        )
        self.wait(2)



        