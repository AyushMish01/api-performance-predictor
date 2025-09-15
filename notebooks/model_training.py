# notebooks/model_training.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import os

# Absolute path to data folder
data_file = r"C:\Users\ravir\OneDrive\Desktop\ayushproject\api-performance-predictor\data\api_logs.csv"

# Load data
df = pd.read_csv(data_file)

# Encode endpoint as numeric
le = LabelEncoder()
df['endpoint_encoded'] = le.fit_transform(df['endpoint'])

# Features and target
X = df[['traffic_rate','endpoint_encoded']]
y = df['latency_ms']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model and encoder
model_folder = r"C:\Users\ravir\OneDrive\Desktop\ayushproject\api-performance-predictor\model"
os.makedirs(model_folder, exist_ok=True)
joblib.dump(model, os.path.join(model_folder, "api_latency_model.pkl"))
joblib.dump(le, os.path.join(model_folder, "endpoint_encoder.pkl"))

print("Model and encoder saved in model/ folder")
