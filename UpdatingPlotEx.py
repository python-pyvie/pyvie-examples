import pyvie as pv
import numpy as np
import matplotlib.pyplot as plt

movie = pv.Movie('UpdatingPlotExample',framerate=10,dpi=400,file_type='.png',movie_type = '.avi')
plt.figure(figsize = (10,10))
x_data = []
y_data = []
lower_line = []
upper_line = []
for t in range(101):
    plt.clf()
    y_data.append(t*np.random.choice([1,2,3]))
    x_data.append(t)
    lower_line.append(t)
    upper_line.append(3*t)
    plt.plot(x_data,lower_line,linewidth=2,c='r')
    plt.plot(x_data,upper_line,linewidth=2,c='g')
    plt.plot(x_data,y_data,linewidth=2,c='black')
    plt.fill_between(x_data,lower_line,upper_line,alpha = .3,color='black')
    plt.xlim(0,100)
    plt.ylim(0,300)
    plt.title('Updating Plot',fontsize = 22)
    plt.xticks(fontsize = 15)
    plt.yticks(fontsize = 15)
    plt.grid(alpha=.5)
    movie.gather()
movie.finalize()