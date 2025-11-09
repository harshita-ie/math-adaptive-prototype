# 🧠 Math Adventures — Adaptive Learning Prototype

### *An AI-powered math learning environment that adjusts question difficulty in real time.*

---

## 📘 Project Description

**Math Adventures** is an adaptive learning prototype designed to make math practice more personalized and engaging.  
It intelligently adjusts question difficulty based on a learner’s recent performance — becoming more challenging when the learner performs well and easing off when they struggle.

This version is a **console-based prototype**, meant to demonstrate how adaptive algorithms can be applied in educational software.  
The adaptive system is *rule-based* but is structured to allow easy extension into *machine-learning-based* personalization later.

---

## 🎯 Key Features

- **Adaptive Difficulty:** Automatically adjusts between *Easy*, *Medium*, and *Hard* levels using accuracy and response time.
- **Wide Range of Math Topics:** Covers arithmetic, algebra, and calculus (integration, differentiation, equations).
- **Real-Time Feedback:** Tracks and evaluates every response with timing.
- **Data Tracking:** Logs accuracy, average response time, and difficulty transitions.
- **ML-Ready Structure:** Includes placeholders for ML-based adaptation using scikit-learn.

---

## 🏗️ Project Structure

```
math-adaptive-prototype/
├── README.md
├── requirements.txt
├── TECHNICAL_NOTE.md
└── src/
    ├── main.py
    ├── puzzle_generator.py
    ├── tracker.py
    └── adaptive_engine.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Requirements
- Python 3.8 or higher  
- pip (Python package installer)

### 2️⃣ Install dependencies

Run:
```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install sympy numpy pandas scikit-learn
```

### 3️⃣ Run the prototype

```bash
python src/main.py
```

---

## 🧩 How It Works

| Component | Role |
|------------|------|
| **PuzzleGenerator** | Generates math problems (arithmetic, algebra, calculus) based on difficulty. |
| **Tracker** | Logs each question’s correctness, time, and difficulty. |
| **AdaptiveEngine** | Determines when to increase/decrease difficulty using performance metrics. |
| **Main** | Runs the learning loop and manages user interaction. |

---

## 🧠 Adaptive Logic

The **rule-based engine** monitors the learner’s *recent accuracy* and *average response time* (over the last few problems):

| Condition | Action |
|------------|---------|
| Accuracy ≥ 80% and avg time ≤ threshold | 🔺 Increase difficulty |
| Accuracy ≤ 50% or avg time ≥ 1.5× threshold | 🔻 Decrease difficulty |
| Otherwise | ➡️ Keep same difficulty |

**Time thresholds**
- Easy: 8 seconds  
- Medium: 12 seconds  
- Hard: 20 seconds

---

## 🧾 Example Questions

| Level | Sample Problem | Expected Answer |
|--------|----------------|-----------------|
| Easy | `7 + 4` | `11` |
| Medium | `Solve equation: 2*x + 3 = 9` | `[3.0]` |
| Hard | `Integrate ∫ sin(x)*x dx` | `-x*cos(x) + sin(x)` |
| Hard | `Find derivative of x³ at x=2` | `12` |

---

## 🧮 Sample Session

```
Enter learner name: Alex
Choose initial difficulty (Easy/Medium/Hard) [Easy]: easy

Hello Alex! Starting session at Easy level. Type "quit" to stop.

Level: Easy | Question: 8 + 3 = ?
> 11
>> Correct!

Level: Easy | Question: 2 ** 3 = ?
> 8
>> Difficulty changed: Easy → Medium
```

---

## 🚀 Future Extensions

- **Machine Learning Adaptation:** Train models on learner data to predict optimal next difficulty.  
- **Web or GUI Interface:** Port to Streamlit or Flask for better usability.  
- **Analytics Dashboard:** Visualize learner progress and skill mastery.  
- **Topic-Based Adaptation:** Adjust difficulty per math topic (e.g., algebra vs. calculus).  

---

## 🧑‍💻 Technologies Used

| Tool | Purpose |
|------|----------|
| **Python 3.8+** | Core programming language |
| **SymPy** | Symbolic math (integration, differentiation, equation solving) |
| **scikit-learn** | Optional ML-based adaptation engine |
| **pandas / numpy** | Data handling and analytics |

---

## 📜 License

Free for academic and non-commercial use.  
Attribution required if redistributed or modified.

---

## ✨ Author

**Developed by:** HARSHITA SARDA  
**Purpose:** Educational Prototype for Adaptive Learning Research   
**Version:** 1.2  
**Date:** 09 November 2025
