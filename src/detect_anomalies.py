import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# =================================================
# 1. LOAD DATASET
# =================================================

df = pd.read_csv("data/employee_activity.csv")

# =================================================
# 2. SELECT BEHAVIOR FEATURES
# =================================================

features = df[["login_hour", "files_accessed", "sessions_per_day"]]

# =================================================
# 3. TRAIN ISOLATION FOREST MODEL
# =================================================

model = IsolationForest(
    contamination=0.07,
    random_state=42
)

df["anomaly"] = model.fit_predict(features)

df["risk_status"] = df["anomaly"].apply(
    lambda x: "Suspicious" if x == -1 else "Normal"
)

# =================================================
# 4. EXPLAINABILITY (REASON FLAGS)
# =================================================

def generate_reason(row):
    reasons = []

    if row["files_accessed"] > 80:
        reasons.append("High file access")

    if row["login_hour"] < 6 or row["login_hour"] > 22:
        reasons.append("Unusual login time")

    if row["sessions_per_day"] > 7:
        reasons.append("Too many sessions")

    if not reasons:
        return "Normal behavior"

    return ", ".join(reasons)

df["reason"] = df.apply(generate_reason, axis=1)

# =================================================
# 5. RISK SCORE (SCALED & REALISTIC)
# =================================================

def calculate_risk_score(row):
    # Normal users → very low risk
    if row["risk_status"] == "Normal":
        return 5 + row["sessions_per_day"]

    # Suspicious users → scaled risk
    score = 40

    if row["files_accessed"] > 80:
        score += min((row["files_accessed"] - 80) / 4, 25)

    if row["sessions_per_day"] > 7:
        score += min((row["sessions_per_day"] - 7) * 2, 20)

    if row["login_hour"] < 6 or row["login_hour"] > 22:
        score += 15

    return int(min(score, 100))

df["risk_score"] = df.apply(calculate_risk_score, axis=1)

# =================================================
# 6. RISK LEVEL (Low / Medium / High)
# =================================================

def risk_level(score):
    if score < 40:
        return "Low"
    elif score <= 70:
        return "Medium"
    else:
        return "High"

df["risk_level"] = df["risk_score"].apply(risk_level)

# =================================================
# 7. DAILY SUMMARY
# =================================================

print("\n--- DAILY SECURITY SUMMARY ---")
print("Total users:", len(df))
print(df["risk_level"].value_counts())

# =================================================
# 8. CLEAN COLUMN ORDER
# =================================================

final_columns = [
    "user_id",
    "risk_status",
    "risk_level",
    "risk_score",
    "reason",
    "login_hour",
    "files_accessed",
    "sessions_per_day"
]

df = df[final_columns]

# =================================================
# 9. SAVE OUTPUT FILES
# =================================================

df[df["risk_status"] == "Normal"].to_csv(
    "results/normal_users.csv", index=False
)

df[df["risk_status"] == "Suspicious"].to_csv(
    "results/suspicious_users.csv", index=False
)

df[df["risk_level"] == "High"].to_csv(
    "results/high_risk_users.csv", index=False
)

print("\n--- FILES GENERATED ---")
print("✔ normal_users.csv")
print("✔ suspicious_users.csv")
print("✔ high_risk_users.csv")

# =================================================
# 10. BAR CHART (COUNTS)
# =================================================

df["risk_status"].value_counts().plot(kind="bar")
plt.title("User Risk Distribution")
plt.xlabel("Risk Status")
plt.ylabel("Number of Users")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
