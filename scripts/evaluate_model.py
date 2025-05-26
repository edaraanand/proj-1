import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

df = pd.read_csv('data/dataset.csv')
X = df[['feature1', 'feature2']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = joblib.load('models/model-1.pkl')
predictions = model.predict(X_test)
classification_report = classification_report(y_test, predictions)
accuracy = accuracy_score(y_test, predictions)

print(f"Classification Report: \n {classification_report}")
print(f"Model Accuracy: {accuracy:.2f}")