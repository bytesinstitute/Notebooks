import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
np.random.seed(42)

num_rows = 1000

data = {
    "CustomerID": [f"CUST_{i:04d}" for i in range(1, num_rows+1)],
    "Name": [fake.name() for _ in range(num_rows)],
    "Age": np.random.randint(18, 70, num_rows).astype(float),
    "Gender": np.random.choice(["Male", "Female", "Other"], num_rows, p=[0.45, 0.45, 0.1]),
    "Email": [fake.email() if np.random.rand() > 0.1 else np.nan for _ in range(num_rows)],
    "City": np.random.choice(["New York", "London", "Tokyo", "Paris", "Sydney"], num_rows),
    "Signup_Date": [fake.date_between(start_date="-3y", end_date="today") for _ in range(num_rows)],
    "Last_Login": [fake.date_time_between(start_date="-1y", end_date="now") if np.random.rand() > 0.2 else np.nan for _ in range(num_rows)],
    "Subscription_Type": np.random.choice(["Basic", "Premium", "Enterprise"], num_rows, p=[0.6, 0.3, 0.1]),
    "Monthly_Charges": np.round(np.random.uniform(10, 200, num_rows), 2),
    "Total_Spend": np.round(np.random.uniform(100, 5000, num_rows), 2),
    "Ratings": np.round(np.random.uniform(1, 5, num_rows), 1),
    "Satisfaction_Score": np.random.randint(1, 11, num_rows),
    "Is_Premium": np.random.choice([True, False], num_rows, p=[0.3, 0.7])
}

data["Age"][np.random.choice(num_rows, int(num_rows*0.1), replace=False)] = np.nan
data["Total_Spend"][np.random.choice(num_rows, int(num_rows*0.05), replace=False)] = np.nan

df = pd.DataFrame(data)

df.to_csv("practice_dataset.csv", index=False)