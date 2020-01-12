from data import read_diabetes, split_data
from fitting import train_logistic_regression, select_features
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.lines import Line2D

# Scikit-learn Models
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB

def visualize_plot(trained_model, test_x, test_y):
    #create color maps for 2-class classification problem i.e, either diabetes positive or negative
    cmap_light = ListedColormap(['#FFAAAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#0000FF'])

    # Grabbing the a handle on the axes and figure of the plot
    fig, ax = plt.subplots()

    x_min, x_max = test_x.iloc[:,0].min() - 1, test_x.iloc[:,0].max() + 1
    y_min, y_max = test_x.iloc[:,1].min() - 1, test_x.iloc[:,1].max() + 1
    h = 0.1  # step size in the mesh
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = trained_model.predict(np.c_[xx.ravel(), yy.ravel()])
    print (Z)

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    ax.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    ax.scatter(test_x.iloc[:,0], test_x.iloc[:,1], c=test_y, edgecolors='k', cmap=cmap_bold)
    plt.xlabel(test_x.iloc[:,0].name)
    plt.ylabel(test_x.iloc[:,1].name)

    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())

    model_accuracy = trained_model.score(test_x, test_y)
    print("train_accuracy::",model_accuracy)

    return fig

if __name__ == '__main__':

    doctors = read_diabetes()
    train_x, test_x, train_y, test_y = split_data(doctors)

    features = ['glucose', 'mass']
    train_x, test_x = select_features(train_x, test_x, features)

    # Training Logistic regression model
    clf = train_logistic_regression(train_x, train_y)
    #clf = eval(classifier+"()")
    #clf = MLPClassifier()
    #clf.fit(train_x, train_y)

    fig = visualize_plot(clf, test_x, test_y)
    plt.savefig('./static/visualize_plot.png')
    plt.show()
