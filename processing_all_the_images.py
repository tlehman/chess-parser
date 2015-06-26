from preprocess_images import *
import os
import numpy as np
import pandas as pd
import pylab as pl
from sklearn.decomposition import RandomizedPCA

img_dir = "ref/"

# the trainingset is an array of (vector,label) pairs
images = [img_dir+f for f in os.listdir(img_dir)][:24]
labels = [f.split("/")[1][:-6] for f in images][:24]

data = []
for image in images:
    img = img_to_matrix(image)
    img = flatten_image(img)
    data.append(img)

data = np.array(data)

is_train = np.random.uniform(0, 1, len(data)) <= 0.7
y = np.where(np.array(labels)=="B", 1, 0)

train_x, train_y = data[is_train], y[is_train]
test_x, test_y = data[is_train==False], y[is_train==False]

# using a randomized PCA
pca = RandomizedPCA(n_components=2)
X = pca.fit_transform(data)
df = pd.DataFrame({"x": X[:, 0], "y": X[:, 1], "label":np.where(y==1, "black", "white")})
colors = ["black", "white"]
for label, color in zip(df['label'].unique(), colors):
    mask = df['label']==label
    pl.scatter(df[mask]['x'], df[mask]['y'], c=color, label=label)

pl.legend()
pl.show()
