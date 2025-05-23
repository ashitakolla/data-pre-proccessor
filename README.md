Smart Expense Tracker
Smart Expense Tracker is a web-based application that allows users to upload receipts, extract itemized billing details using OCR, and track expenses by category to help manage personal budgets more effectively.

✅ Features
Upload receipt images (JPG/PNG)

Extract items and prices using OCR (Optical Character Recognition)

Automatically compute total expenses from receipt

Categorize each item (Groceries, Dining, Stationery, etc.)

Budget tracking per category

View total and category-wise expenses

Responsive UI with Bootstrap 5

 Tech Stack
Frontend: HTML5, Bootstrap 5, Jinja2 templating

Backend: Flask (Python)

OCR: pytesseract + Pillow

Data Handling: Python dictionaries / JSON

Optional: SQLite (for persistent storage)

 Installation
Clone the repo:

bash
Copy
Edit
git clone https://github.com/your-username/smart-expense-tracker.git
cd smart-expense-tracker
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
python app.py
Visit: http://127.0.0.1:5000

📂 Folder Structure
cpp
Copy
Edit
smart-expense-tracker/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── styles.css
├── receipts/
├── processed_data/
├── utils/
│   └── ocr_processing.py
└── requirements.txt


 Future Improvements
Add login/authentication system

Export monthly reports (PDF/Excel)

Cloud storage integration (Google Drive, Dropbox)

Real-time charts and analytics
