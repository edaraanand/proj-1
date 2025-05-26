import pandas as pd

# Dummy data for example
df = pd.DataFrame({
    'feature1': range(100),
    'feature2': range(100, 200),
    'target': [0 if i < 50 else 1 for i in range(100)]
})

df.to_csv('data/dataset.csv', index=False)
print("Data saved to data/dataset.csv")
