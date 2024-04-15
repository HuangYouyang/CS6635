from Halo_loader import Halo
from particle_loader import particleSDF
import matplotlib.pylab as plt
from matplotlib.animation import FuncAnimation


def update(frame, ax, particles_x_array, particles_y_array, particles_z_array, halo_x_array, halo_y_array, halo_z_array, twoD):
    particles_x = particles_x_array[frame]
    particles_y = particles_y_array[frame]
    particles_z = particles_z_array[frame]

    halo_x = halo_x_array[frame]
    halo_y = halo_y_array[frame]
    halo_z = halo_z_array[frame]

    ax.clear()
    ax.set_xlabel('x [cMpc/h]')
    ax.set_ylabel('y [cMpc/h]')
    if twoD:
        ax.set_title('2D Projection of Particle Density')
    else:
        ax.set_title('3D Projection of Particle Density')
    if twoD:
        ax.scatter(particles_x, particles_y, color='b', s=1.0, alpha=0.05)
        ax.scatter(halo_x, halo_y, color='r', alpha=0.1)
    else:
        ax.set_ylabel('z [cMpc/h]')
        ax.scatter(particles_x, particles_y, particles_z, color='b', s=1.0, alpha=0.05)
        ax.scatter(halo_x, halo_y, halo_z, color='r', alpha=0.1)

    return ax


def particle_density_2d(startT, endT, animation=False, save=True, twoD=True):
    prefix = "../../project/data/ds14_scivis_0128/"

    particles_x_array = []
    particles_y_array = []
    particles_z_array = []
    halo_x_array = []
    halo_y_array = []
    halo_z_array = []

    time = startT
    S = int(startT * 100)
    E = int(endT * 100) + 1

    # read the data
    for i in range(S, E):
        # particle data
        time += 0.01
        filenameParticle = prefix + "ds14_scivis_0128_e4_dt04_{0:.2f}00".format(time)
        particle = particleSDF(filenameParticle)

        particles_x = particle.PositionsOffset.T[0]
        particles_y = particle.PositionsOffset.T[1]
        particles_z = particle.PositionsOffset.T[2]

        particles_x_array.append(particles_x)
        particles_y_array.append(particles_y)
        particles_z_array.append(particles_z)

        print("Finish reading " + filenameParticle)

        # halo data
        filenameHalo = prefix + "rockstar/hlists/hlist_{0:.2f}000.list".format(time)
        haloData = Halo(filenameHalo)

        halo_x = haloData.position.T[0]
        halo_y = haloData.position.T[1]
        halo_z = haloData.position.T[2]

        halo_x_array.append(halo_x)
        halo_y_array.append(halo_y)
        halo_z_array.append(halo_z)

        print("Finish reading " + filenameHalo)

    if animation:
        fig, ax = plt.subplots(figsize=[10, 10])

        # animation
        if twoD:
            ani = FuncAnimation(fig, update, frames=len(particles_x_array),
                                fargs=(ax, particles_x_array, particles_y_array, particles_z_array, halo_x_array, halo_y_array, halo_z_array, twoD),
                                interval=200, blit=False)
            saveDir = "../output/particle_density_2d.gif"
        else:
            ax = fig.add_subplot(111, projection="3d")
            ani = FuncAnimation(fig, update, frames=len(particles_x_array),
                                fargs=(ax, particles_x_array, particles_y_array, particles_z_array, halo_x_array, halo_y_array, halo_z_array, twoD),
                                interval=200, blit=False)
            saveDir = "../output/particle_density_3d.gif"

        if save:
            ani.save(saveDir)
            print("Finish saving " + saveDir)

        # plt.show()
    else:
        for i in range(len(particles_x_array)):
            fig = plt.figure(figsize=[10, 10])

            if twoD:
                plt.scatter(particles_x_array[i],
                            particles_y_array[i], color='b', s=1.0, alpha=0.05)

                plt.scatter(halo_x_array[i], halo_y_array[i], color='r', alpha=0.1)

                plt.xlabel('x [cMpc/h]')
                plt.ylabel('y [cMpc/h]')

                saveDir = "../output/particle_density_2d_{0}.png".format(i)
            else:
                fig.patch.set_facecolor('0.2')
                ax = fig.add_subplot(111, projection="3d")
                ax.scatter(particles_x_array[i],
                            particles_y_array[i],
                            particles_z_array[i], color='white', s=0.05, alpha=0.05)

                ax.scatter(halo_x_array[i], halo_y_array[i], halo_z_array[i], color='b', alpha=0.1)
                ax.patch.set_facecolor('0.2')

                ax.set_xlabel('x [cMpc/h]', color="white")
                ax.set_ylabel('y [cMpc/h]', color="white")
                ax.set_title('3D Projection of Particle Density', color="white")
                ax.tick_params(axis='x', colors='white')
                ax.tick_params(axis='y', colors='white')
                ax.tick_params(axis='z', colors='white')

                saveDir = "../output/particle_density_3d_{0}.png".format(i)

            if save:
                plt.savefig(saveDir, bbox_inches='tight')
                print("Finish saving" + saveDir)

            # plt.show()


if __name__ == '__main__':
    particle_density_2d(0.99, 0.99, animation=False, save=True, twoD=False)
