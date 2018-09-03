import pyvie as pv
import numpy as np
import matplotlib.pyplot as plt

movie = pv.Movie("RandomImageExample",framerate=1,dpi=400,file_type='.png',movie_type = '.avi')

plt.imshow(np.zeros((10,10)))
movie.gather()
plt.clf()
plt.imshow(np.random.uniform(size=(10,10)))
movie.gather()
plt.clf()
plt.imshow(np.random.random(size=(10,10)))
movie.gather()
plt.clf()
plt.scatter([1,2,3,4],[5,6,7,8])
movie.gather()
plt.clf()
plt.plot(np.linspace(0,2*np.pi,100),np.sin(np.linspace(0,2*np.pi,100))*np.cos(np.linspace(0,2*np.pi,100)))
movie.gather()

movie.finalize()