import numpy as np

text_offset_unit = 0.5

def rot_mat_x(t):
    mat = np.array([
        [1, 0        ,  0        ],
        [0, np.cos(t), -np.sin(t)],
        [0, np.sin(t),  np.cos(t)],
    ])
    return mat

def rot_mat_y(t):
    mat = np.array([
        [ np.cos(t), 0, np.sin(t)],
        [ 0        , 1, 0        ],
        [-np.sin(t), 0, np.cos(t)],
    ])
    return mat

def rot_mat_z(t):
    mat = np.array([
        [np.cos(t), -np.sin(t), 0],
        [np.sin(t),  np.cos(t), 0],
        [0        ,  0        , 1],
    ])
    return mat

def calculate_b(a, e):
    return a.get_value() * np.sqrt(1 - e.get_value() ** 2)

def calculate_ra(a, e):
    return a.get_value() * (1 + e.get_value())

def calculate_rp(a, e):
    return a.get_value() * (1 - e.get_value())

def generate_orbit_equation(a, e, w, i, W):
    def orbit_equation(t):
        r = np.array([                                      # Note the cursed coordinates.
            calculate_b(a, e) * np.sin(t),                  #  These are there so that the
            a.get_value() * (e.get_value() + np.cos(t)),    #  logic adds up with right hand
            0,                                              #  rule. Not prety, but it works,
        ])                                                  #  unfortunately
        R_W = rot_mat_z(-W.get_value())
        R_i = rot_mat_y(-i.get_value())
        R_w = rot_mat_z(w.get_value())
        return R_W @ R_i @ R_w @ r
    return orbit_equation

def get_apoapsis_vec(a, e, w, i, W):
    r = np.array([0, calculate_ra(a, e), 0])
    R_W = rot_mat_z(-W.get_value())
    R_i = rot_mat_y(-i.get_value())
    R_w = rot_mat_z(w.get_value())
    return R_W @ R_i @ R_w @ r

def get_incremented_apoapsis_vec(a, e, w, i, W):
    apoapsis_vec = get_apoapsis_vec(a, e, w, i, W)
    unit_apoapsis_vec = apoapsis_vec / np.linalg.norm(apoapsis_vec)
    return apoapsis_vec + text_offset_unit * unit_apoapsis_vec

def get_periapsis_vec(a, e, w, i, W):
    r = np.array([0, calculate_rp(a, e), 0])
    R_W = rot_mat_z(-W.get_value())
    R_i = rot_mat_y(-i.get_value())
    R_w = rot_mat_z(w.get_value())
    return -R_W @ R_i @ R_w @ r

def get_incremented_periapsis_vec(a, e, w, i, W):
    periapsis_vec = get_periapsis_vec(a, e, w, i, W)
    unit_periapsis_vec = periapsis_vec / np.linalg.norm(periapsis_vec)
    return periapsis_vec + text_offset_unit * unit_periapsis_vec

def get_centre(a, e, w, i, W):
    return (get_apoapsis_vec(a, e, w, i, W) + get_periapsis_vec(a, e, w, i, W)) / 2

def get_focus(a, e, w, i, W):
    return 2 * get_centre(a, e, w, i, W)

def get_normal(i, W):
    normal = np.array([
        -np.sin(i.get_value()) * np.cos(W.get_value()),
        np.sin(i.get_value()) * np.sin(W.get_value()),
        np.cos(i.get_value())
    ])
    return normal

def get_semimajor_vec(a, e, w, i, W):
    return get_apoapsis_vec(a, e, w, i, W)

def get_incremented_semimajor_vec(a, e, w, i, W):
    return get_incremented_apoapsis_vec(a, e, w, i, W)

        
def get_semiminor_vec(a, e, w, i, W):
    b = calculate_b(a, e)
    centre = get_centre(a, e, w, i, W)
    major_direction = get_apoapsis_vec(a, e, w, i, W) - get_focus(a, e, w, i, W)
    unit_major_direction = major_direction / np.linalg.norm(major_direction)
    return centre + b * np.cross(get_normal(i, W), unit_major_direction)

def get_incremented_semiminor_vec(a, e, w, i, W):
    centre = get_centre(a, e, w, i, W)
    semiminor_vec = get_semiminor_vec(a, e, w, i, W) - centre
    unit_seminimor_vec = semiminor_vec / np.linalg.norm(semiminor_vec)
    return centre + semiminor_vec + text_offset_unit * unit_seminimor_vec

def get_ascending_vec_norm(W):
    _W = W.get_value()
    return [np.sin(-_W), -np.cos(-_W), 0]

def get_ascending_vec(a, e, w, W):
    _a = a.get_value()
    _e = e.get_value()
    f_asc = -w.get_value()
    r_asc = _a * (1 - _e ** 2) / (1 + _e * np.cos(f_asc))
    direction = get_ascending_vec_norm(W)
    return r_asc * np.array(direction)

def get_inclination_vec(i, W):
    orbital_norm = get_normal(i, W)
    ascending_vec_norm = get_ascending_vec_norm(W)
    return np.cross(orbital_norm, ascending_vec_norm)
