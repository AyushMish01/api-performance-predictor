# notebooks/data_generation.py
import os
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Absolute path to project data folder
data_folder = r"C:\Users\Ravir\OneDrive\Desktop\ayushproject\api-performance-predictor\data"
os.makedirs(data_folder, exist_ok=True)

def generate_logs(n=10000, seed=42):
    random.seed(seed)
    np.random.seed(seed)
    start_time = datetime.now()
    data = []
    endpoints = ['/login', '/payment', '/search', '/profile']

    for i in range(n):
        ts = start_time + timedelta(seconds=i)
        endpoint = random.choice(endpoints)
        traffic = np.random.poisson(20) if endpoint != '/payment' else np.random.poisson(10)
        latency = np.random.normal(100, 20) + traffic * random.uniform(0.5, 1.5)
        latency = max(10, latency)  # avoid negative
        error_rate = max(0, np.random.normal(0.5, 0.3) + traffic / 100.0)
        data.append([ts, endpoint, int(traffic), float(latency), float(error_rate)])

    df = pd.DataFrame(data, columns=['timestamp','endpoint','traffic_rate','latency_ms','error_rate'])
    df.to_csv(os.path.join(data_folder, 'api_logs.csv'), index=False)
    print("Saved data/api_logs.csv with", len(df), "rows")

if __name__ == "__main__":
    generate_logs(n=10000)
