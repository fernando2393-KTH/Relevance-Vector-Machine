import numpy as np
from sklearn.ensemble import AdaBoostClassifier
from sklearn import svm
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import rvm_classification
import Kernel

def calculateErrorRate(pred_labels, real_labels):
    cnt = 0
    for i in range(len(pred_labels)):
        if (pred_labels[i] != real_labels[i]):
            cnt += 1
    return cnt / len(real_labels)    

"""
data_set = "ctg"
data_set_index = 1

training_data = np.loadtxt(
                "datasets/{data_set}/{data_set}_train_data_{index}.asc".format(data_set=data_set, index=data_set_index))
training_labels = np.loadtxt(
                "datasets/{data_set}/{data_set}_train_labels_{index}.asc".format(data_set=data_set, index=data_set_index))
training_labels[training_labels == -1] = 0  # Sanitize labels, some use -1 so we force it to 0

test_data = np.loadtxt(
                "datasets/{data_set}/{data_set}_test_data_{index}.asc".format(data_set=data_set, index=data_set_index))
test_labels = np.loadtxt(
                "datasets/{data_set}/{data_set}_test_labels_{index}.asc".format(data_set=data_set,
                                                                                index=data_set_index))
test_labels[test_labels == -1] = 0  # Sanitize labels, some use -1 so we force it to 0
"""
"""
iris_dataset = load_iris()
y = iris_dataset.target
X = iris_dataset.data
training_data, test_data, training_labels, test_labels = train_test_split(X, y, test_size=0.5, random_state=42)
"""

"""
data = pd.read_csv("datasets/banknote/banknote.csv", delimiter=";", header=None)
data = pd.DataFrame(data)
columns = data.columns.tolist()
y = np.array(data[len(columns)-1])
y[y == -1] = 0
X = np.array(data[range(len(columns)-2)])
training_data, test_data, training_labels, test_labels = train_test_split(X, y, test_size=0.5, random_state=42)
"""

"""
# SVM Classification
clf = svm.SVC(kernel=Kernel.gaussian_kernel)
clf.fit(training_data, training_labels)
predictions = clf.predict(test_data)
print("Normal SVM error is:\t", calculateErrorRate(np.array(predictions), np.array(test_labels)))
print("SVM Vectors:", len(clf.support_))
"""

"""
# Boosted Classification
clf = AdaBoostClassifier(svm.SVC(probability=True, kernel=Kernel.combination_spherical_t_student_kernel), n_estimators=50, learning_rate=1.0, algorithm='SAMME')
clf.fit(training_data, training_labels)
predictions = clf.predict(test_data)
print("Adaboost error is:\t", calculateErrorRate(np.array(predictions), np.array(test_labels)))
estimators = clf.estimators_
num = 0
for est in estimators:
    num += len(est.support_)
print("SVM Boosted Vectors:\t", round(num/len(estimators)))
"""

"""
# RVM Classification
clf = rvm_classification.RVM_Classifier(None)
clf.set_training_data(training_data, training_labels)
clf.fit()
predictions = clf.predict(test_data)
print("Normal RVM error is:\t", calculateErrorRate(predictions, test_labels))
print("RVM Vectors:", clf.get_nr_relevance_vectors())
"""