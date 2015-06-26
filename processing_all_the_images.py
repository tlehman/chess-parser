from preprocess_images import *
import os
import numpy as np

img_dir = "ref/"
images = [img_dir+f for f in os.listdir(img_dir)]
labels = [f.split("/")[1][:-5] for f in images]

data = []
for image in images:
    img = img_to_matrix(image)
    img = flatten_image(img)
    img = np.array(img)
    data.append(img)

print len(data)

