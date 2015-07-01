from preprocess_images import *
import os
import numpy as np
import pandas as pd
import pylab as pl
from random import randint
from sklearn.decomposition import RandomizedPCA
from sklearn import svm

img_dir = "ref/pieces/"

images = [img_dir+f for f in os.listdir(img_dir)]
# we want to train the classifier on 80% of the given data, and test on the other 20%
training_or_test = [randint(0,100) < 80 for i in images]
img_group = zip(images, training_or_test)
images_training = filter(lambda p: p[1], img_group)
images_test = filter(lambda p: not p[1], img_group)


"0 is blank, odd positive numbers are black, even postives are white, etc."
label_codes = {"_": 0, "BP": 1, "WP": 2,
                       "BR": 3, "WR": 4,
                       "BN": 5, "WN": 6,
                       "BB": 7, "WB": 8,
                       "BQ": 9, "WQ": 10,
                       "BK": 11,"WK": 12}

def label_from_code(c):
    return [label for label, code in label_codes.items() if code == c][0]


labels = [f[0].split("/")[-1][:-7] for f in images_training]
target = [label_codes[label] for label in labels]

def images_to_vectors(images):
    vectors = []
    for image in images:
        image = image[0]
        img = img_to_matrix(image)
        img = flatten_image(img)
        vectors.append(img)
    return np.array(vectors)

data_training = images_to_vectors(images_training)
data_test = images_to_vectors(images_test)

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
