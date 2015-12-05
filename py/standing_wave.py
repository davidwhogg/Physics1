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
    plt.figure(figsize=(4, 4))
    plt.axes([0., 0., 1., 1.])
    phases = np.arange(0., 7., np.pi/8)
    for i, phase in enumerate(phases):
        plotwave(phase, chr(85-i))
    plt.axis('off')
    plt.xlim(-0.2, 13.3)
    print plt.ylim(-0.13, 2. * np.pi + 0.13)
    plt.savefig(fn)
    return None

if __name__ == '__main__':
    fn = 'standing_wave.pdf'
    main(fn)
