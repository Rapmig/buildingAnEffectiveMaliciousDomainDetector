import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


df = pd.read_csv("Done/Output Final/DNSModelInputWSpam50.csv")
df.head()
#model on target (0 or 1) and rest are x variables

y=df['target']

X = pd.get_dummies(df.drop(['target'], axis = 1))

# View count of each class
y.value_counts()

# Split features and target into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, stratify=y)

# Instantiate and fit the RandomForestClassifier
forest = RandomForestClassifier()
forest.fit(X_train, y_train)

# Make predictions for the test set
y_pred_test = forest.predict(X_test)

# View accuracy score
print(accuracy_score(y_test, y_pred_test))

# View the classification report for test data and predictions
print(classification_report(y_test, y_pred_test))