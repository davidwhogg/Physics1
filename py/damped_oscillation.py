if __name__ == '__main__':
    import matplotlib
    matplotlib.use('Agg')
    from matplotlib import rc
    rc('font',**{'family':'serif','serif':'Computer Modern Roman','size':12})
    rc('text', usetex=True)
import numpy as np
import pylab as plt

def plotwave(phase, label):
    dtheta = 0.001
    amp = 0.1
    theta = np.arange(0., 4. * np.pi + 0.5 * dtheta, dtheta)
    plt.plot([0., 4. * np.pi], [phase, phase], 'ko')
    plt.plot(theta, phase + np.zeros_like(theta), 'k-', lw=0.5, alpha=0.5)
    plt.plot(theta, phase + amp * np.cos(phase) * np.sin(theta), 'k-', lw=2.)
    plt.text(np.max(theta) + 0.2, phase, label, ha='left', va='center')
    return None

def main(fn):
    times = np.arange(0., 100., 0.05)
    positions = 3.2 * np.exp(-0.05 * times) * np.cos(6. * times + 1.)
    plt.figure(figsize=(6, 2))
    plt.plot(times, positions, "k-")
    plt.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.25)
    plt.xlabel("time (s)")
    plt.ylabel("position (m)")
    plt.savefig(fn)
    return None

if __name__ == '__main__':
    fn = 'damped_oscillation.pdf'
    main(fn)
