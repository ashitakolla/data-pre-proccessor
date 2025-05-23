import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

class DataPreprocessor:
    def __init__(self, file_path):
        self.data = self.load_data(file_path)
        self.log = []

    def load_data(self, file_path):
        if file_path.endswith('.csv'):
            return pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            return pd.read_excel(file_path)
        elif file_path.endswith('.json'):
            return pd.read_json(file_path)
        else:
            raise ValueError("Unsupported file format")

    def handle_missing_values(self, strategy='mean'):
        for column in self.data.columns:
            if self.data[column].isnull().sum() > 0:
                if strategy == 'mean' and self.data[column].dtype != 'object':
                    self.data[column].fillna(self.data[column].mean(), inplace=True)
                elif strategy == 'mode':
                    self.data[column].fillna(self.data[column].mode()[0], inplace=True)
                self.log.append(f"Missing values in '{column}' filled using {strategy}")

    def remove_duplicates(self):
        initial_rows = self.data.shape[0]
        self.data.drop_duplicates(inplace=True)
        removed = initial_rows - self.data.shape[0]
        if removed > 0:
            self.log.append(f"Removed {removed} duplicate rows")

    def fix_data_types(self):
        for column in self.data.columns:
            try:
                self.data[column] = pd.to_numeric(self.data[column], errors='ignore')
            except Exception:
                self.log.append(f"Data type adjustment failed for '{column}'")

    def scale_features(self, method='standard'):
        scaler = StandardScaler() if method == 'standard' else MinMaxScaler()
        numeric_cols = self.data.select_dtypes(include=['float64', 'int64']).columns
        self.data[numeric_cols] = scaler.fit_transform(self.data[numeric_cols])
        self.log.append(f"Features scaled using {method} scaler")

    def export_data(self, output_path='cleaned_data.csv'):
        self.data.to_csv(output_path, index=False)
        with open("processing_log.txt", "w") as log_file:
            log_file.write("\n".join(self.log))
        print(f"Data cleaned and saved to {output_path}")
        print(f"Processing log saved to 'processing_log.txt'")

# Step 1: Preprocess the Data
file_path = r"C:/Users/Admin/Downloads/dirty data.csv"  # Fixed file path
processor = DataPreprocessor(file_path)
processor.handle_missing_values(strategy='mean')
processor.remove_duplicates()
processor.fix_data_types()
processor.scale_features(method='standard')
processor.export_data()



# Step 2: Prepare the Data for Model Training
# Assuming 'data' is the preprocessed DataFrame from your processor
data = processor.data  # Using the processed data from the DataPreprocessor

# Step 3: Split Data into Features (X) and Target (y)
# Replace 'target_column' with the actual column name you want to predict
X = data.drop('Consumer', axis=1)  # Drop the target column ('Consumer' here)
y = data['Consumer']  # 'Consumer' is the target variable

# Step 4: Split the Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Choose and Train a Model (e.g., RandomForestClassifier)
model = RandomForestClassifier()

# Train the model with the training data
model.fit(X_train, y_train)

# Step 6: Make Predictions on the Test Data
y_pred = model.predict(X_test)

# Step 7: Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Optional: Print a detailed classification report (for classification tasks)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Step 8: Save the Model (Optional)
joblib.dump(model, 'model.pkl')
print("Model saved to 'model.pkl'")
