"""

https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60
https://stackoverflow.com/questions/44443479/python-sklearn-show-loss-values-during-training/44453621#44453621
http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier.score

"""
import io
import json
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.model_selection import train_test_split
import sys


# data in format: [1, d["sentiment"][0] , d["sentiment"][1]]
def normalize_data(data):
    
    polarity_sum = 0
    subjectivity_sum = 0
     
    for d in data:
        polarity_sum += d[1]
        subjectivity_sum += d[2]
    mean_polarity = polarity_sum / len(data)
    mean_subjectivity = subjectivity_sum / len(data)
        
    for i in range(len(data)):
        data[i][1] -= mean_polarity
        data[i][2] -= mean_subjectivity
    #for d in data:
    #    print(d)
    return data


def pca_projection(data):
    pca = PCA(n_components = 1)
    principalComponents = pca.fit_transform(data)
    
    principal_df = pd.DataFrame(data = principalComponents, columns = ['PC1'])
    
    explained_variance = pca.explained_variance_ratio_
    print('principal_df: ', principal_df)
    print('explained_variance: ', explained_variance)
    return principal_df, explained_variance


def logistic_reg(data, labels):
    x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size = 0.2)
    
    logreg = LogisticRegression( max_iter = 1000)
    logreg.fit(x_train, y_train)
    
    #predictions = logisticRegr.predict(x_test)
    
    score = logreg.score(x_test, y_test)
    print('score: ', score)
    return score



def sgd(data, labels, a = 0.001, i = 1000):
    x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size = 0.2)
    sgd = SGDClassifier(loss='log', penalty = 'l2', alpha = a, shuffle = True, max_iter = i, verbose = 1) #verbose = 1
    sgd.fit(x_train, y_train)
    score = sgd.score(x_test, y_test)
    
    # plot loss 
    old_stdout = sys.stdout
    sys.stdout = mystdout = io.StringIO()
    sys.stdout = old_stdout
    loss_history = mystdout.getvalue()
    
    loss_list = []
    for line in loss_history.split('\n'):
        if(len(line.split("loss: ")) == 1):
            continue
        loss_list.append(float(line.split("loss: ")[-1]))
    plt.figure()
    plt.plot(np.arange(len(loss_list)), loss_list)
    plt.title('Loss over Epochs')
    plt.xlabel("Time in epochs")
    plt.ylabel("Loss")
    plt.xlim([0, 9])
    plt.ylim([0.5, 1])
    plt.show()
    plt.close()
    print('sgd score: ', score)
    return score

def test_hyperparameters(data, labels, alpha, max_iter):
    for a in alpha:
        for i in max_iter:
            s = sgd(data, labels, a, i)
            print('Score with alpha = {} and max_iter = {} : {}'.format(a, i, s))


def main():
    
    labeled_data = []
    with open('labeled_tweets.json') as json_file:
        for line in json_file:
            labeled_data.append(json.loads(line))   
    
    data = []
    labels = []
    for d in labeled_data:
        data.append([1, d["sentiment"][0],  d["sentiment"][1]])
        labels.append(d["label"])
        
    data = normalize_data(data)
    
    principal_df, explained_variance = pca_projection(data)
    
 
    # combine PC and labels
    # turn labels into a df- need to normalize??
    labels_df = pd.DataFrame(labels)
    
    #run logistic reg
    #score = logistic_reg(principal_df, labels_df)
    #print('Score:', score)
    
    # alpha = [0.01, 0.001, 0.0001]
    # max_iter = [100, 1000, 10000]
    # test_hyperparameters(principal_df, labels_df, alpha, max_iter)
    # from this test, the lowest test score was reached using a = 0.001 and max_iter = 1000
    score = sgd(principal_df, labels_df)
    print('Test Score:', score)
    
    # test for overfitting

main()
