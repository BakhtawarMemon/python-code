import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from sklearn.model_selection import train_test_split
import argparse
from warnings import simplefilter

def read_diabetes():
    '''
    Reads "diabetes.csv", drops NAN values, sets the string values in the diabetes column to integers and
    returns a dataframe of the dataset.
    '''

    simplefilter(action='ignore', category=FutureWarning)   #to ignore all future warnings

    doctor = pd.read_csv('diabetes.csv', index_col=0)       #Read data
    doctors = doctor.dropna()                               #and remove empty values

    pd.set_option('mode.chained_assignment', None)
    doctors.diabetes[doctors.diabetes == 'pos'] = 1         #convert label column in binary
    doctors.diabetes[doctors.diabetes == 'neg'] = 0

    return doctors

def split_data(doctors):
    '''
    Takes a dataframe of the data from "diabetes.csv" and splits dataset into a 80/20 train-test-split.
    Returns training and test sets, including targets.
    '''
    train_features = doctors.drop('diabetes', axis=1)       #split data into training and
    target = doctors['diabetes']                            #test/validation sets
    target = target.astype('int')
    train_x, test_x, train_y, test_y = train_test_split(train_features, target, train_size=0.8)
    #print ('train_x size ::', train_x.shape)
    #print ('train_y size :: ', train_y.shape)
    #print ('test_x size ::', test_x.shape)
    #print ('test_y size :: ', test_y.shape)
    return train_x, test_x, train_y, test_y



def create_scatter_plot(feature_1, feature_2):
    """This function will create scatter plot of two dimensions of the feature space
        and shows how the given dimensions relates to the diabetes class.

    Args:
        feature_1 (str): Name  of feature one
        feature_2 (str): Name of feature two

    Returns:
        Scatter plot of how the given two features relates to diabetes class.

    """
    color= ['green' if l == 1 else 'blue' for l in doctors.diabetes]
    plt.scatter(doctors[feature_1], doctors[feature_2],  color=color)
    plt.xlabel(feature_1)
    plt.ylabel(feature_2)

    legend_elements = [Line2D([0], [0], marker='o', color='w', label='positive',
                            markerfacecolor='g', markersize=10),
                            Line2D([0], [0], marker='o', color='w', label='negative',
                            markerfacecolor='b', markersize=10)]
    plt.legend(handles=legend_elements, title="diabetes")
    plt.show()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
    description='Creates a scatter plot of a pair of features from dataset')

    parser.add_argument('-o', '--feature_1', type=str,
                    help='e.g., glucose, mass, insulin, pregnant etc', required=True)

    parser.add_argument('-t', '--feature_2', type=str,
                    help='e.g., glucose, mass, insulin, pregnant etc', required=True)

    args = parser.parse_args()

    doctors = read_diabetes()

    create_scatter_plot(args.feature_1, args.feature_2)
