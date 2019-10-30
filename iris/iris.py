from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
import pickle
import pandas as pd
import numpy as np
iris = datasets.load_iris()

x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.5)

classifier = tree.DecisionTreeClassifier()
classifier.fit(x_train, y_train)
predictions = classifier.predict(x_test)
data = {
  "petal_length": 1.4,
  "petal_width": 0.3,
  "sepal_length": 5.2,
  "sepal_width": 3.6
}
target_names = ['setosa', 'versicolor', 'virginica']
print(target_names)
data = pd.DataFrame(data, index=[0]).T
data = [data[0]]

print(accuracy_score(y_test, predictions))
xx=(classifier.predict(data))
print(target_names[x in xx])

filename = 'model.sav'
pickle.dump(classifier, open(filename, 'wb'))
