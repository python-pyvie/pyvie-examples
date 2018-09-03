import pyvie as pv
import numpy as np
import matplotlib.pyplot as plt

movie = pv.Movie("ImshowExample",framerate=5,dpi=400,file_type='.png',movie_type = '.avi')
plt.figure(figsize=(10,10))
grid = np.zeros((10,10))
for t in range(100):
    plt.clf()
    y = np.random.randint(0,grid.shape[0])
    x = np.random.randint(0,grid.shape[1])
    grid[y,x] += 1
    plt.imshow(grid)
    plt.title('2D Imshow',fontsize = 22)
    plt.xticks(fontsize = 15)
    plt.yticks(fontsize = 15)
    movie.gather()
movie.finalize()