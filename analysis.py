# ============================
# E-commerce Sales Analysis (Fixed)
# ============================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Style
sns.set(style="whitegrid")

# Load dataset
df = pd.read_csv("SampleSuperstore.csv", encoding='latin1')

# ----------------------------
# 1. Basic Overview
# ----------------------------
print("Dataset Shape:", df.shape)
print("\nTotal Sales:", round(df['Sales'].sum(), 2))
print("Total Profit:", round(df['Profit'].sum(), 2))

# ----------------------------
# 2. Sales by Region
# ----------------------------
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(8,5))
sns.barplot(data=region_sales, x='Region', y='Sales', hue='Region', palette='Blues_d', legend=False)
plt.title("Sales by Region")
plt.show()

# ----------------------------
# 3. Profit by Category
# ----------------------------
category_profit = df.groupby('Category')['Profit'].sum().sort_values().reset_index()

plt.figure(figsize=(8,5))
sns.barplot(data=category_profit, x='Category', y='Profit', hue='Category', palette='Set2', legend=False)
plt.title("Profit by Category")
plt.show()

# ----------------------------
# 4. Top Sub-Categories (Replacing Product Name)
# ----------------------------
# Since 'Product Name' is missing, we use 'Sub-Category'
top_subs = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(10,6))
sns.barplot(data=top_subs, x='Sales', y='Sub-Category', hue='Sub-Category', palette='viridis', legend=False)
plt.title("Top 10 Sub-Categories by Sales")
plt.show()

# ----------------------------
# 5. Segment Analysis
# ----------------------------
segment_profit = df.groupby('Segment')['Profit'].sum()

plt.figure(figsize=(8,5))
plt.pie(segment_profit.values, labels=segment_profit.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title("Profit Share by Customer Segment")
plt.show()

# ----------------------------
# 6. Business Insights
# ----------------------------
print("\n===== BUSINESS INSIGHTS =====")
print(f"1. Highest sales region: {region_sales.iloc[0]['Region']}")
print(f"2. Most profitable category: {category_profit.iloc[-1]['Category']}")
print(f"3. Best customer segment: {segment_profit.idxmax()}")