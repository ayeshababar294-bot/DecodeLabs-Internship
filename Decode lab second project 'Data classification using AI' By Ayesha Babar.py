# ==========================================================
# DecodeLabs AI Internship
# Project 2: Data Classification Using AI
# Name: Ayesha Babar
# ==========================================================

# Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# -----------------------------
# Step 1: Load Dataset
# -----------------------------
print("Loading Iris Dataset...")

iris = load_iris()

X = iris.data
y = iris.target

print("Dataset Loaded Successfully!")
print("Total Samples :", len(X))
print("Total Features:", len(X[0]))
print("Classes :", iris.target_names)

# -----------------------------
# Step 2: Split Dataset
# -----------------------------
print("\nSplitting Dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# -----------------------------
# Step 3: Create Model
# -----------------------------
print("\nCreating Decision Tree Classifier...")

classifier = DecisionTreeClassifier(random_state=42)

# -----------------------------
# Step 4: Train Model
# -----------------------------
print("Training Model...")

classifier.fit(X_train, y_train)

print("Model Trained Successfully!")

# -----------------------------
# Step 5: Test Model
# -----------------------------
print("\nTesting Model...")

predictions = classifier.predict(X_test)

# -----------------------------
# Step 6: Display Predictions
# -----------------------------
print("\nActual\t\tPredicted")

for actual, predicted in zip(y_test, predictions):
    print(
        iris.target_names[actual],
        "\t",
        iris.target_names[predicted]
    )

# -----------------------------
# Step 7: Calculate Accuracy
# -----------------------------
accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy = {:.2f}%".format(accuracy * 100))

# -----------------------------
# Step 8: Predict New Data
# -----------------------------
print("\nPredicting New Flower...")

new_flower = [[5.1, 3.5, 1.4, 0.2]]

result = classifier.predict(new_flower)

print("Input:", new_flower)
print("Predicted Flower:", iris.target_names[result[0]])

print("\nProject Completed Successfully!")