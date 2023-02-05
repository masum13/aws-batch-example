import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

df = pd.read_csv('SampleTestData.csv')
classifier = joblib.load('classifier.pkl')
prediction = classifier.predict(df)

print(prediction)
