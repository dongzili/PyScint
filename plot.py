import numpy as np
import matplotlib.pyplot as plt
import matplotlib
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 14}
matplotlib.rc('font', **font)

def __init__():
    return

def smooth( array, n0, n1 ):
    array_out = array
    for i in range(n0):
        array_out = array_out + np.roll(array, i, axis=0) + np.roll(array, -1*i, axis=0)
    for i in range(n1):
        array_out = array_out + np.roll(array, i, axis=1) + np.roll(array, -1*i, axis=1)
    array_out = array_out * (1. + 2.*n0 + 2.*n1 )
    return array_out

def plot_secondary(I1,I2,doppler,delay,num_rows):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.imshow(np.log(np.real(smooth(I1*np.conjugate(I2),5,0))
                  [num_rows/2:7*num_rows/10,:]),origin='lower',
           extent=[doppler[0],doppler[-1],
                   delay[num_rows/2],delay[7*num_rows/10]],
           vmin=18,vmax=30,cmap=plt.get_cmap('gray_r'))
    ax.set_aspect('auto')
    plt.colorbar(orientation='vertical')
    plt.xlabel(r'$f_D$ [mHz]')
    plt.ylabel(r'$\tau$[ms]')

def plot_dynamic(I,time,frequency):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.imshow(I1,extent=[time[0],time[-1],frequency[0],frequency[-1]],
               vmin=18,vmax=30,cmap=plt.get_cmap('gray_r'))
    ax.set_aspect('auto')
    plt.colorbar(orientation='vertical')
    plt.xlabel(r'time (s)')
    plt.ylabel(r'frequency (MHz)')

