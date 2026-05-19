import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_csv.csv", encoding="latin1")

df = df.drop_duplicates()
df = df.fillna(0)

print("Columns in Dataset:")
print(df.columns)

text_columns = df.select_dtypes(include='object').columns
numeric_columns = df.select_dtypes(include='number').columns

category_col = text_columns[0]
value_col = numeric_columns[0]

print("\nUsing:")
print("Category Column:", category_col)
print("Value Column:", value_col)

analysis = (
    df.groupby(category_col)[value_col]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))

bars = plt.bar(
    analysis.index.astype(str),
    analysis.values
)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f'{height:.0f}',
        ha='center',
        va='bottom'
    )

plt.title(f"Top 10 {category_col} by {value_col}", fontsize=16)
plt.xlabel(category_col, fontsize=12)
plt.ylabel(value_col, fontsize=12)

plt.xticks(rotation=30)

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()

plt.show()