from data import split_data, read_diabetes
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.model_selection import KFold
from sklearn import svm
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt


#model 1 Logistic Regression
def train_logistic_regression(train_x, train_y):
    """Training logistic regression model with train dataset features(train_x) and target(train_y)

    Args:
        train_x (ndarray): train dataset features
        train_y (ndarray): target dataset features

    Return:
        Trained logistic regression model.
    """

    logistic_regression_model = LogisticRegression()
    logistic_regression_model.fit(train_x, train_y)
    return logistic_regression_model

def model_accuracy(trained_model, features, targets):
    """Get the accuracy score of the model

    Args:
        trained_model (LogisticRegression)
        featutres (ndarray)
        targets (ndarray)

    Returns:
        Accuracy score of the trained model.
    """
    accuracy_score = trained_model.score(features, targets)
    return accuracy_score

def select_features(train_x, test_x, features):
    '''
    Creates new dataframes where only the selected features are present.
    The selected features are input as a list.

    Args:
        train_x (pandas dataframe)
        test_x (pandas dataframe)
        features (list of strings)

    Returns:
        Training and test dataframes with only the selected features.
    '''
    train_x = train_x[features]
    test_x = test_x[features]

    return train_x, test_x

def select_features_input(train_x, test_x):
    '''
    Creates new dataframes where only the selected features are present.
    The selected features are input from user.

    Args:
        train_x (pandas dataframe)
        test_x (pandas dataframe)

    Returns:
        Training and test dataframes with only the selected features.
    '''
    feature_num = 2                                         #select features
    while True:
        print('Give number of features, between 2 and 8.')
        feature_num = int(input())
        if (feature_num <= 8 and feature_num >= 2):
            print("Minimum 2 features. Maximum 8.")
            break
    feature_name = []
    for i in range(feature_num):
        print ('feature name :', i+1)
        feature_name.append(input())

    train_x = train_x[feature_name]
    test_x = test_x[feature_name]

    return train_x, test_x

if __name__ == "__main__":

    doctors = read_diabetes()
    train_x, test_x, train_y, test_y = split_data(doctors)

    train_x, test_x = select_features_terminal(train_x, test_x)

    # Training Logistic regression model
    trained_logistic_regression_model = train_logistic_regression(train_x, train_y)
    train_accuracy = trained_logistic_regression_model.score(train_x, train_y)

    # Testing the logistic regression model
    test_accuracy = trained_logistic_regression_model.score(test_x, test_y)
    y_pred = trained_logistic_regression_model.predict(test_x)

    print('Model 1: Logistic regression model')
    print('train_accuracy on given features::',train_accuracy)
    print('test_accuracy on given features::',test_accuracy)

    print(classification_report(test_y, y_pred))

    logit_roc_auc = roc_auc_score(test_y, trained_logistic_regression_model.predict(test_x))
    fpr, tpr, thresholds = roc_curve(test_y, trained_logistic_regression_model.predict_proba(test_x)[:,1])
    plt.figure()
    plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
    plt.plot([0, 1], [0, 1],'r--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.legend()
    plt.show()

    #model 2 Support Vector Machine (SVM) Model
    model = svm.SVC()
    clf = svm.SVC(kernel='linear', C=1).fit(train_x, train_y)   #same train/test split is applied
    svm_accuracy = clf.score(test_x, test_y)
    print("Model 2: SVM accuracy on given features::", svm_accuracy)

    #Here we are using cross validation on split data "cross_val_score"
    accuracy = cross_val_score(model,train_x, train_y, scoring='accuracy', cv = 10)
    print("Model accuracy with cross validation::",accuracy.mean() * 100)
