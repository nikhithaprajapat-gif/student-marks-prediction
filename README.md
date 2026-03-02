# 🎓 Student Exam Score Predictor

A Streamlit web application that predicts student exam scores using a Linear Regression model trained on 5000 student records.

---

## 📁 Project Structure

```
project/
│
├── app.py                                        # Streamlit application
├── model.pkl                                     # Trained model (joblib)
├── ultimate_student_productivity_dataset_5000.csv  # Dataset
└── README.md                                     # Project documentation
```

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install streamlit scikit-learn pandas numpy joblib
```

### 2. Train & Export the Model (in your notebook)

```python
import joblib
joblib.dump(model, 'model.pkl')
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## 🧠 Model Details

| Property | Value |
|---|---|
| Algorithm | Linear Regression |
| Training Samples | 4000 |
| Test Samples | 1000 |
| Train/Test Split | 80/20 |
| Mean Absolute Error | ~4.19 |

---

## 📊 Input Features

| Feature | Description |
|---|---|
| Academic Level | High School / Undergraduate / Postgraduate |
| Study Hours | Daily hours spent in class/studying |
| Self Study Hours | Daily self-directed study hours |
| Online Classes Hours | Daily hours of online learning |
| Social Media Hours | Daily social media usage |
| Gaming Hours | Daily gaming hours |
| Sleep Hours | Daily sleep duration |
| Screen Time Hours | Total daily screen time |
| Mental Health Score | Score from 1 (poor) to 10 (excellent) |
| Productivity Score | Score from 0 to 100 |

**Target Variable:** `exam_score` (0–100)

---

## 🔑 Key Correlations with Exam Score

| Feature | Correlation |
|---|---|
| Productivity Score | +0.886 |
| Mental Health Score | +0.547 |
| Study Hours | +0.513 |
| Sleep Hours | +0.235 |
| Screen Time Hours | -0.132 |
| Social Media Hours | -0.106 |

---

## 🖥️ App Features

- Interactive sliders for all 10 input features
- Real-time exam score prediction
- Performance feedback (Excellent / Average / Below Average)
- Clean two-column layout

---

## 📦 Dependencies

- `streamlit` — Web UI framework
- `scikit-learn` — Machine learning
- `pandas` — Data manipulation
- `numpy` — Numerical computation
- `joblib` — Model serialization
