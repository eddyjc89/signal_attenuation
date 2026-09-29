# main.py

#imports
import numpy
import pandas
import matplotlib.pyplot
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression
from sklearn.manifold import MDS
from matplotlib.lines import Line2D
import matplotlib.patches as mpatch

# main
def main():
    # Load data
    AP_Location_df = pandas.read_excel('./data/Signal_Attenuation_Condensed.xlsx', sheet_name='AP_Positions')
    Measured_Point_Location_df = pandas.read_excel('./data/Signal_Attenuation_Condensed.xlsx', sheet_name='Measured_Point_Positions')
    Training_Obs_df = pandas.read_excel('./data/Signal_Attenuation_Condensed.xlsx', sheet_name='Training_Obs')
    Experiment_Obs_df = pandas.read_excel('./data/Signal_Attenuation_Condensed.xlsx', sheet_name='Experiment_Obs')
    print(AP_Location_df.head())
    print(Measured_Point_Location_df.head())
    print(Training_Obs_df.head())
    print(Experiment_Obs_df.head())

if __name__ == "__main__":
    main()