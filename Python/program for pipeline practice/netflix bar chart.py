import pandas as pd
import matplotlib.pyplot as plt  # Correct import

data = pd.read_csv("netflix_titles.csv")

# Count the number of entries for each type (e.g., Movie, TV Show)
type_counts = data['type'].value_counts()

# Plot
plt.bar(type_counts.index, type_counts.values, width=0.5, color="orange")

plt.xlabel('Type')
plt.ylabel('Amount')
plt.title('Number of Titles by Type')

plt.show()
