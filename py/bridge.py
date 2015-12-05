if __name__ == '__main__':
    import matplotlib
    matplotlib.use('Agg')
    from matplotlib import rc
    rc('font',**{'family':'serif','serif':'Computer Modern Roman','size':12})
    rc('text', usetex=True)
import numpy as np
import pylab as plt

lw_default = 2.

def beam(x, y, theta, lw=lw_default):
    xp = np.array([0., 0.1, 0.9, 1.0,  0.9, 0.1, 0.])
    thick = 0.08
    yp = thick * 0.5 * np.array([0., 1., 1., 0., -1., -1., 0.])
    ct = np.cos(np.deg2rad(theta))
    st = np.sin(np.deg2rad(theta))
    plt.plot(x + xp * ct - yp * st, y + xp * st + yp * ct, 'k-', lw=lw_default)
    plt.plot([x, x + ct], [y, y + st], 'ko', mec='none', mfc='k', ms=10)
    return None

def bridge(fn):
    plt.figure(figsize=(4, 2))
    plt.axes([0., 0., 1., 1.])
    plt.fill([-0.5, 0.,  0.,   2.,  2., 2.5, 2.5, -0.5, -0.5],
             [ 0.,  0., -0.5, -0.5, 0., 0., -0.6, -0.6,  0.], 'k-', alpha=0.5)
    beam(0., 0., 0.)
    beam(0., 0., 60.)
    beam(1., 0., 120.)
    beam(1., 0., 0.)
    beam(1., 0., 60.)
    beam(2., 0., 120.)
#    beam(2., 0., 0.)
#    beam(2., 0., 60.)
#    beam(3., 0., 120.)
    yt = np.sin(np.deg2rad(60))
    beam(0.5, yt, 0.)
#    beam(1.5, yt, 0.)
    plt.axis('equal')
    plt.axis('off')
    plt.savefig(fn)
    return None

if __name__ == '__main__':
    fn = 'bridge.pdf'
    bridge(fn)
