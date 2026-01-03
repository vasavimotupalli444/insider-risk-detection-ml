

# 🔐 Insider Risk Detection using Machine Learning

## 📌 Overview

Insider threats are one of the most critical security risks for organizations, especially in banks and large enterprises.
This project implements an **unsupervised machine learning system** to detect **abnormal employee system usage patterns** and assess **insider risk** in a scalable and explainable way.

The system analyzes employee activity logs and flags unusual behavior such as:

* Unusual login hours
* Excessive file access
* Abnormally high login sessions

It produces **actionable, prioritized outputs** that security teams can review directly.

---

## 🎯 Problem Statement

Organizations need an automated way to identify potentially risky internal behavior without relying on labeled fraud data.

Challenges:

* Insider misuse data is rare and unlabeled
* False alarms must be minimized
* Alerts should be explainable and prioritized

---

## 💡 Solution Approach

This project uses **unsupervised anomaly detection** with Isolation Forest to learn normal behavior patterns and detect deviations.

### Key design decisions:

* **Unsupervised ML** → no labeled data required
* **Explainability** → clear reasons for alerts
* **Risk scoring** → prioritization instead of binary flags
* **Clean outputs** → analyst-friendly CSV files

---

## 🧠 Machine Learning Model

* **Algorithm:** Isolation Forest
* **Type:** Unsupervised Learning
* **Why Isolation Forest?**

  * Effective for rare anomalies
  * Scales well for enterprise data
  * Commonly used in security analytics

---

## 📊 Dataset Description

Synthetic employee activity data is used to avoid privacy concerns.

| Feature            | Description                      |
| ------------------ | -------------------------------- |
| `user_id`          | Unique employee ID               |
| `login_hour`       | Hour of system login (0–23)      |
| `files_accessed`   | Number of files accessed per day |
| `sessions_per_day` | Number of login sessions         |

---

## ⚙️ Features Implemented

* Anomaly detection using ML
* Risk score (0–100) for prioritization
* Risk levels: **Low / Medium / High**
* Explainability using rule-based reasons
* Daily security summary
* Bar chart visualization (risk distribution)
* Separate output files for clean review

---

## 📂 Project Structure

```
insider-risk-detection-ml/
│
├── data/
│   └── employee_activity.csv
│
├── src/
│   └── detect_anomalies.py
│
├── results/
│   ├── normal_users.csv
│   ├── suspicious_users.csv
│   └── high_risk_users.csv
│
└── README.md
```

---

## 📈 Output Files

The system generates three actionable CSV files:

| File                   | Purpose                    |
| ---------------------- | -------------------------- |
| `normal_users.csv`     | Low-risk users             |
| `suspicious_users.csv` | Users requiring monitoring |
| `high_risk_users.csv`  | High-priority insider risk |

Each record includes:

* Risk status
* Risk level
* Risk score
* Explanation of behavior

---

## 📊 Visualization

A bar chart shows the distribution of **Normal vs Suspicious users**, providing a quick overview of system health for security teams.

---

## 🧪 How to Run the Project

### 1️⃣ Install dependencies

```bash
pip install pandas scikit-learn matplotlib
```

### 2️⃣ Run the detection script

```bash
python src/detect_anomalies.py
```

### 3️⃣ View results

* Check the `results/` folder for CSV outputs
* Bar chart will be displayed automatically

---

## 🧾 Tech Stack

* Python
* Pandas
* Scikit-learn
* Matplotlib

