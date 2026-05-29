import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 11)
#  creating axis for x
y = x ** 2
#  let y be all the values for x^2
plt.plot(x, y)
plt.savefig('ch_1.6_saving_figures_example_using_savfig.png', dpi=300)
#  plot what value of y you get, for each x.
