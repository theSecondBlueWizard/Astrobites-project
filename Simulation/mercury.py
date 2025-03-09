import numpy as np
from matplotlib import pyplot as plt
import rebound

import reboundx
from reboundx import constants

sim = rebound.simulation.Simulation()
sim.move_to_com()
sim.integrator = "WHFAST"
sim.dt = 1e-4

sim.add("Sun")
sim.add("Mercury")
# sim.add("Venus")
# sim.add("Earth")
# sim.add("Mars")
# sim.add("Jupiter")
# sim.add("Saturn")
# sim.add("Uranus")
# sim.add("Neptune")

x = sim.particles[1].pomega

rebx = reboundx.Extras(sim)
gr = rebx.load_force("gr")
rebx.add_force(gr)
gr.params["c"] = constants.C / 100

sim.save_to_file("./mercury_w_GR.bin", step = 10)
sim.integrate(10 * 2 * np.pi) # 50 years
# print((np.rad2deg(sim.particles[1].pomega - x) - int(np.rad2deg(sim.particles[1].pomega - x))) * 3600)
# sim.cite()
