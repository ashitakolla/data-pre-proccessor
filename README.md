#  Smart Expense Tracker

**Smart Expense Tracker** is a web-based application that allows users to **upload receipts**, extract **itemized billing details using OCR**, and **track expenses by category** to help manage personal budgets more effectively.

---

## ✅ Features

- Upload receipt images (JPG/PNG)  
- Extract items and prices using OCR (Optical Character Recognition)  
- Automatically compute total expenses from receipt  
- Categorize each item (Groceries, Dining, Stationery, etc.)  
- Budget tracking per category  
- View total and category-wise expenses  
- Beautiful and responsive UI using Bootstrap 5

---

##  Tech Stack

- **Frontend**: HTML5, Bootstrap 5, Jinja2 templating  
- **Backend**: Flask (Python)  
- **OCR**: `pytesseract` + `Pillow`  
- **Data Handling**: Python dictionaries / JSON  
- **Optional**: SQLite (for persistent storage)

---

##  Installation

1. **Clone the repo**:
   ```bash
   git clone https://github.com/your-username/smart-expense-tracker.git
   cd smart-expense-tracker
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the app**:  
   Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser

---

##  Folder Structure

```
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
├── requirements.txt
└── README.md
```

---

##  Future Improvements

- Add login/authentication  
- Export reports (PDF/Excel)  
- Real-time visualizations  
- Cloud storage integration  

---

##  License

This project is licensed under the [MIT License](LICENSE).

