import pandas as pd
import matplotlib.pyplot as plt
import json

# Load dataset
df = pd.read_csv("All_Diets.csv")

# Clean data
df = df.dropna()

# Convert to numeric
df["Protein(g)"] = pd.to_numeric(df["Protein(g)"], errors='coerce')
df["Carbs(g)"] = pd.to_numeric(df["Carbs(g)"], errors='coerce')
df["Fat(g)"] = pd.to_numeric(df["Fat(g)"], errors='coerce')

# --- CALCULATIONS ---
avg_protein = df["Protein(g)"].mean()
avg_carbs = df["Carbs(g)"].mean()
avg_fat = df["Fat(g)"].mean()

print("Average Protein:", avg_protein)
print("Average Carbs:", avg_carbs)
print("Average Fat:", avg_fat)

# --- BAR CHART ---
df.groupby("Diet_type")["Protein(g)"].mean().plot(kind='bar', title="Protein by Diet")
plt.savefig("bar_chart.png")
plt.show()
plt.clf()

# --- PIE CHART ---
df["Diet_type"].value_counts().plot(kind='pie', autopct='%1.1f%%', title="Diet Distribution")
plt.savefig("pie_chart.png")
plt.show()
plt.clf()

# --- LINE CHART ---
df[["Protein(g)", "Carbs(g)", "Fat(g)"]].head(10).plot(kind='line', title="Nutrition Trends")
plt.savefig("line_chart.png")
plt.show()
plt.clf()

# --- SAVE RESULTS JSON ---
result = {
    "avg_protein": avg_protein,
    "avg_carbs": avg_carbs,
    "avg_fat": avg_fat
}

with open("results.json", "w") as f:
    json.dump(result, f)

print("Charts + results.json created successfully")