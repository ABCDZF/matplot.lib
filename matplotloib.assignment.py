#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q.1> What is Matpltolib ? why is it used ? Name five plots that can be plotted using the Pyplot module of Matplotlib.
Matplotlib is a popular Python library used for creating visualizations and plots. It provides a comprehensive collection 
of tools for data visualization, including data analysis, plotting, and image manipulation. Matplotlib is widely used in 
the scientific community, particularly in data analysis and research.

Matplotlib's Pyplot module is a collection of functions that provides a convenient interface for creating plots and charts. 
It simplifies the process of creating visualizations by providing a consistent interface for different types of plots.

Here are five types of plots that can be created using the Pyplot module of Matplotlib:

1. Line plots: These plots display data as a series of points connected by a line. They are commonly used to display trends and 
   changes in data over time.

2. Scatter plots: These plots display data as a set of points, where each point represents a single observation or data point. 
   They are commonly used to identify patterns and relationships between variables.

3. Bar plots: These plots display data as a set of rectangular bars, where the height of each bar represents the value of the 
   corresponding data point. They are commonly used to compare different categories or groups.

4. Histograms: These plots display the distribution of data by grouping it into intervals or bins and displaying the number of 
   observations in each bin. They are commonly used to explore the distribution of data.

5. Heatmaps: These plots display data as a grid of colored squares, where the color of each square represents the value of the 
   corresponding data point. They are commonly used to visualize large datasets and identify patterns and trends.


# Q2 A scatter plot is a type of graphical display used to represent the relationship between two numerical variables. In a scatter plot, each observation in a data set is represented by a point, with the position of the point determined by the values of the two variables being plotted.
# 
# 

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
np.random.seed(3)
x = 3 + np.random.normal(0,2,50)
y = 3 + np.random.normal(0,2,len(x))
plt.scatter(x,y)
plt.title("This is my title")
plt.xlabel("X axis")
plt.ylabel("Y axis")


# Q3
# 

# In[ ]:


Q.1> What is Matpltolib ? why is it used ? Name five plots that can be plotted using the Pyplot module of Matplotlib.
Matplotlib is a popular Python library used for creating visualizations and plots. It provides a comprehensive collection 
of tools for data visualization, including data analysis, plotting, and image manipulation. Matplotlib is widely used in 
the scientific community, particularly in data analysis and research.

Matplotlib's Pyplot module is a collection of functions that provides a convenient interface for creating plots and charts. 
It simplifies the process of creating visualizations by providing a consistent interface for different types of plots.

Here are five types of plots that can be created using the Pyplot module of Matplotlib:

1. Line plots: These plots display data as a series of points connected by a line. They are commonly used to display trends and 
   changes in data over time.

2. Scatter plots: These plots display data as a set of points, where each point represents a single observation or data point. 
   They are commonly used to identify patterns and relationships between variables.

3. Bar plots: These plots display data as a set of rectangular bars, where the height of each bar represents the value of the 
   corresponding data point. They are commonly used to compare different categories or groups.

4. Histograms: These plots display the distribution of data by grouping it into intervals or bins and displaying the number of 
   observations in each bin. They are commonly used to explore the distribution of data.

5. Heatmaps: These plots display data as a grid of colored squares, where the color of each square represents the value of the 
   corresponding data point. They are commonly used to visualize large datasets and identify patterns and trends.
Q.2> What is a scatter plot? Use the following code to generate data for x and y. Using this generated data plot a scatter plot.
A scatter plot is a type of graphical display used to represent the relationship between two numerical variables. In a scatter plot, each observation in a data set is represented by a point, with the position of the point determined by the values of the two variables being plotted.

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(3)
x = 3 + np.random.normal(0,2,50)
y = 3 + np.random.normal(0,2,len(x))
plt.scatter(x,y)
plt.title("This is my title")
plt.xlabel("X axis")
plt.ylabel("Y axis")
Text(0, 0.5, 'Y axis')

Q3: Why is the subplot() function used? Draw four line plots using the subplot() function. Use the following data:
The subplot() function is used in data visualization to create multiple plots within a single figure. It allows us to create a grid of subplots, each displaying a different plot, and control the size, layout, and appearance of each subplot To create four line plots using the subplot() function, we can use the following code

import numpy as np
import matplotlib.pyplot as plt

# Create the data arrays for each line plot
x1 = np.array([0, 1, 2, 3, 4, 5])
y1 = np.array([0, 100, 200, 300, 400, 500])
x2 = np.array([0, 1, 2, 3, 4, 5])
y2 = np.array([50, 20, 40, 20, 60, 70])
x3 = np.array([0, 1, 2, 3, 4, 5])
y3 = np.array([10, 20, 30, 40, 50, 60])
x4 = np.array([0, 1, 2, 3, 4, 5])
y4 = np.array([200, 350, 250, 550, 450, 150])

# Create a figure and a grid of subplots with 2 rows and 2 columns
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))

# Plot the first line plot on the top-left subplot
axs[0, 0].plot(x1, y1)
axs[0, 0].set_title('Line 1')

# Plot the second line plot on the top-right subplot
axs[0, 1].plot(x2, y2)
axs[0, 1].set_title('Line 2')

# Plot the third line plot on the bottom-left subplot
axs[1, 0].plot(x3, y3)
axs[1, 0].set_title('Line 3')

# Plot the fourth line plot on the bottom-right subplot
axs[1, 1].plot(x4, y4)
axs[1, 1].set_title('Line 4')

# Add a common x-axis label and a common y-axis label to the entire figure
fig.text(0.5, 0.04, 'X-axis Label', ha='center')
fig.text(0.04, 0.5, 'Y-axis Label', va='center', rotation='vertical')

# Show the plot
plt.show()





 


# In[ ]:


Q.4> What is a bar plot? Why is it used? Using the following data plot a bar plot and a horizontal bar plot.
A bar plot is a type of data visualization that uses rectangular bars to represent data values. In a bar plot, the height or length of each bar corresponds to the value of a particular variable or category. Bar plots can be created horizontally or vertically, and they are commonly used to compare the sizes or values of different categories or variables.

Bar plots are useful for presenting categorical data, such as the frequency of occurrence of different categories or the distribution of a categorical variable. They are also used to compare the values of numerical data for different categories, such as the average scores of students in different classes or the sales figures of different products.

company = np.array(["Apple" , "Microsoft" , "Google" , "AMD"])
profit = np.array([3000,8000,1000,10000])
# plotting a bar plot
plt.bar(company, profit)
plt.xlabel("Company Name")
plt.ylabel("Profit")
plt.title("Vertical Bar Plot")
plt.show()
# Plotting a Horizental Bar Plot
plt.barh(company, profit)
plt.xlabel("Profit")
plt.ylabel("Company Name")
plt.title("Horizental Bar Plot")
plt.show(


# In[ ]:


Q.5> What is a box plot? Why is it used? Using the following data plot a box plot.
Box plot is a type of data visualization that displays the distribution of a numerical dataset. The plot is made up of a box and whisker diagram that provides information on the central tendency, spread, and skewness of the data. Box plots are used to display the distribution of a dataset and to identify any outliers or extreme values. They are useful for comparing the distribution of multiple datasets, such as different groups or samples, and for detecting any differences or similarities in the data. Box plots are commonly used in statistical analysis, data science, and scientific research to explore and communicate the characteristics of a dataset.

box1 = np.random.normal(100,10,200)
box2 = np.random.normal(90,20,200)
plt.boxplot(box1)
plt.boxplot(box2)
plt.show()

