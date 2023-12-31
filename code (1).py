#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


# Import all neccesary libraries and package in the code
import numpy as np
import matplotlib.pyplot as plt 

# Creating a user-define function named scatter
def scatter (distance,theta,colors,area):
    # creating the figure object 
    fig = plt.figure(figsize=(9,9))
    # Creating the axis object and setting the projections to be a polar 
    ax = fig.add_subplot(projection = 'polar')
    # Plotiing the graph
    c = ax.scatter(distance,theta,c=colors,s=area,cmap='hsv',alpha=0.80)
    # Defining the titile of plot 
    plt.title('Demonstrating the scatter plot in polar co-ordinates')
    # Displaying the plot
    plt.show()
    
    
# Creating the main() finction
def main():
    # Defining random seed to that the numbers are not changed each time we refresh the code 
    np.random.seed(42)
    # Using the random function to set the distance
    distance = np.arange(1,2*np.pi,0.1)
    # Creating 600 data point for the angle subtended by the points
    theta = np.log(distance)
    # Defining the area of the point to be disoplayed
    area = 200
    # Defining color value to be used for cmap
    colors = theta
    # Printing the data point for better understanding 
    print(theta[:100])
    print(distance[:100])
    # calling the scatter() function
    scatter(distance,theta,colors,area)
# calling the main() function
if __name__ == '__main__':
    main()
  


# In[ ]:




