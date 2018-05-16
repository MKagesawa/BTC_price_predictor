"""

https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60

"""

import json
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.model_selection import train_test_split


# data in format: [1, d["sentiment"][0] , d["sentiment"][1]]
def standardize_data(data):
    
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
        
    return data


def pca_projection(data):
    pca = PCA(n_components = 1)
    principalComponents = pca.fit_transform(data)
    
    principal_df = pd.DataFrame(data = principalComponents, columns = ['PC1'])
    
    explained_variance = pca.explained_variance_ratio_
    
    return principal_df, explained_variance
    

def logistic_reg(data, labels):
    x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size = 0.2)
    
    logreg = LogisticRegression( max_iter = 1000)
    logreg.fit(x_train, y_train)
    
    #predictions = logisticRegr.predict(x_test)
    
    score = logreg.score(x_test, y_test)

    return score


def sgd(data, labels):
    x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size = 0.2)
    sgd = SGDClassifier(loss='log', penalty = 'l2', alpha = 0.0001, shuffle = True, max_iter = 1000)
    sgd.fit(x_train, y_train)
    score = sgd.score(x_test, y_test)
    return score


def main():
    
    labeled_data = []
    with open('labeled_tweets.json') as json_file:
        for line in json_file:
            labeled_data.append(json.loads(line))
    
    
    data = []
    labels = []
    for d in labeled_data:
        data.append([1, d["sentiment"][0] ,  d["sentiment"][1]]) 
        labels.append(d["label"])
        
    data = standardize_data(data)
    
    principal_df, explained_variance = pca_projection(data)
    #print(principal_df)
 
    # combine PC and labels
    # turn labels into a df- need to standardize?? 
    labels_df = pd.DataFrame(labels)
    
    #run logistic reg
    score = logistic_reg(principal_df, labels_df)
    print('Score:', score)
    
    
    score_2 = sgd(principal_df, labels_df)
    print('Score 2:', score_2)
    
main()
