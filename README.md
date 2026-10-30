# 🎓 Student Pass/Fail Prediction System

<p align="center">
  <b>Machine Learning Project using Python</b>
</p>

<p align="center">
  Predict student academic performance based on study hours and attendance percentage.
</p>

---

## 📌 About The Project

The **Student Pass/Fail Prediction System** is a Machine Learning project developed using Python.

This project predicts whether a student is likely to **Pass or Fail** based on two important factors:

- 📚 Study Hours
- 📊 Attendance Percentage

A trained Machine Learning model analyzes the student's input data and generates a prediction.

## ✨ Features

- 🎯 Predicts student Pass or Fail.
- 📚 Uses study hours as an input feature.
- 📊 Uses attendance percentage as an input feature.
- 🤖 Machine Learning model training.
- 💾 Saves the trained model using Pickle.
- 🔍 Predicts results for new student data.
- 🌐 Simple application interface.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Programming Language |
| 🤖 Scikit-learn | Machine Learning |
| 🐼 Pandas | Data Processing |
| 🔢 NumPy | Numerical Operations |
| 📦 Pickle | Model Serialization |
| 🌐 Flask | Web Application |

## 📂 Project Structure

```text
python-model-training/
│
├── static/              # CSS, JavaScript and images
│
├── app.py               # Main application
├── train_model.py       # Model training script
├── model.pkl            # Trained ML model
├── students.csv         # Student dataset
│
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── .gitignore           # Ignored files
```

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/arhamahmadcenter-creator/python-model-training.git
```

**2. Open the project folder**

```bash
cd python-model-training
```

**3. Create a virtual environment**

```bash
python -m venv .venv
```

**4. Activate the virtual environment**

Windows:

```bash
.venv\Scripts\activate
```

**5. Install dependencies**

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

**Step 1: Train the Machine Learning model**

```bash
python train_model.py
```

**Step 2: Run the application**

```bash
python app.py
```

Open the local URL displayed in your terminal to access the application.

## 📊 Input Features

| Feature | Description |
|---|---|
| Study Hours | Number of hours spent studying |
| Attendance | Student attendance percentage |

## 🎯 Prediction Results

The model generates one of two possible outcomes:

- 🟢 **Pass**
- 🔴 **Fail**

## 🧠 Machine Learning Workflow

1. 📥 Load student dataset.
2. 🧹 Prepare and process data.
3. 📊 Select input features.
4. ✂️ Split data into training and testing sets.
5. 🤖 Train the Machine Learning model.
6. 📈 Evaluate model performance.
7. 💾 Save the trained model.
8. 🎯 Generate predictions for new students.

## 🚀 Future Improvements

- 📈 Improve prediction accuracy.
- 📊 Add performance visualization.
- 👨‍🎓 Include more student performance features.
- 🎨 Improve application interface.
- 📱 Make the application responsive.

## 👨‍💻 Author

**Muhammad Arham**

- GitHub: [@arhamahmadcenter-creator](https://github.com/arhamahmadcenter-creator)

---

<p align="center">
  ⭐ If you find this project useful, don't forget to give it a star!
</p>
