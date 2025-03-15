import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, classification_report

# Example of a synthetic dataset
data = {
    'Math_Proficiency': [85, 70, 90, 65, 78],
    'Science_Proficiency': [80, 75, 95, 60, 85],
    'English_Proficiency': [75, 80, 70, 85, 80],
    'Coding_Skills': [60, 50, 70, 40, 65],
    'Communication_Skills': [80, 85, 75, 90, 85],
    'Chosen_Profession': ['Engineer', 'Doctor', 'Software Developer', 'Artist', 'Engineer']
}

df = pd.DataFrame(data)

# Encode categorical variable 'Chosen_Profession'
le = LabelEncoder()
df['Chosen_Profession'] = le.fit_transform(df['Chosen_Profession'])

# Split the data into features (X) and target variable (y)
X = df.drop('Chosen_Profession', axis=1)
y = df['Chosen_Profession']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize numerical features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create a Random Forest classifier
model = RandomForestClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)


# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print(f'Model Accuracy: {accuracy}')
print('Classification Report:\n', classification_rep)

