import pandas as pd

df = pd.read_csv("train.csv")

print(df.head(5))
print(df.size)

print(df["Embarked"].nunique())
print(df["Embarked"].unique())
print(df["Embarked"].nunique())
print(df["Embarked"].value_counts())

print(df["Fare"].mean())
print(df["Fare"].median())
print(df["Fare"].mode()[0])

#mode also works on categorical data
print(df["Embarked"].mode()[0])
print(df["Sex"].mode()[0])

print(df["Fare"].min())
print(df["Fare"].max())

print(df["Fare"].var())
print(df["Fare"].std())