import json
import math
import numpy as np
import random
from textblob import TextBlob
import sentiment_tokenization

"""
def get_labels(combined_data, csv_f):
    # combined data has "timestamp", "tweet", "sentiment"
    # csv_f has the label indicating price movement at each minute
    # csv_f[0][0] is the time stamp csv_f[0][-1] is the label 
    # give each tweet the same label based on timestamp
    labeled_data = []
    for tweet in combined_data:
        ts = tweet["timestamp"]
        for line in csv_f:
            if line[0] == ts:                
                tweet["label"] = line[-1]
            labeled_data.append(tweet)
    return labeled_data
"""1

def split_data(data):
    # divide data into training, validation, and test sets

    # randomly shuffle data in place
    random.shuffle(data)
    
    training_len = math.ceil(len(data) * 0.8)
    validation_len = len(data) - training_len
    test_len = len(data) - validation_len - training_len
    
    training = data[:training_len]
    validation = data[training_len:test_len]
    test = data[test_len:]
    
    return training, validation, test


def logistic_func(w, x, b):
    z = np.dot(w, x)
    f = 1 / (1 + math.e ** -z)
    return f


def mle(x, y, w, b, cost_history):
    # cost_history is a list of the cost after each iteration of SGD
    temp = 0
    m = len(x)
    for i in range(m):
        temp += y[i] * math.log(logistic_func(w, x[i], b[i])) + \
        (1 - y[i]) * math.log(1 - logistic_func(w, x[i], b[i]))
    J = -(1 / m) * temp
    cost_history.append(J)
    return J, cost_history


def SGD(data, a):
    # random initialization of w
    w = [random.random() for i in range(len(data[0] + 1))]
    
    # shuffle points
    random.shuffle(data)
    
    # derivative of mle cost function
    #dw
    # update w
    #w = w - a * dw
    
    pass


def main():
    print(get_labels(sentiment_tokenization.combined_data, )[0])