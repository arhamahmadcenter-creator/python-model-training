import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier

# Load CSV dataset
data = pd.read_csv("students.csv")

# Separate input and output
x = data[["Study_Hours", "Attendance"]]
y = data["Result"]

# Create Decision Tree model
model = DecisionTreeClassifier(
     max_depth=3,
 random_state=42
)
# Train the model
model.fit(x, y)

# Save the trained model
joblib.dump(model, "model.pk1")

print("Decision Tree training completed!")
print("Model saved successfully.")
print("Training accuracy:", model.score (x, y) * 100, "%")