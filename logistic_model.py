'''
Links:
    https://zlatankr.github.io/posts/2017/03/06/mle-gradient-descent
    https://machinelearningmastery.com/implement-logistic-regression-stochastic-gradient-descent-scratch-python/
    
'''

import json
import math
import numpy as np
import random
import matplotlib.pyplot as plt

'''
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
    return combined_data
'''

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


def logistic_func(w, x):
    z = np.dot(w,x)
    f = 1 / (1 + math.e ** -z)
    return f


def mle(x, label, w):
    
    cost = -1 * (label * math.log(logistic_func(w,x)) + (1-label) * math.log(1 - logistic_func(w,x)))

    return cost


def SGD(data, labels, a, w):
    
    #w = [random.random() for i in range(len(data[0] + 1))]
    
    # shuffle points
    random.shuffle(data)
    
    cost = []
    
    for d in range(len(data)):
        
        update = []
        cost.append(mle(d, labels[d], w))
        
        for i in range(len(w)):
            # need a temp list to store updates to each item in w
            temp =  w - a * (logistic_func(w, data[d]) - labels[d]) * data[i]
            update.append(temp)
            
        # update all items in w simultaneously
        update = np.array(update)
        w = w - a * update

    return w, cost


def main():
    
    labeled_data = []
    with open('labeled_tweets.json') as json_file:
        for line in json_file:
            labeled_data.append(json.loads(line))
    print(labeled_data[0])
    
    # get just the relevant variables we are using 
    data = []
    labels = []
    for d in labeled_data:
        data.append([1, d["sentiment"][0] ,  d["sentiment"][1], d["price"]])
        labels.append(d["label"])
    
    print(data[0])
    
    epochs = 10
    a = 0.001
    w = np.zeros(len(data[0])+1)
    cost = []
    
    for e in range(epochs):
        w, c = SGD(data, labels, a, w)
        cost.append(c)
        
    print(w)
        
    # plot cost function 
    plt.plot(range(10), [sum(i) for i in cost])
    plt.title('Cost per Epoch of SGD')
    plt.xlabel('Epoch')
    plt.ylabel('Cost')
    plt.show()
    
    
main()
