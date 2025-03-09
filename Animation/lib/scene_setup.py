import manim as m
from lib.orbit_calculations import *

def make_orbit(a, e, w, i, W):
    def orbit_equation():
        func = generate_orbit_equation(a, e, w, i, W)
        return func
    
    def orbit_parametric_func():
        parametric_func = m.ParametricFunction(
            orbit_equation(),
            t_range = (0, m.TAU),
            fill_opacity = 0,
            color = m.RED,
        ).set_shade_in_3d(True)
        return parametric_func
    return m.always_redraw(orbit_parametric_func)

def make_a_objects(a, e, w, i, W):
    def a_line():
        line = m.Line(
                get_centre(a, e, w, i, W),
                get_semimajor_vec(a, e, w, i, W),
                color = m.PURPLE
            )
        return line
    
    def a_label():
        label_position = get_incremented_semimajor_vec(a, e, w, i, W)
        label = m.MathTex("a", font_size = 56).move_to(label_position)
        return label
    
    a_display = m.Variable(
            a.get_value(),
            m.MathTex("a", font_size = 56),
            num_decimal_places = 3
        )
    a_display.add_updater(
            lambda x: x.tracker.set_value(
                a.get_value()
            )
        )
    
    a_static_label = m.MathTex("a", font_size = 56)
    
    return m.always_redraw(a_line), m.always_redraw(a_label), a_display, a_static_label

def make_b_objects(a, e, w, i, W):
    def b_line():
        line = m.Line(
                get_centre(a, e, w, i, W),
                get_semiminor_vec(a, e, w, i, W),
                color = m.PURPLE
            )
        return line
    
    def b_label():
        label_position = get_incremented_semiminor_vec(a, e, w, i, W)
        label = m.MathTex("b", font_size = 56).move_to(label_position)
        return label

    b_display = m.Variable(
            calculate_b(a, e),
            m.MathTex("b", font_size = 56),
            num_decimal_places = 3
        )
    
    b_display.add_updater(
            lambda x: x.tracker.set_value(calculate_b(a, e))
        )
    b_static_label = m.MathTex("b", font_size = 56)
    
    return m.always_redraw(b_line), m.always_redraw(b_label), b_display, b_static_label

def make_ra_objects(a, e, w, i, W):
    def ra_line():
        line = m.Line(
            [0,0,0], get_apoapsis_vec(a, e, w, i, W), color = m.GREEN
        )
        return line

    def ra_label():
        label_position = get_incremented_apoapsis_vec(a, e, w, i, W)
        label = m.MathTex("r_a", font_size = 56).move_to(label_position)
        return label
    
    ra_display = m.Variable(
            calculate_ra(a, e),
            m.MathTex("r_a", font_size = 56),
            num_decimal_places = 3
        )
    ra_display.add_updater(
        lambda x: x.tracker.set_value(calculate_ra(a, e))
    )

    ra_static_label = m.MathTex("r_a", font_size = 56)
    
    return m.always_redraw(ra_line), m.always_redraw(ra_label), ra_display, ra_static_label

def make_rp_objects(a, e, w, i, W):
    def rp_line():
        line = m.Line(
            [0,0,0], get_periapsis_vec(a, e, w, i, W), color = m.BLUE
        )
        return line

    def rp_label():
        label_positon = get_incremented_periapsis_vec(a, e, w, i, W)
        label = m.MathTex("r_p", font_size = 56).move_to(label_positon)
        return label
    
    rp_display = m.Variable(
        calculate_rp(a, e),
        m.MathTex("r_p", font_size = 56),
        num_decimal_places = 3
    )
    rp_display.add_updater(
        lambda x: x.tracker.set_value(calculate_rp(a, e))
    )

    rp_static_label = m.MathTex("r_p", font_size = 56)
    
    return m.always_redraw(rp_line), m.always_redraw(rp_label), rp_display, rp_static_label

def make_e_objects(e):
    e_display = m.Variable(
        e.get_value(),
        m.MathTex("e", font_size = 56),
        num_decimal_places = 3
    )
    e_display.add_updater(
        lambda x: x.tracker.set_value(e.get_value())
    )
    e_static_label = m.MathTex("e", font_size = 56)
    return e_display, e_static_label

def make_w_objects(a, e, w, i, W):
    def rp_arrow():
        rp_vec = get_periapsis_vec(a, e, w, i, W)
        arrow = m.Arrow(
            [0,0,0], rp_vec / np.linalg.norm(rp_vec), color = m.BLUE
        )
        return arrow

    def rp_label():
        label_positon = get_incremented_periapsis_vec(a, e, w, i, W)
        label = m.MathTex("r_p", font_size = 56).move_to(label_positon)
        return label
    
    def asc_node():
        arrow = m.Arrow([0,0,0], get_ascending_vec(a, e, w, W), color = m.PINK)
        return arrow
    
    w_display = m.Variable(
        w.get_value(),
        m.MathTex("\omega", font_size = 56),
        num_decimal_places = 3
    )
    w_display.add_updater(
        lambda x: x.tracker.set_value(w.get_value())
    )
    return m.always_redraw(rp_arrow), m.always_redraw(rp_label), m.always_redraw(asc_node), w_display 


def make_i_objects(i, W):
    def i_arrow():
        i_vec = get_inclination_vec(i, W)
        arrow = m.Arrow(
            [0,0,0], i_vec, color = m.BLUE
        )
        return arrow
    
    def i0_arrow():
        i_vec = get_inclination_vec(i, W)
        i_vec[2] = 0
        arrow = m.Arrow(
            [0,0,0], i_vec, color = m.BLUE
        )
        return arrow
        
    i_display = m.Variable(
        i.get_value(),
        m.MathTex("i", font_size = 56),
        num_decimal_places = 3
    )
    i_display.add_updater(
        lambda x: x.tracker.set_value(i.get_value())
    )
    return m.always_redraw(i_arrow), m.always_redraw(i0_arrow), i_display
    
def make_W_objects(a, e, w, W):
    def asc_node():
        arrow = m.Arrow([0,0,0], get_ascending_vec(a, e, w, W), color = m.PINK)
        return arrow
    
    def equinnox():
        arrow = m.Arrow([0,0,0], [1, 0, 0], color = m.GREY)
        return arrow
    
    W_display = m.Variable(
        W.get_value(),
        m.MathTex("\Omega", font_size = 56),
        num_decimal_places = 3
    )
    W_display.add_updater(
        lambda x: x.tracker.set_value(W.get_value())
    )
    return m.always_redraw(asc_node), m.always_redraw(equinnox), W_display 