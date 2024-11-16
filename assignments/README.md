
# **PROGRAMMING FOR DATA ANALYTICS (ASSIGNMENTS)**

![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Python_Powered.png/640px-Python_Powered.png)

This directory contains solutions for the following assignments:

1. Weather Plot ([assignment2-weather.ipynb](./assignment2-weather.ipynb)).
2. Pie Chart of Email Domains ([assignment03-pie.ipynb](./assignment03-pie.ipynb))
3. Risk Simulation ([assignment_5_risk.py](./assignment_5_risk.ipynb))
4. Knock Airport Weather Analysis ([assignment_6_Weather.py](./assignment_6_Weather.ipynb))

Each notebook focuses on specific data analysis tasks, visualization techniques, and simulations using Python.

***

### **Assignment 2 weather**

***

- **Objective**: Visualize the temperature over time (dryBulbTemperature_Celsius) with a clear and informative plot.

- **Key Features**:
  - Uses Pandas to load and process weather data ([data for assignment](./weatherreadings1.csv)).
  - Generates a scatter plot with Matplotlib.

##### **References**

- [scatter(x, y)](https://matplotlib.org/stable/plot_types/basic/scatter_plot.html#sphx-glr-plot-types-basic-scatter-plot-py)
- [matplotlib.axes.Axes.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib-axes-axes-scatter)
- [Annotations](https://matplotlib.org/stable/users/explain/text/annotations.html#annotations)
- [matplotlib.pyplot.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib-pyplot-axvline)
- [pandas.to_datetime](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas-to-datetime)
- [Python | Pandas.to_datetime()](https://www.geeksforgeeks.org/python-pandas-to_datetime/)
- [matplotlib.dates](https://matplotlib.org/stable/api/dates_api.html)

***

### **Assignment 3 domains**

***

- **Objective**: Create a pie chart showing the distribution of email domains from a dataset.

- **Key Features**:
  - Uses a CSV file from the url: https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download. 
  - Visualizes the relative frequency of domains from the given dataset.

##### **References**

- [Labeling a pie and a donut](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html)
- [Pie charts](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html)
- [matplotlib.style](https://matplotlib.org/stable/api/style_api.html#matplotlib.style.use)
- [Style sheets reference](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)
- [Selecting individual colors from a colormap](https://matplotlib.org/stable/gallery/color/individual_colors_from_cmap.html)
- [How to have actual values in matplotlib Pie Chart displayed](https://stackoverflow.com/questions/41088236/how-to-have-actual-values-in-matplotlib-pie-chart-displayed)

***

### **Assignment 5 risk** 

***

- **Objective**: Simulate 1000 battle rounds in Risk Game (3 attackers vs 2 defenders) and plot the results.

- **Key Features**:
  - Implements Risk rules for troop losses based on dice rolls.
  - The plot visually communicates the distribution of possible outcomes in Risk battles, emphasizing which scenarios are most and least likely     under the given conditions.

##### **References**

- [Risk game with python_stackoverflow](https://stackoverflow.com/questions/74421396/risk-game-with-python)
- [Speed up Risk wargame dice rolling simulation_stackoverflow](https://stackoverflow.com/questions/23885702/speed-up-risk-wargame-dice-rolling-simulation)
- [Python Random choices() Method](https://www.w3schools.com/python/ref_random_choices.asp)
- [numpy.column_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html)
- [Indexing on ndarrays](https://numpy.org/doc/stable/user/basics.indexing.html)
- [np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy-unique)
- [How to fit the text above the bars plot in matplotlib?](https://stackoverflow.com/questions/71366538/how-to-fit-the-text-above-the-bars-plot-in-matplotlib)

***

### **Assignment 6 Knock airport Weather**

***

- **Objective**: Analyze and visualize weather data from Knock Airport ([data for assignment](./hly4935.csv)).

- **Key Features**:
  - Plots temperature trends over time, daily and monthly means.
  - Analyzes windspeed data, including rolling averages and maximum values.

##### **References**

- [Ignore the first space in CSV](https://stackoverflow.com/questions/70801888/ignore-the-first-space-in-csv)
- [pandas.read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- [pandas.to_datetime](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html)
- [matplotlib.pyplot.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)
- [Matplotlib.dates.DateFormatter class in Python](https://www.geeksforgeeks.org/matplotlib-dates-dateformatter-class-in-python/)
- [pandas.DataFrame.resample](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html)
- [pandas.Series.rolling](https://pandas.pydata.org/docs/reference/api/pandas.Series.rolling.html)
- [Working with Missing Data in Pandas](https://www.geeksforgeeks.org/working-with-missing-data-in-pandas/)


***

## **How to Use this directory**

To run the Jupyter notebooks you'll need the following Python libraries:

- `pandas`
- `numpy`
- `matplotlib`


***

## **Author**

Created by **Yuliia Kharchenko**.

***