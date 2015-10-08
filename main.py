from datetime import time
from generator_sets import Point, Set, Generator
import random
# from math import *
# import matplotlib.pyplot as plt
# from pandas import date_range,Series,DataFrame,read_csv, qcut
# from pandas.tools.plotting import radviz,scatter_matrix,bootstrap_plot,parallel_coordinates
# from numpy.random import randn
# from pylab import *
# import brewer2mpl
# from matplotlib import rcParams *

print('hi')
generator = Generator()
generator.init()
# start = Time.tzname()
sets = generator.generate()
# print('this end with this: ', time.tzname()-start)
for set in sets:
    print('hey')
    set.print_()





