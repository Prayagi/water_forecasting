import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ---------------- LOAD DATA ----------------
data = pd.read_csv("newDataset_with_demand.csv")

# Clean column names
data.columns = data.columns.str.strip()
data.dropna(inplace=True)

print("Columns:", data.columns)

# ---------------- FEATURES ----------------
features = ["population", "capacity", "inflow", "outflow", "reservoirlevel"]
target = "Water_Demand"

# Safety check
for col in features + [target]:
    if col not in data.columns:
        raise ValueError(f"❌ Column '{col}' not found")

X = data[features]
y = data[target]

# ---------------- SPLIT ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------- RANDOM FOREST ----------------
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\n🔹 Random Forest")
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2:", r2_score(y_test, y_pred))

# ---------------- LINEAR REGRESSION ----------------
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred_lr = lin_reg.predict(X_test)

# ---------------- USER INPUT ----------------
print("\n--- Enter Input Values ---")

population = int(input("Population: "))
capacity = float(input("Capacity: "))
inflow = float(input("Inflow: "))
outflow = float(input("Outflow: "))
reservoirlevel = float(input("Reservoir Level: "))

new_data = pd.DataFrame({
    "population": [population],
    "capacity": [capacity],
    "inflow": [inflow],
    "outflow": [outflow],
    "reservoirlevel": [reservoirlevel]
})

future = model.predict(new_data)[0]
print(f"\n✅ Predicted Water Demand: {future:.2f}")

# ---------------- VISUALIZATION ----------------

# Feature Importance
plt.figure()
sns.barplot(x=model.feature_importances_, y=features)
plt.title("Feature Importance")
plt.show()

# RF Plot
plt.figure()
plt.scatter(y_test, y_pred)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.title("RF: Actual vs Predicted")
plt.show()

# LR Plot
plt.figure()
plt.scatter(y_test, y_pred_lr)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.title("LR: Actual vs Predicted")
plt.show()

# Histogram
plt.figure()
sns.histplot(y_pred, bins=20)
plt.axvline(future, color='red')
plt.title("Prediction Distribution")
plt.show()

# Input vs Prediction
labels = ["Pop", "Cap", "In", "Out", "Level", "Pred"]
values = [population, capacity, inflow, outflow, reservoirlevel, future]

plt.figure()
plt.bar(labels, values)
plt.title("Input vs Prediction")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score  
import joblib 
import numpy as np   

# import pandas as pd
# import numpy as np

# Load your dataset
data = pd.read_csv("newDataset.csv")

# Clean column names
data.columns = data.columns.str.strip()

# Set seed (same result every time)
np.random.seed(42)

# =========================
# ADD WATER DEMAND COLUMN
# =========================

data['Water_Demand'] = (
    data['population'] * 0.2 +          # main driver
    data['outflow'] * 0.25 +            # usage
    data['inflow'] * 0.15 +             # supply effect
    data['reservoirlevel'] * 0.05 -     # storage impact
    data['annual'] * 0.1 +              # rainfall reduces demand
    np.random.normal(0, 10, len(data))  # realistic noise
)

# Ensure no negative values
data['Water_Demand'] = data['Water_Demand'].abs()

# =========================
# SAVE UPDATED DATASET
# =========================

data.to_csv("newDataset_with_demand.csv", index=False)

print("✅ Water_Demand column added successfully!")

missing_values = data.isnull().sum().sort_values(ascending=False)
missing_values

data.columns

c_columns = data.select_dtypes(include=['object','category']).columns
print("Categorical Columns: ")
print(c_columns)

LE = LabelEncoder()
c_column = ['district', 'state_ut_name']

for col in c_column:
    data[col] = LE.fit_transform(data[col])

data

# Clean column names
data.columns = data.columns.str.strip()

# data['Water_Demand'] = (
#     data['population'] * 0.2 +
#     data['reservoirlevel'] * 0.1 +
#     data['capacity'] * 0.05 +
#     np.random.normal(0, 10, len(data))
# )

# slight variation
# data['Water_Demand'] = data['Water_Demand'] * np.random.uniform(0.9, 1.1, len(data))

c_columns = data.select_dtypes(include=['object','category']).columns
print("Categorical Columns:", c_columns)

le = LabelEncoder()

for col in c_columns:
    data[col] = le.fit_transform(data[col])

features = [
    'capacity',
    'year',
    'jan-feb',
    'jun-sep',
    'mar-may'
]

X = data[features]
y = data['Water_Demand']

# from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(
    n_estimators=150,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

# from sklearn.metrics import r2_score, mean_squared_error

y_pred = model.predict(X_test)

print("R2 Score:", r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))

from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)

print("CV Score:", scores.mean())

import joblib

joblib.dump(model, "water_model.pkl")

import seaborn as sns

sns.histplot(data['Water_Demand'], kde=True)
plt.title("Improved Water Demand Distribution")
plt.show()