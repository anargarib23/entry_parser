
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score

from yellowbrick.classifier import ClassificationReport, ConfusionMatrix

import yaml
import numpy as np
import pandas as pd
import seaborn as sns
import os

import pickle5 as pickle
from datetime import datetime

with open('./params/params.yaml', 'r') as stream:
	params = yaml.safe_load(stream)

pd.set_option('display.max_rows', None)



df = pd.read_csv(params["dataset-path"], usecols=['wiki', 'content'])*1



df = df.sample(frac=1)

cv = CountVectorizer()
X = cv.fit_transform(df['content'])

X = np.array(X.todense())
y = df['wiki']

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    stratify=y)


model = MultinomialNB().fit(X_train, y_train)

y_pred = model.predict(X_test)

print('Accuracy:', accuracy_score(y_test, y_pred))
print('F1 score:', f1_score(y_test, y_pred, average="macro"))

report = ClassificationReport(model, classes=['nonwiki', 'wiki'], support=True, title='Classification Report')
confusion_matrix = ConfusionMatrix(model, classes=['nonwiki', 'wiki'], title='Confusion Matrix')

confusion_matrix.fit(X_train, y_train)
confusion_matrix.score(X_test, y_test)
confusion_matrix.show()

report.fit(X_train, y_train)
report.score(X_test, y_test)
report.show()


directory = params["model-path"] + '/NB Classifier ' + datetime.now().strftime("%m-%d-%Y %H:%M:%S")
os.mkdir(directory)

model_file = open(directory + '/model', 'wb')
vectorizer_file = open(directory + '/vectorizer', 'wb')
report_file = open(directory + '/classification_report', 'wb')
matrix_file = open(directory + '/confusion_matrix', 'wb')

pickle.dump(model, model_file)
pickle.dump(cv, vectorizer_file)
pickle.dump(report, report_file)
pickle.dump(confusion_matrix, matrix_file)
