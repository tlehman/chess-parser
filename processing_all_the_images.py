from preprocess_images import *
import os
import numpy as np
import pandas as pd
import pylab as pl
from sklearn.decomposition import RandomizedPCA
from sklearn import svm

img_train_dir = "ref/pieces/"
img_test_dir = "tmp/027/"

# the trainingset is an array of (vector,label) pairs
images_training = [img_train_dir+f for f in os.listdir(img_train_dir)]
images_test = [img_test_dir+f for f in os.listdir(img_test_dir)]
"0 is blank, odd positive numbers are black, even postives are white, etc."
label_codes = {"_": 0, "BP": 1, "WP": 2,
                       "BR": 3, "WR": 4,
                       "BN": 5, "WN": 6,
                       "BB": 7, "WB": 8,
                       "BQ": 9, "WQ": 10,
                       "BK": 11,"WK": 12}

def label_from_code(c):
    return [label for label, code in label_codes.items() if code == c][0]


labels = [f.split("/")[-1][:-7] for f in images_training]
target = [label_codes[label] for label in labels]

data_training = []
for image in images_training:
    img = img_to_matrix(image)
    img = flatten_image(img)
    data_training.append(img)

data_test = []
for image in images_test:
    img = img_to_matrix(image)
    img = flatten_image(img)
    data_test.append(img)

data_training = np.array(data_training)
data_test = np.array(data_test)


# using a randomized PCA, reducing to 25 dimensions (from 7500 dimensions)
pca = RandomizedPCA(n_components=25)
X = pca.fit_transform(data_training)
X_test = pca.fit_transform(data_test)

# make a linear support vector classifier
clf = svm.LinearSVC()
clf.fit(X, target)

# check classified images
for i, x in enumerate(X_test):
    predicted = clf.predict(x)[0]
    label = label_from_code(predicted)
    print "%s  is  %s" % (images_test[i], label)
