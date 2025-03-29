# 💼 Income & Expenses Survey Tool

Absolutely! Here's a **detailed `README.md`** for your **Flask + MongoDB + Data Analysis + AWS Deployment** project. You can copy-paste this into your project’s `README.md` file and modify details like project name or author as needed.

---

```markdown
# 🧪 Income & Expense Survey Tool – Flask + MongoDB + Data Analytics

This project is a full-stack data collection and analysis tool designed to gather user information about income and spending patterns in preparation for launching a healthcare product. It includes a web interface built with Flask, stores data in MongoDB, processes and visualizes the data using Python and Jupyter Notebook, and is fully deployable on AWS EC2.

---

## 📦 Project Structure

```
final_project/
├── app.py                 # Main Flask application
├── export_data.py         # Extracts MongoDB data and exports to CSV
├── user_class.py          # "User" class for data formatting and export
├── data_processing.ipynb  # Jupyter Notebook for analysis and visualization
├── requirements.txt       # All dependencies
├── README.md              # You're here!
├── templates/
│   └── index.html         # HTML form for survey input
├── static/
│   └── style.css          # Optional styling
└── user_data.csv          # Generated data file (after export)
```

---

## 🚀 Features

- 📋 Web form to collect: Age, Gender, Income, and categorized Expenses
- 🧠 Data storage in MongoDB (local or remote via MongoDB Atlas)
- 📈 Visualizations in Jupyter:  
  - Top earning age groups  
  - Gender-based spending across categories
- 📤 Export charts as `.png` for PowerPoint/report use
- 🌍 Deployable on AWS EC2 with Gunicorn for production

---

## 🧰 Tech Stack

- **Frontend**: HTML, CSS (optional)
- **Backend**: Flask (Python)
- **Database**: MongoDB (via PyMongo)
- **Data Processing**: Pandas, Matplotlib
- **Hosting**: AWS EC2 (Ubuntu or Amazon Linux)
- **Environment**: Python 3.x, pip

---

## ⚙️ Installation & Local Setup

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv
.\venv\Scripts\activate   # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start MongoDB Locally
Ensure MongoDB is running locally (`mongod` command) or connect to MongoDB Atlas.

### 5. Run the Flask App
```bash
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📤 Export Data to CSV

After submitting data through the form:

```bash
python export_data.py
```

This will create a `user_data.csv` file.

---

## 📊 Run Data Analysis

Start Jupyter:

```bash
jupyter notebook
```

Open `data_processing.ipynb`, run the cells to:
- Analyze average income by age
- Visualize gender-based spending
- Save charts for reporting

---

## ☁️ Deploy on AWS EC2

### 1. Launch EC2 Instance
- Amazon Linux or Ubuntu
- Open ports: 22 (SSH), 80 (HTTP), 5000 (optional)

### 2. SSH Into the Instance
```bash
ssh -i "your-key.pem" ubuntu@your-ec2-public-ip
```

### 3. Install Dependencies
```bash
sudo apt update -y
sudo apt install git python3-pip -y
pip3 install flask pymongo pandas matplotlib gunicorn
```

### 4. Upload or Clone the Project
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### 5. Run Flask App with Gunicorn
```bash
gunicorn --bind 0.0.0.0:80 app:app
```

Visit: `http://your-ec2-public-ip`

---

## 📝 Sample User Input Format

Form fields:
- Age: number
- Gender: Male/Female/Other
- Total Income: number
- Expense Categories (with checkboxes and amounts):
  - Utilities
  - Entertainment
  - School Fees
  - Shopping
  - Healthcare

---

## 📚 Dependencies

See `requirements.txt`, including:
```
Flask
pymongo
pandas
matplotlib
jupyter
gunicorn
```


