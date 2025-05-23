import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.impute import SimpleImputer

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
        # Create an imputer object depending on the strategy
        imputer = SimpleImputer(strategy=strategy)
        for column in self.data.columns:
            if self.data[column].isnull().sum() > 0:
                if self.data[column].dtype != 'object':
                    self.data[column] = imputer.fit_transform(self.data[[column]])
                    self.log.append(f"Missing values in '{column}' filled using {strategy}")
                else:
                    # Handle categorical missing values
                    self.data[column] = self.data[column].fillna(self.data[column].mode()[0])
                    self.log.append(f"Missing values in '{column}' filled using mode")

    def remove_duplicates(self):
        initial_rows = self.data.shape[0]
        self.data.drop_duplicates(inplace=True)
        removed = initial_rows - self.data.shape[0]
        if removed > 0:
            self.log.append(f"Removed {removed} duplicate rows")

    def fix_data_types(self):
        for column in self.data.columns:
            try:
                # Attempt conversion to numeric
                self.data[column] = pd.to_numeric(self.data[column], errors='ignore')
                # Additional checks could be added for datetime or categorical types
            except Exception:
                self.log.append(f"Data type adjustment failed for '{column}'")

    def scale_features(self, method='standard'):
        if method == 'standard':
            scaler = StandardScaler()
        elif method == 'minmax':
            scaler = MinMaxScaler()
        elif method == 'robust':
            scaler = RobustScaler()
        else:
            raise ValueError("Invalid scaling method")

        numeric_cols = self.data.select_dtypes(include=['float64', 'int64']).columns
        self.data[numeric_cols] = scaler.fit_transform(self.data[numeric_cols])
        self.log.append(f"Features scaled using {method} scaler")

    def export_data(self, output_path='cleaned_data.csv'):
        self.data.to_csv(output_path, index=False)
        with open("processing_log.txt", "w") as log_file:
            log_file.write("\n".join(self.log))
        print(f"Data cleaned and saved to {output_path}")
        print(f"Processing log saved to 'processing_log.txt'")

# Example Usage
file_path = r"C:\Users\Admin\Desktop\Research\EGG\Normalized_Data\normalized_sub01_hi.csv"
processor = DataPreprocessor(file_path)
processor.handle_missing_values(strategy='mean')
processor.remove_duplicates()
processor.fix_data_types()
processor.scale_features(method='standard')
processor.export_data()
