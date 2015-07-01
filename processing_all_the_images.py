from preprocess_images import *
import os
import numpy as np
import pandas as pd
import pylab as pl
from random import randint
from sklearn.decomposition import RandomizedPCA
from sklearn.neighbors import KNeighborsClassifier

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

# using a randomized PCA, reducing to 13 dimensions (from 7500 dimensions)
pca = RandomizedPCA(n_components=13)
X = pca.fit_transform(data_training)
X_test = pca.fit_transform(data_test)

# make a linear support vector classifier
knn = KNeighborsClassifier()
knn.fit(X, target)

# check classified images
number_correct = 0
number_total = len(X_test)
for i, x in enumerate(X_test):
    predicted = knn.predict(x)[0]
    label = label_from_code(predicted)
    image = images_test[i][0]

    correct = image.startswith(img_dir + label)
    if correct:
        number_correct += 1
    print "%s  is  %s (%r)" % (image, label, correct)

percent_correct = 100*float(number_correct)/float(number_total)
print "%d correct out of %d, %d percent accurate" % (number_correct, number_total, percent_correct)
