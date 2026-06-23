import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/cleaned_dataset.csv")

print(df.describe())

plt.hist(df["Age"])
plt.title("Age Distribution")
plt.savefig("images/age_distribution.png")
plt.close()

sns.countplot(x="Survived", data=df)
plt.title("Survival Count")
plt.savefig("images/survival_count.png")
plt.close()

numeric_df = df.select_dtypes(include=["number"])

plt.figure(figsize=(8,6))
sns.heatmap(numeric_df.corr(), annot=True)
plt.title("Correlation Matrix")
plt.savefig("images/correlation_matrix.png")
plt.close()

print("EDA completed.")
