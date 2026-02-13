import pandas as pd
import numpy as np

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 90},
    {"name": "Eva", "score": 88}
]
# 1.
df = pd.DataFrame(students)

# 2.
scores = np.array(df["score"])

mean_score = np.mean(scores)
median_score = np.median(scores)
std_deviation = np.std(scores)

print("Mean Score:", mean_score)
print("Median Score:", median_score)
print("Standard Deviation:", std_deviation)

# 3.
df["above_average"] = df["score"] > mean_score

# Display final DataFrame
print("\nFinal DataFrame:")
print(df)
