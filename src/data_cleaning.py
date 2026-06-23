import pandas as pd

df = pd.read_csv("data/raw_dataset.csv")

print(df.head())

if "Age" in df.columns:
    df["Age"] = df["Age"].fillna(df["Age"].median())

if "Embarked" in df.columns:
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

if "Cabin" in df.columns:
    df = df.drop("Cabin", axis=1)

df = df.drop_duplicates()

df.to_csv("data/cleaned_dataset.csv", index=False)

print("Data cleaning completed.")
