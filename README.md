# 🩺 Predictive Pulse: Harnessing Machine Learning for Blood Pressure Analysis

A **machine learning–powered web application** that predicts systolic and diastolic blood pressure from patient data.  
Built with **Python** and **Flask**, it’s designed for healthcare professionals and researchers who need quick, accurate, and accessible predictions

---

## ✨ Features

- 📊 **Accurate Predictions** — Uses ML models to estimate blood pressure
- 📂 **Multiple Input Modes** — Upload CSV files or enter data manually
- 📈 **Interactive Visualizations** — Analyze and interpret results visually
- 💾 **Downloadable Reports** — Export predictions in a structured format
- 🏥 **Healthcare-Ready** — Designed with clinical use in mind

---

## 🛠 Technology Stack

**Backend:** Python, Flask  
**Frontend:** HTML, CSS, Bootstrap  
**Machine Learning:** scikit-learn  
**Data Processing:** pandas, NumPy  
**Model Storage:** joblib  

---

## ⚙️ Installation & Setup

### 1️⃣ Prerequisites
- Python **3.8+**
- pip (Python package manager)

### 2️⃣ Steps

```bash
# Clone the repository
git clone https://github.com/adhikarilaxman/Predictive-Pulse-Harnessing-Machine-Learning-for-Blood-Pressure-Analysis.git
cd Predictive-Pulse-Harnessing-Machine-Learning-for-Blood-Pressure-Analysis

# Create and activate a virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py


📂 Project Structure
Predictive-Pulse-Harnessing-Machine-Learning-for-Blood-Pressure-Analysis/
├── app.py                # Main Flask app
├── forms.py              # WTForms for data input
├── model.joblib          # Trained ML model
├── data/                 # Sample patient data
├── img/                  # Images and icons
├── static/               # Static files (CSS, JS)
├── templates/            # HTML templates
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation


🤝 Contributing
Contributions are always welcome!

Fork the repository

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit changes (git commit -m 'Add some AmazingFeature')

Push to your branch (git push origin feature/AmazingFeature)

Open a Pull Request
