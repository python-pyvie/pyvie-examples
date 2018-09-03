import matplotlib.pyplot as plt
import numpy as np
import pyvie as pv

movie = pv.Movie("SkydiverExample",framerate=10,dpi=400,file_type='.png',movie_type = '.avi')
x0 = 0
y0 = 1000
x = [x0]
y = [y0]
vix = 10
viy = 0
vx = [vix]
vy = [viy]
axi = 0
ayi = -9.81
ax = [axi]
ay = [ayi]
start = 0 
end = 15
steps = 20
time = np.linspace(start,end,steps)
for t in time[1:]:
    
    f, ((ax1, ax2),(ax3, ax4)) = plt.subplots(2, 2, figsize=(10,10))
    ax1.set_title('Skydiver',fontsize=22)
    ax1.scatter(x[-1], y[-1])
    ax1.set_ylim(0,1050)
    ax1.set_xlim(-5,155)
    ax1.tick_params(labelsize=15)
    ax2.set_title('Skydiver Trajectory',fontsize=22)
    ax2.plot(x, y)
    ax2.set_ylim(0,1050)
    ax2.set_xlim(-5,155)
    ax2.tick_params(labelsize=15)
    ax3.set_title('Skydiver Velocity',fontsize=22)
    ax3.plot(time[0:len(vx)],np.sqrt(np.array(vx)**2+np.array(vy)**2))
    ax3.set_ylim(0,145)
    ax3.set_xlim(-1,15)
    ax3.tick_params(labelsize=15)
    ax4.set_title('Skydiver Acceleration',fontsize=22)
    ax4.plot(time[0:len(ax)],np.sqrt(np.array(ax)**2+np.array(ay)**2))
    ax4.set_xlim(-1,15)
    ax4.tick_params(labelsize=15)
    movie.gather()
    f.clf()
    
    x.append(.5*ax[-1]*t**2 + vix*t + x0)
    y.append(.5*ay[-1]*t**2 + viy*t + y0)
    
    vx.append(vix + ax[-1]*t)
    vy.append(viy + ay[-1]*t)
    
    ax.append(axi)
    ay.append(ayi)
    
movie.finalize()