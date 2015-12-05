if __name__ == '__main__':
    import matplotlib
    matplotlib.use('Agg')
    from matplotlib import rc
    rc('font',**{'family':'serif','serif':'Computer Modern Roman','size':12})
    rc('text', usetex=True)
import numpy as np
import os as os
import pylab as plt

def vx_vs_t(fn):
    t = [-5., 0., 10., 30., 35., 55., 65., 70.]
    vx = [0., 0., 15., 15.,  5.,  5.,  0.,  0.]
    plt.figure(figsize=(4, 2))
    xo, yo = 0.15, 0.20
    plt.axes([xo, yo, 0.98-xo, 0.96-yo])
    plt.plot(t, vx, 'k-', lw=3.)
    plt.grid(True, alpha=0.5)
    plt.xlim(-5., 70.)
    plt.ylim(-5., 20.)
    plt.xlabel(r'time $t$ (s)')
    plt.ylabel(r'velocity $v_x$ (m\,s$^{-1}$)')
    plt.savefig(fn)
    return None

if __name__ == '__main__':
    fn = 'vx_vs_t.pdf'
    vx_vs_t(fn)
