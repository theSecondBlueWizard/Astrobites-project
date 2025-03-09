import manim as m

class TitleSequence(m.Scene):
    def construct(self):
        title_text_1 = m.Text("Brief Overview of Modern")
        title_text_2 = m.Text("Orbital Modelling Using")
        title_text_3 = m.Text("REBOUND")
        for letter in title_text_3:
            letter.set_color(m.random_bright_color())

        title_card = m.VGroup(title_text_1, title_text_2, title_text_3)

        self.play(m.Write(title_card.arrange(m.DOWN)))
        self.wait(2)
        self.play(m.FadeOut(title_card))