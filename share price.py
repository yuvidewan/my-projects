import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from datetime import datetime

# Load data
data = yf.Ticker("^BSESN").history(period="1y")
closes = np.array(data['Close'])
dates = data.index
X = np.arange(len(closes)).reshape(-1, 1)
y = closes

# Polynomial regression (degree 7 for curve)
poly = PolynomialFeatures(degree=7)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

# Predict
y_pred = model.predict(X_poly)

# Define your future date (e.g., '2025-05-10')
future_date_str = '2025-04-21'
future_date = datetime.strptime(future_date_str, '%Y-%m-%d')

# Get the last available date in the dataset
last_date = data.index[-1].to_pydatetime().replace(tzinfo=None)

# Calculate the difference in days between the future date and the last date in the data
days_to_predict = (future_date - last_date).days

# Predict using polynomial regression for the future date
future_day = np.array([[len(closes) + days_to_predict]])  # Adding to the last index
future_day_poly = poly.transform(future_day)
predicted_price = model.predict(future_day_poly)[0]

# Print result
print(f"Predicted closing price on {future_date_str} is ₹{predicted_price:.2f}")

# Plot
plt.figure(figsize=(12, 6))
plt.plot(dates, y, label='Actual Prices')
plt.plot(dates, y_pred, label='Polynomial Regression (deg 7)', color='red')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Stock Price with Polynomial Regression')
plt.legend()
plt.grid(True)
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()
