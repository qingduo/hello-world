from __future__ import print_function
import imageio
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import tarfile
from IPython.display import display, Image
from sklearn.linear_model import LogisticRegression
from six.moves.urllib.request import urlretrieve
from six.moves import cPickle as pickle
import random
import scipy

def show_pics(data_root):
    os.chdir(data_root)
    for dir_item in os.listdir(data_root):
        if os.path.isdir(dir_item):
            files=os.listdir(dir_item)
            print(dir_item," has", len(files), "files.")
            fullname=os.path.join(dir_item,files[random.randint(1,len(files))])
            print(fullname)
            display(Image(fullname))
        else:
            print(dir_item," is NOT a dir. Pass..")

data_1 = '/Users/kingdom/tensorflow/udacity/notMNIST_large'
data_2 = '/Users/kingdom/tensorflow/udacity/notMNIST_small'
show_pics(data_1)
show_pics(data_2)
