import manim as m

class scene(m.ThreeDScene):
    def construct(self):
        text = m.Text("https://github.com/theSecondBlueWizard/Astrobites-project", font_size = 24)
        self.play(m.Write(text))
        self.play(m.Unwrite(text))