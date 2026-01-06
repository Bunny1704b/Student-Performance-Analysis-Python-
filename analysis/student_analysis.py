import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/student_marks.csv")
df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

print(df)

plt.bar(df["Name"], df["Average"])
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.title("Student Performance Analysis")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
