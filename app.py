from flask import Flask, request, render_template, send_file
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler, MinMaxScaler

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

class DataPreprocessor:
    def __init__(self, data):
        self.data = data
        self.log = []

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
                self.data[column] = pd.to_numeric(self.data[column])
            except ValueError:
                self.log.append(f"Skipping column '{column}' due to conversion issues")

    def scale_features(self, method='standard'):
        scaler = StandardScaler() if method == 'standard' else MinMaxScaler()
        numeric_cols = self.data.select_dtypes(include=['float64', 'int64']).columns
        self.data[numeric_cols] = scaler.fit_transform(self.data[numeric_cols])
        self.log.append(f"Features scaled using {method} scaler")

    def export_data(self, output_path='processed_data.csv'):
        self.data.to_csv(output_path, index=False)
        with open("processing_log.txt", "w") as log_file:
            log_file.write("\n".join(self.log))
        return output_path

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']

        if uploaded_file.filename != '':
            file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(file_path)

            # Load data and process
            data = pd.read_csv(file_path)
            processor = DataPreprocessor(data)
            processor.handle_missing_values()
            processor.remove_duplicates()
            processor.fix_data_types()
            processor.scale_features()

            # Save processed file
            processed_path = os.path.join(PROCESSED_FOLDER, 'cleaned_data.csv')
            processor.export_data(processed_path)

            return send_file(processed_path, as_attachment=True)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
