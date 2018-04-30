from file_manipulation import csv_f
import json
import math
import numpy as np
import random
from sentiment_tokenization import combined_data
from textblob import TextBlob

def get_labels(combined_data, csv_f):
    # combined data has "timestamp", "tweet", "sentiment"
    # csv_f has the label indicating price movement
    # give each tweet the same label based on timestamp
    
    for tweet in combined_data:
        ts = tweet["timestamp"]
        #tweet["label"] = 
    pass


def split_data(data):
    # divide data into training, validation, and test sets
    with open(json_file, 'r') as read_file:
        data = json.load(read_file)
        
    # ALSO NEED TO MAKE SURE THAT THE DATES WE HAVE TWEETS FOR AND THE DATES WE
    # HAVE PRICE DATA FOR ARE THE SAME SO THAT WE AREN'T USING EXTRANEOUS DATA? 
    
        
    # randomly shuffle data in place
    # not sure if this works-- does json.load return a list of JSON objects?
    random.shuffle(data)
    
    training_len = math.ceil(len(data) * 0.8)
    validation_len = len(data) - training_len 
    test_len = len(data) - validation_len - training_len
    
    training = data[:training_len]
    validation = data[training_len:test_len]
    test = data[test_len:]
    
    return training, validation, test

def logistic_func(w, x, b):
    z = np.dot(w,x)
    f = 1 / (1 + math.e ** -z)
    return f

def mle(x, y, w, b, cost_history):
    # cost_history is a list of the cost after each iteration of SGD
    temp = 0
    m = len(x)
    for i in range(m):
        temp += y[i] * math.log(logistic_func(w, x[i], b[i])) + \
        (1 - y[i]) * math.log( 1 - logistic_func(w, x[i], b[i]))
    J = -(1 / m) * temp
    cost_history.append(J)
    return J, cost_history

#try a different gradient descent algorithm? 
def SGD(data, a):
    # random initialization of w
    w = [random.random() for i in range(len(data[0]))]
    
    # shuffle points
    random.shuffle(data)
    
    # derivative of mle cost function
    dw 
    # update w
    w = w - a * dw
    
    pass

def main():
    print(csv_f[:5])