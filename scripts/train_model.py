import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv('data/dataset.csv')
X = df[['feature1', 'feature2']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

joblib.dump(model, 'models/model-1.pkl')
joblib.dump(model, 'models/model-1.joblib')
print("Model saved to models/model-1.pkl")
print("Model saved to models/model-1.joblib")
