import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("All_Diets.csv")

# Handle missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Average macronutrients per diet
avg_macros = df.groupby('Diet_type')[['Protein(g)', 'Carbs(g)', 'Fat(g)']].mean()
print("Average Macronutrients:\n", avg_macros)

# Top 5 protein-rich recipes per diet
top_protein = df.sort_values('Protein(g)', ascending=False).groupby('Diet_type').head(5)
print("\nTop Protein Recipes:\n", top_protein[['Diet_type','Recipe_name','Protein(g)']])

# Highest protein diet
highest_protein = avg_macros['Protein(g)'].idxmax()
print("\nHighest Protein Diet:", highest_protein)

# Most common cuisine per diet
common_cuisine = df.groupby('Diet_type')['Cuisine_type'].agg(lambda x: x.value_counts().index[0])
print("\nMost Common Cuisine:\n", common_cuisine)

# New ratios
df['Protein_to_Carbs'] = df['Protein(g)'] / df['Carbs(g)']
df['Carbs_to_Fat'] = df['Carbs(g)'] / df['Fat(g)']

# -------- VISUALIZATION --------

# Bar Chart
avg_macros.plot(kind='bar')
plt.title("Average Macronutrients per Diet")
plt.ylabel("Grams")
plt.xticks(rotation=45)
plt.savefig("bar_chart.png")
plt.close()

# Heatmap
sns.heatmap(avg_macros, annot=True)
plt.title("Macronutrient Heatmap")
plt.savefig("heatmap.png")
plt.close()

# Scatter Plot
sns.scatterplot(data=top_protein, x='Protein(g)', y='Carbs(g)', hue='Diet_type')
plt.title("Top Protein Recipes")
plt.savefig("scatter.png")
plt.close()

print("\nGraphs saved successfully as images!")
