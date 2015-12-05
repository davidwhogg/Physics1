if __name__ == '__main__':
    import matplotlib
    matplotlib.use('Agg')
    from matplotlib import rc
    rc('font',**{'family':'serif','serif':'Computer Modern Roman','size':12})
    rc('text', usetex=True)
import numpy as np
import pylab as plt

def com_shape(label, x, y):
    plt.plot(x, y, 'k-', lw=3.)
    plt.text(3,3,label)
    plt.grid(True, alpha=0.5)
    plt.xlabel(r'$x$ (cm)')
    plt.axis('equal')
    plt.xlim(-3., 5.)
    plt.ylim(-3., 5.)
    return None

if __name__ == '__main__':
    plt.figure(figsize=(8, 2.2))
    plt.subplots_adjust(left=0.08, right=0.99, bottom=0.2)
    plt.subplot(141)
    com_shape(r'\bf A', [-2., -2., 0., 0., 1., 1., -2.], [-2., 1., 1., 0., 0., -2., -2.])
    plt.ylabel(r'$y$ (cm)')
    plt.subplot(142)
    com_shape(r'\bf B', [-2., -2., 0., 0., 2., 2., -2.], [-2., 2., 2., 0., 0., -2., -2.])
    plt.subplot(143)
    com_shape(r'\bf C', [-2., -2., 0., 0., 3., 3., -2.], [-2., 3., 3., 0., 0., -2., -2.])
    plt.subplot(144)
    com_shape(r'\bf D', [-2., -2., 0., 0., 4., 4., -2.], [-2., 4., 4., 0., 0., -2., -2.])
    plt.savefig('com_shapes.pdf')
