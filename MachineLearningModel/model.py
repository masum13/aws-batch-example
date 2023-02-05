import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split

df = pd.read_csv('../InputData/titanic.csv')

## Cleaning up the code
df.drop(['Cabin'],axis=1,inplace=True)
df['Age'].fillna(df['Age'].mean(),inplace=True)

## Removing the string-data as it's not needed
df.drop(['Ticket','Name'],axis=1,inplace=True)
sex = pd.get_dummies(df['Sex'],drop_first=True)
embarked = pd.get_dummies(df['Embarked'],drop_first=True)
df.drop(['Sex','Embarked'],axis=1,inplace=True)
df = pd.concat([df,sex,embarked],axis=1)

## Preparing the train and test dataset
x = df.drop('Survived',axis=1)
y = df['Survived']

X_train, X_val, Y_train, Y_val = train_test_split(x,y, test_size = 0.05, random_state=42)

X_val.to_csv("../ExampleSet/SampleTestData.csv", index=False)
Y_val.to_csv("../ExampleSet/SamplePrediction.csv",index=False)

# Training the model
classifier = RandomForestClassifier()
classifier.fit(x, y)

# Package the model
joblib.dump(classifier, 'classifier.pkl')
