import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Example dataset (replace with Kaggle dataset for real project)
data = {
    "rooms": [2, 3, 4, 5, 6],
    "size": [800, 1200, 1500, 2000, 2500],
    "price": [100000, 150000, 200000, 250000, 300000]
}
df = pd.DataFrame(data)

X = df[['rooms', 'size']]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Predicted:", pred)
print("MSE:", mean_squared_error(y_test, pred))
