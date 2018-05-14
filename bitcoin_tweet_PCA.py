"""

https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60

"""

import json
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd


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
    

def main():
    
    labeled_data = []
    with open('labeled_tweets.json') as json_file:
        for line in json_file:
            labeled_data.append(json.loads(line))
    print(labeled_data[0])
    
    data = []
    labels = []
    for d in labeled_data:
        data.append([1, d["sentiment"][0] ,  d["sentiment"][1]]) # no d["price"]
        labels.append(d["label"])
 

# apply logistic regression to the transformed data?