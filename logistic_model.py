import json
import numpy as np
import math

# divide data into training, validation, and test sets
#json format: 
with open('data_file.json', 'r') as read_file1:
    btc_tweet1 = json.load(read_file1)
    
    