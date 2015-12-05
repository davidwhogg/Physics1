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
    t  = [-5., 0., 0., 10., 10., 30., 30., 35., 35., 55., 55., 65., 70.]
    vA = [ 0., 0.,1.5, 0.0, 1.5, 1.5, 3.0, 0.0, 0.5, 0.5, 1.0,  0.,  0.]
    vB = [ 0., 0., 0., 4.0, 1.5, 1.5, 3.0, 0.0, 0.5, 0.5, 1.0,  0.,  0.]
    vC = [ 0., 0., 0., 1.5, 1.5, 1.5, 1.5, 0.0, 0.0, 0.0, 0.0,  0.,  0.]
    vD = [ 0., 0., 0., 1.5, 1.5, 1.5, 1.5, 0.0, 1.5, 0.5, 0.5,  0.,  0.]
    vs = [vA, vB, vC, vD]
    label = [r'\bf A', r'\bf B', r'\bf C', r'\bf D']
    dt = 0.001
    tp = np.arange(-5., 70., dt)
    plt.figure(figsize=(4, 4))
    plt.subplots_adjust(top=0.98, right=0.98)
    for fig in range(4):
        plt.subplot(2, 2, fig+1)
        vp = np.interp(tp, t, vs[fig])
        xp = np.cumsum(vp * dt)
        plt.plot(tp, xp, 'k-', lw=2.)
        plt.xlim(-5., 45.)
        plt.xticks([0, 10, 20, 30, 40])
        plt.ylim(-5., 60.)
        plt.text(0., 45., label[fig])
        if fig in [2, 3]:
            plt.xlabel(r'time $t$ (s)')
        if fig in [0, 2]:
            plt.ylabel(r'position $x$ (m)')
    plt.savefig(fn)
    return None

if __name__ == '__main__':
    fn = 'x_vs_t_options.pdf'
    vx_vs_t(fn)
