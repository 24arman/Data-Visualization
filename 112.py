#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[3]:


# Import all neccesary libraries and package in the code
import random

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates




from mpl_toolkits.mplot3d import Axes3D

mpl.rcParams['font.size']= 10
fig = plt.figure()
ax  = fig.add_subplot(111,projection='3d')



for z in [2011,2012,2013,2014]:
    xs = range(1,13)
    ys = 1000 * np.random.rand(12)
    
    
    color = plt.cm.Set2(random.choice(range(plt.cm.Set2.N)))
    ax.bar(xs,ys,zs = z, zdir='y', color = color ,alpha = 0.8)

ax.xaxis.set_major_locator(mpl.ticker.FixedLocator(xs))
ax.yaxis.set_major_locator(mpl.ticker.FixedLocator(ys))


ax.set_xlabel('month')
ax.set_ylabel('year')
ax.set_zlabel('sales net[usd]')

plt.show()


# In[ ]:




