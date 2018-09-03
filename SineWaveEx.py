import pyvie as pv
import numpy as np
import matplotlib.pyplot as plt

movie = pv.Movie('SineWaveExample',framerate=20,dpi=400,file_type='.png',movie_type = '.avi')
plt.figure(figsize = (10,10))
for phi in np.linspace(0,2*np.pi,300):
    plt.clf()
    x = np.linspace(0,2*np.pi,100)
    y = np.sin(x+phi)
    plt.plot(x,y,linewidth = 4)
    plt.xlim(0,2*np.pi)
    plt.grid(alpha=.5)
    plt.title('Sine Wave Example',fontsize = 22)
    plt.xticks(fontsize = 15)
    plt.yticks(fontsize = 15)
    movie.gather()
movie.finalize()