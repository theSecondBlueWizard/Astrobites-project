import rebound
import numpy as np
import manim as m

def progressBar(progress: int, total: int, len: int) -> str:
    scaledProgress = round(progress / total * (len))
    return '[' + ('#' * scaledProgress) + ('-' * (len - scaledProgress)) + ']' +  str(progress) + '/' + str(total)

class ParticleAnimationWithSlowC(m.Scene):

    def read_positions(self, file):
        # N = 310_000
        N = 31_000
        dt = 2
        mercury_vec = []
        for i in range(0, N, dt):
            if not i % 100:
                print(progressBar(i, N, 20))
            xyz = rebound.Simulation(file, snapshot=int(i)).particles[1]
            mercury_vec.append(np.array([xyz.x, xyz.y, xyz.z], dtype=np.float64))

        return mercury_vec

    def construct(self):
        mercury_w_GR_vecs = self.read_positions("mercury_w_GR.bin")
        mercury_wo_GR_vecs = self.read_positions("mercury_wo_GR.bin")

        # Create a Dot at the starting position.
        particle_w_GR = m.Dot(point=mercury_w_GR_vecs[1], color = m.BLUE)
        particle_wo_GR = m.Dot(point=mercury_wo_GR_vecs[1], color = m.ORANGE)

        traced_particle_w_GR = m.TracedPath(
            particle_w_GR.get_center,
            dissipating_time = 5,
            stroke_opacity = [1,0],
            color = m.BLUE
        )
        traced_particle_wo_GR = m.TracedPath(
            particle_wo_GR.get_center,
            dissipating_time = 5,
            stroke_opacity = [1,0],
            color = m.ORANGE
        )
        self.add(
            traced_particle_w_GR,
            traced_particle_wo_GR,
            particle_w_GR,
            particle_wo_GR,
        )
        self.add(m.Sphere(radius = 0.1).set_color(m.YELLOW))

        # A ValueTracker to move through indices of positions.
        tracker = m.ValueTracker(0)

        def update_particle_w_GR(mob):
            index = int(tracker.get_value())
            index = min(index, len(mercury_w_GR_vecs) - 1)
            mob.move_to(5 * mercury_w_GR_vecs[index])

        def update_particle_wo_GR(mob):
            index = int(tracker.get_value())
            index = min(index, len(mercury_wo_GR_vecs) - 1)
            mob.move_to(5 * mercury_wo_GR_vecs[index])
        
        # Add the updater to the particle.
        particle_w_GR.add_updater(update_particle_w_GR)
        particle_wo_GR.add_updater(update_particle_wo_GR)

        # Animate the tracker from 0 to the last index.
        self.play(tracker.animate.set_value(len(mercury_wo_GR_vecs) - 1), run_time=20, rate_func=m.linear)

        particle_w_GR.remove_updater(update_particle_w_GR)
        # Clean up the updater.
        particle_wo_GR.remove_updater(update_particle_wo_GR)