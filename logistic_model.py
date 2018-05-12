from file_manipulation import csv_f
import json
import math
import numpy as np
import random
from sentiment_tokenization import combined_data
from textblob import TextBlob

def get_labels(combined_data, csv_f):
    # combined data has "timestamp", "tweet", "sentiment"
    # csv_f has the label indicating price movement at each minute
    # csv_f[0][0] is the time stamp csv_f[0][-1] is the label 
    # give each tweet the same label based on timestamp
    
    for tweet in combined_data:
        ts = tweet["timestamp"]
        for line in csv_f:
            if line[0] == ts:                
                tweet["label"] = line[-1]
    x = []            
    labels = []
    for i in combined_data:
        x.append([i['sentiment'].polarity,i['sentiment'].subjectivity, 1]) 
        labels.append(i['label'])
                
    return x, labels


def split_data(data):
    # divide data into training, validation, and test sets

    # randomly shuffle data in place
    random.shuffle(data)
    
    training_len = math.ceil(len(data) * 0.8)
    validation_len = (len(data) - training_len) // 2 
    
    training = data[:training_len]
    validation = data[training_len : training_len + validation_len]
    test = data[training_len + validation_len:]
    
    return training, validation, test


def logistic_func(w, x):
    
    w = np.array(w)
    
    # must account for bias by extending x by 1-- is bias term the first or last
    # make it the last
    x = np.array(x)
    z = np.dot(w,x)
    
    f = 1 / (1 + math.e ** -z)
    
    return f

# x is a list of the data points, y is a list of the labels, 
# w is a list of the weights
# cost_history is a list of the cost after each iteration of SGD
def mle(x, y, w, cost_history):
    # b is a list of the bias terms
    
    temp = 0
    m = len(x)
    for i in range(m):
        temp += y[i] * math.log(logistic_func(w, x[i], b[i])) + \
        (1 - y[i]) * math.log( 1 - logistic_func(w, x[i], b[i]))
    J = -(1 / m) * temp
    cost_history.append(J)
    return J, cost_history


def SGD(data, a):
    # random initialization of w
    w = [random.random() for i in range(len(data[0] + 1))]
    w = np.array(w)
    
    # shuffle points
    random.shuffle(data)
    
    # derivative of mle cost function
    dw 
    # update w
    w = w - a * dw
    
    pass


def main():
    training, validation, test = split_data(combined_data)
    x, labels = get_labels(training, csv_f)
    
    cost_history = []
    mle(x, labels, w)
    
    a = 0.01
    
    
    