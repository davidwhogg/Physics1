if __name__ == '__main__':
    import matplotlib
    matplotlib.use('Agg')
    from matplotlib import rc
    rc('font',**{'family':'serif','serif':'Computer Modern Roman','size':12})
    rc('text', usetex=True)
import numpy as np
import pylab as plt

def com_shape(fn):
    plt.figure(figsize=(4, 4))
    plt.clf()
    plt.plot([1., 1., 3., 3., 5., 5., 1.],
             [1., 7., 7., 3., 3., 1., 1.], 'k-', lw=3.)
    plt.grid(True, alpha=0.5)
    plt.xlabel(r'$x$ (cm)')
    plt.ylabel(r'$y$ (cm)')
    plt.axis('equal')
    plt.xlim(-1., 8.)
    plt.ylim(-1., 8.)
    plt.savefig(fn)
    return None

if __name__ == '__main__':
    fn = 'com_shape.pdf'
    com_shape(fn)
