import manim as m
from lib.orbit_calculations import *
import lib.scene_setup as scene

class PlotOrbit(m.ThreeDScene):
    def construct(self):
        a = m.ValueTracker(1)
        e = m.ValueTracker(0)
        w = m.ValueTracker(0)
        i = m.ValueTracker(0)
        W = m.ValueTracker(np.pi/2)

        orbit = scene.make_orbit(a, e, w, i, W)
        self.play(m.Create(orbit))

        sun = m.Sphere(radius = 0.1).set_color(m.YELLOW)
        self.play(m.Create(sun))
        self.play(m.Uncreate(sun))
        self.wait(1)
        
        a_line, a_label, _, a_temp = scene.make_a_objects(a, e, w, i, W)
        b_line, b_label, _, b_temp = scene.make_b_objects(a, e, w, i, W)

        self.wait()

        self.play(m.Create(a_line, run_time = 0.5))
        self.play(m.Write(a_label, run_time = 0.2))

        self.play(m.Create(b_line, run_time = 0.5))
        self.play(m.Write(b_label, run_time = 0.2))
        
        self.wait(2)

        self.play(a.animate.set_value(1.3))
        self.play(e.animate.set_value(0.5), run_time = 2)
        
        self.wait(1)
        _, _, a_display, _ = scene.make_a_objects(a, e, w, i, W)
        _, _, b_display, _ = scene.make_b_objects(a, e, w, i, W)
        
        self.play(
            m.Transform(a_label, a_temp.to_corner(m.UL)),
            m.Transform(b_label, b_temp.next_to(a_temp, m.DOWN)),
            m.Write(a_display.to_corner(m.UL)),
            m.Write(b_display.next_to(a_display, m.DOWN))
        )
        self.remove(a_label, b_label, a_temp, b_temp)

        self.wait(1)

        self.play(
            e.animate.set_value(0.9),
            a.animate.set_value(2)
        )

        self.wait(1)

        self.play(
            e.animate.set_value(0.5),
            a.animate.set_value(1)
        )

        self.play(
            m.Uncreate(a_line, runtime = 0.2),
            m.Uncreate(b_line, runtime = 0.2)
        )

        self.wait()
        
        sun = m.Sphere(radius = 0.1).set_color(m.YELLOW)

        self.play(
            m.Create(sun)
        )
        
        ra_line, ra_label, _, ra_temp = scene.make_ra_objects(a, e, w, i, W)
        rp_line, rp_label, _, rp_temp = scene.make_rp_objects(a, e, w, i, W)

        self.play(m.Create(rp_line, run_time = 0.5))
        self.play(m.Write(rp_label, run_time = 0.2))

        self.play(m.Create(ra_line, run_time = 0.5))
        self.play(m.Write(ra_label, run_time = 0.2))

        self.wait(1)
        
        self.play(
            e.animate.set_value(0.5),
            a.animate.set_value(2)
        )

        self.play(
            e.animate.set_value(0.9),
            a.animate.set_value(2.5)
        )
        
        self.play(
            e.animate.set_value(0.5),
            a.animate.set_value(2)
        )
        
        _, _, ra_display, _ = scene.make_ra_objects(a, e, w, i, W)
        _, _, rp_display, _ = scene.make_rp_objects(a, e, w, i, W)

        self.play(
            m.TransformMatchingTex(ra_label, ra_temp.next_to(b_temp, m.DOWN)),
            m.TransformMatchingTex(rp_label, rp_temp.next_to(ra_temp, m.DOWN)),
            m.Write(ra_display.next_to(b_display, m.DOWN)),
            m.Write(rp_display.next_to(ra_display, m.DOWN))
        )
        self.remove(ra_label, rp_label, ra_temp, rp_temp)

        eccentricity_equation = m.MathTex(r"e",  r" = \sqrt{1 - \frac{b^2}{a^2}} = \frac{r_a - r_p}{r_a + r_p}")
        self.play(
            m.Write(eccentricity_equation.to_edge(m.LEFT))
        )

        self.wait(4)
        e_display, e_temp = scene.make_e_objects(e)

        self.play(
            m.TransformMatchingTex(eccentricity_equation, e_temp.next_to(rp_temp, m.DOWN)),
            m.Write(e_display.next_to(rp_display, m.DOWN)),
        )
        self.remove(eccentricity_equation, e_temp)
        
        self.wait(1)
        self.play(
            rp_display.animate.set_color(m.YELLOW),
            a_display.animate.set_color(m.YELLOW),
        )
        self.wait(1)
        self.play(
            rp_display.animate.set_color(m.WHITE),
            a_display.animate.set_color(m.WHITE),
            b_display.animate.set_color(m.PURPLE),
            e_display.animate.set_color(m.PURPLE),
        )
        self.wait(1)
        self.play(
            b_display.animate.set_color(m.WHITE),
            e_display.animate.set_color(m.WHITE),
            a_display.animate.set_color(m.GREEN),
            ra_display.animate.set_color(m.GREEN),
        )
        self.wait(1)
        self.play(
            ra_display.animate.set_color(m.WHITE),
            e_display.animate.set_color(m.GREEN),
        )

        self.wait(2)

        self.play(
            m.Unwrite(b_display),
            m.Unwrite(ra_display),
            m.Unwrite(rp_display),
            e_display.animate.set_color(m.WHITE),
            a_display.animate.set_color(m.WHITE),
        )
        self.play(
            m.Uncreate(ra_line),
            e_display.animate.next_to(a_display, m.DOWN)
        )

        self.wait(2)

        _, rp_label, asc_node_arrow, w_display = scene.make_w_objects(a, e, w, i, W)
        
        self.play(
            m.Create(asc_node_arrow),
            m.Write(rp_label),
            m.Write(w_display.next_to(e_display, m.DOWN))
        )
        self.wait(2)

        self.play(
            w.animate.set_value(np.pi),
        )
        self.wait(2)

        self.play(
            w.animate.set_value(np.pi / 2),
        )

        self.wait(4)

        self.move_camera(phi = 1, theta = -1)
        self.play(a_display.animate.to_edge(m.LEFT),)
        self.play(e_display.animate.next_to(a_display, m.DOWN))
        self.play(w_display.animate.next_to(e_display, m.DOWN),)

        self.play(
            a.animate.set_value(3),
            w.animate.set_value(3 * np.pi / 2),
            m.Uncreate(asc_node_arrow),
            m.Unwrite(rp_label),
            m.Uncreate(rp_line),
        )

        i_arrow, i0_arrow, i_display = scene.make_i_objects(i, W)

        self.play(
            m.Create(i_arrow),
            m.Create(i0_arrow),
            m.Write(i_display.next_to(w_display, m.DOWN))
        )

        self.play(i.animate.set_value(m.PI/4), runtime = 8)
        self.play(i.animate.set_value(3 * m.PI / 2), runtime = 8)
        self.play(i.animate.set_value(m.PI / 4), runtime = 8)
        self.play(
            w.animate.set_value(m.PI/3),
            W.animate.set_value(3 * np.pi / 2),
            m.Uncreate(i_arrow),
            m.Uncreate(i0_arrow),
        )

        asc_node, equinnox, W_display = scene.make_W_objects(a, e, w, W)
        self.play(
            m.Write(W_display.next_to(i_display, m.DOWN)),
            m.Create(asc_node),
            m.Create(equinnox),
        )

        t = m.ValueTracker(0)
        body = m.always_redraw(lambda: m.Sphere(radius = 0.1).move_to(generate_orbit_equation(a, e, w, i, W)(t.get_value())))

        self.wait(3)
        self.play(m.Create(body))
        self.play(t.animate.set_value(-2))
        self.play(t.animate.set_value(-3))
        self.play(t.animate.set_value(-2 * np.pi))
        self.play(m.Uncreate(body))
        self.wait(3)


        self.play(W.animate.set_value(m.PI), runtime = 8)
        self.play(
            m.Uncreate(equinnox),
            i.animate.set_value(1),
            W.animate.set_value(3 * np.pi / 2),
            e.animate.set_value(0.75),
        )
        rp_line, rp_label, _, _, scene.make_rp_objects(a, e, w, i, W)
        self.play(
            m.Uncreate(equinnox),
            m.Create(rp_line),
            m.Create(rp_label),
        )
        self.play(w_display.animate.set_color(m.RED))
        self.play(w_display.animate.set_color(m.WHITE))
        self.play(w_display.animate.set_color(m.RED))
        self.play(w_display.animate.set_color(m.WHITE))
        self.play(w.animate.set_value(0))
        self.wait(1)
        self.play(w.animate.set_value(1))
        self.play(w.animate.set_value(2))
        self.play(w.animate.set_value(3))
        self.play(w.animate.set_value(4))
        self.wait(1)
        self.play(
            e.animate.set_value(0),
            m.Unwrite(rp_label),
            m.Uncreate(rp_line),
            m.Uncreate(asc_node)
        )
        self.play(m.Unwrite(a_display))
        self.play(m.Unwrite(e_display))
        self.play(m.Unwrite(i_display))
        self.play(m.Unwrite(W_display))
        self.play(m.Unwrite(w_display))
        self.play(a.animate.set_value(0))
        self.play(m.Uncreate(sun))

        self.wait(1)
