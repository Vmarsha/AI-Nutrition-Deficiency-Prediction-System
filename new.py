import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load Excel dataset
df = pd.read_excel("symptom_deficiency_dataset.xlsx")

# Remove missing rows
df.dropna(inplace=True)

# Display preview
print("Dataset Preview:")
print(df.head())

# Features and target
X = df.drop("Deficiency", axis=1)
y = df["Deficiency"]

# Convert categorical columns
X = pd.get_dummies(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model saved successfully as model.pkl")