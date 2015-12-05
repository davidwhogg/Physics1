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
    t  = [  0., 3./10., 6./10.,   1.]
    vA = [  3.,     0.,    -3.,  -7.]
    vB = [  3.,     0.,     3.,   7.]
    vC = [-10.,   -10.,   -10., -10.]
    vD = [  3.,     3.,     3.,   3.]
    vs = [vA, vB, vC, vD]
    label = [r'\bf A', r'\bf B', r'\bf C', r'\bf D']
    dt = 0.001
    tp = np.arange(-5., 70., dt)
    plt.figure(figsize=(4, 4))
    plt.subplots_adjust(top=0.98, left=0.15, right=0.98)
    for fig in range(4):
        plt.subplot(2, 2, fig+1)
        plt.plot(t, vs[fig], 'k-', lw=2.)
        plt.xlim(0., 1.)
        plt.ylim(-11., 11.)
        plt.text(0.02, 5., label[fig])
        if fig in [2, 3]:
            plt.xlabel(r'time $t$ (s)')
        if fig in [0, 2]:
            plt.ylabel(r'velocity $v_y$ (m\,s$^{-1}$)')
    plt.savefig(fn)
    return None

if __name__ == '__main__':
    fn = 'vy_vs_t_options.pdf'
    vx_vs_t(fn)
