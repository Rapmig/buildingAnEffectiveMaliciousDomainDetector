import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
def convert(data):
    number = preprocessing.LabelEncoder()
    data['domainName'] = number.fit_transform(data.domainName)
    data=data.fillna(-999)
    return data


data = pd.read_csv("Done/Output Final/DNSModelInput.csv")
data.head()
#model on target (0 or 1) and rest are x variables

y=data['target']

X = pd.get_dummies(data.drop(['target'], axis = 1))

print(f'X : {X.shape}')
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=101)
print(f'X_train : {X_train.shape}')
print(f'y_train : {y_train.shape}')
print(f'X_test : {X_test.shape}')
print(f'y_test : {y_test.shape}')




rf_Model = RandomForestClassifier()


rf_Model.fit(X_train,y_train)



print (f'Train Accuracy - : {rf_Model.score(X_train,y_train):.3f}')
print (f'Test Accuracy - : {rf_Model.score(X_test,y_test):.3f}')

