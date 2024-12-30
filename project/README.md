
***

<div style="text-align: center; color: red;">
  <h1>Programming for Data Analytics module</h1>

  <h1>The project: "Wind Speed Analysis around the Ireland with a view to Wind Farm"</h1>
</div>

***

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Mount_Lucas_Wind_Farm_Co._Offaly_Ireland_-_geograph.org.uk_-_5399920.jpg/800px-Mount_Lucas_Wind_Farm_Co._Offaly_Ireland_-_geograph.org.uk_-_5399920.jpg)


This directory contains my work (project implementation) on the **Programming for Data Analytics** module of the [ATU](https://www.atu.ie/) **Higher Diploma in Science in Computing in Data Analytics** course. 


## Project Objectives:

1. Analyse historical wind speed data across Ireland.
2. Determine optimal locations for wind farms based on wind speed trends and operational ranges.
3. Identify potential future wind power trends and variability.
4. Implement long-term forecasting using appropriate models.


## Assessment strategy for the project: 

| **Description**                |                                                                                                   |
|--------------------------------|---------------------------------------------------------------------------------------------------|
| **Minimum Project**            |                                                                                                   |
| 1. Read in/acquire/make up, a number of good data sets |                                                                           |
| 2. Analyse the data using various techniques, we have covered in this module|                                                      |
| 3. Some nice-looking plots to illustrate our findings. |                                                                           |
| **Features we can add**        |                                                                                                   |
| 1. Increase the range of data we are analysing |                                                                                   |
| 2. Use more features of SciKitLearn and other packages that we find useful |                                                       |
| 3. Provide meaningful insights    |                                                                                                |
| 4. Increase the complexity of our plots without reducing readability |                                                             |
| 5. Use a database                 |                                                                                                |


***

## Repository Files Description

1. **data/**
   - **File format**: Directory.
   - **Description**: Contains individual CSV files for each meteorological station. These files are downloaded during the execution of the code in the `fetching_data.ipynb` notebook.

2. **All_stations_data.csv**
   - **File format**: CSV.
   - **Description**: A combined file containing data from all stations. It includes selected fields of interest for analysis and is created using the `fetching_data.ipynb` notebook.

3. **analysis_by_station.py**
   - **File format**: Python script.
   - **Description**: Contains the `StationProcessor` class, which is used in the `wind_analysis.ipynb` notebook to prepare individual station files for analysis. This includes tasks like converting wind speed units, filling missing values, and describing the dataset for analysis.

4. **README.md**
   - **File format**: Markdown.
   - **Description**: Provides an overview of the directory, its purpose, and instructions for usage.

5. **fetching_data.ipynb**
   - **File format**: Jupyter Notebook.
   - **Description**: Fetches and downloads station-specific data using a base URL. It also combines the selected fields into a unified dataset (`All_stations_data.csv`) for all stations.

6. **wind_analysis.ipynb**
   - **File format**: Jupyter Notebook.
   - **Description**: Represents the main project. Includes a comparative analysis of all stations, exploration of trends and tendencies, application of analyses to specific stations, wind power calculations for turbines, and long-term forecasting using appropriate models.

7. **requirements.txt**
   - **File format**: Text.
   - **Description**: Lists all the Python dependencies and libraries required to run the code in this directory. Install these packages using `pip install -r requirements.txt`.


***

## Getting Started

### Development Environment

This project was developed using:

- **Visual Studio Code (VS Code):** Used as the primary IDE for writing and managing code.
- **Virtual Environment:** A virtual environment (`venv`) was set up to manage project dependencies and ensure isolation from system-wide Python packages.

### Set Up the Development Environment:

- Install VS Code if not already installed. Download it from [https://code.visualstudio.com/](https://code.visualstudio.com/).

- Run the following commands to set up and activate a virtual environment:

```bash
python -m venv project_env
project_env\Scripts\activate # On Windows (source project_env/bin/activate On MacOS/Linux)
```

- Use the `requirements.txt` file to install all necessary libraries:

```bash
pip install -r requirements.txt
```

- Open the project folder in VS Code and activate the virtual environment within the integrated terminal for a seamless development experience.

- Install recommended VS Code extensions such as:
  - Python
  - Pylance
  - Jupyter (for working with `.ipynb` notebooks)

- All work for this project was conducted within a virtual environment to ensure consistency and ease of dependency management.


***

## Usage Guide

### For Data Analysis

The primary focus of this project is on **wind_analysis.ipynb**, which serves as the main notebook, providing a comprehensive overview of the entire project. This notebook includes the following:

- A detailed comparative analysis of meteorological stations.
- Identification of trends and tendencies across stations.
- Application of analyses to individual stations, including wind power calculations for turbine use.
- Long-term forecasting using appropriate predictive models.

### Workflow

Before running **wind_analysis.ipynb**, it is essential to ensure that the required data is available. This data is prepared using **fetching_data.ipynb**, which:

1. Downloads and extracts raw meteorological data for individual stations.
2. Combines the selected data fields into a unified file named **All_stations_data.csv**.

To begin the analysis, either:
- Run **fetching_data.ipynb** first to download and prepare the data.
- Or use the raw station-specific files from the `data/` directory and the combined **All_stations_data.csv** file if they have already been created.

### Importance and Usefulness

This project might be useful for:
- Researchers analysing wind trends and their potential applications in renewable energy.
- Developers exploring workflows for integrating meteorological data into analytical systems.
- Decision-makers assessing the feasibility of wind turbine installations in specific regions.

While the project already provides a robust foundation for wind data analysis, there is room for further development. Possible areas for extension include:
- Enhancing turbine power calculations with hourly or more granular data.
- Incorporating additional meteorological features into long-term forecasting models.

### Important Notes

- **Environment Setup**: Ensure that your Python environment matches the dependencies specified in `requirements.txt`. This can be done using a virtual environment to maintain consistency and prevent dependency conflicts.
- **References**: Links to external resources and references used throughout the notebooks are:
  - **Embedded as clickable links**: Directly accessible within the text of the notebooks.
  - **Aggregated in the References section**: Located at the end of **wind_analysis.ipynb** for consolidated access.

***

## Autor

Created by **Yuliia Kharchenko**.

***