import os, sys, time, datetime
import pickle

import pandas as pd
import numpy as np
import torch
import sklearn

import pdb

data_all = pickle.load(open('data_all_copy.pkl', 'rb')).astype(np.float16)

mean = data_all.mean(axis=0)

std_dev = np.sqrt(np.square(data_all - mean).sum(axis=0) / (data_all.shape[0] - 1))

data_norm = (data_all - mean) / (std_dev + 1e-10)

pdb.set_trace()

pickle.dump(data_norm, open('data_norm.pkl', 'wb'))
