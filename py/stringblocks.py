if __name__ == '__main__':
    import matplotlib
    matplotlib.use('Agg')
    from matplotlib import rc
    rc('font',**{'family':'serif','serif':'Computer Modern Roman','size':12})
    rc('text', usetex=True)
import numpy as np
import os as os
import pylab as plt

def drawblock(x, y, size, label):
    px = x + size * np.array([0., 1., 1., 0., 0.])
    py = y + size * np.array([0., 0., 1., 1., 0.])
    plt.plot(px, py, 'k-', lw=3.)
    plt.text(x + 0.5 * size, y + 0.5 * size, label,
             horizontalalignment='center',
             verticalalignment='center')
    return None

def stringblocks(fn):
    plt.figure(figsize=(4, 0.75))
    xo, yo = 0.15, 0.20
    plt.axes([0., 0., 1., 1.])
    tiny = -0.06
    plt.plot([-1., 7.], [tiny, tiny], 'k-', lw=3.)
    drawblock(0., 0., 1., '$m_1$')
    drawblock(4., 0., 1., '$m_2$')
    plt.plot([1., 4.], [0.5, 0.5], 'k-', lw=2.)
    plt.text(2.5, 0.6, '$T$', ha='center')
    plt.gca().add_patch(plt.Arrow(5., 0.5, 1., 0., facecolor='k',
                                  edgecolor='none', alpha=0.5))
    plt.text(6.1, 0.5, '$F$', ha='left', va='center')
    plt.axis('equal')
    plt.axis('off')
    plt.savefig(fn)
    return None

if __name__ == '__main__':
    fn = 'stringblocks.pdf'
    stringblocks(fn)
