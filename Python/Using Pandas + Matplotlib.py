import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (example: Titanic dataset from seaborn)
df = sns.load_dataset("titanic")

# Basic analysis: average age of passengers
avg_age = df['age'].mean()
print("Average Age of Passengers:", avg_age)

# Bar chart: survival count
df['survived'].value_counts().plot(kind='bar', title="Survival Count")
plt.show()

# Scatter plot: age vs fare
plt.scatter(df['age'], df['fare'])
plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Age vs Fare")
plt.show()

# Heatmap: correlation
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.show()
