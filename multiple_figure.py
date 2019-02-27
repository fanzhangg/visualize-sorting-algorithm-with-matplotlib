import numpy as np
import matplotlib.pyplot as pl
import matplotlib


x = np.linspace(0., 10., 11)
y = x ** 2
z = x ** 3

pl.ion()

pl.figure(1)
pl.plot(x, y, 'bo:')
# Plot large blue dots connected by blue lines

pl.xlabel('x')
pl.ylabel('y')
pl.title('plot 1')

pl.figure(2)
pl.plot(x, z, 'rs-')
# Plot large red squares connected by solid lines


pl.xlabel('x')
pl.ylabel('z')
pl.title('plot 2')
