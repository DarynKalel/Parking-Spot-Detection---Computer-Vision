import os
import pickle

import numpy as np
from skimage.io import imread
from skimage.transform import resize
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

#1 Prepare the Data

input_dir = 'C:/Users/Alikh/Downloads/clf-data'
categories = ['empty', 'not_empty']

data = []
labels = []

for category_idx, category in enumerate(categories):
    for file in os.listdir(os.path.join(input_dir, category)):
        img_path = os.path.join(input_dir, category, file)
        img = imread(img_path)
        img = resize(img, (15, 15))
        data.append(img.flatten())
        labels.append(category_idx)

data = np.asarray(data)
labels = np.asarray(labels)

#2 Split data into train and test
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

#3 Train Data
classifier = SVC()
parameters = [{'gamma':[0.01, 0.001, 0.001], 'C':[1, 10, 100, 1000]}]
grid_search = GridSearchCV(classifier, parameters)
grid_search.fit(x_train, y_train)

#4 Test Data
best_classifier = grid_search.best_estimator_
y_predictor = best_classifier.predict(x_test)
score = accuracy_score(y_predictor, y_test)
print('{}% of samples were correctly classified'.format(str(score*100)))

pickle.dump(best_classifier, open('C:/Users/Alikh/Downloads/models.p', 'wb'))