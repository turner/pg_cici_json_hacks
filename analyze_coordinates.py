import json
import matplotlib.pyplot as plt

# Read the JSON file
with open('hacks.json', 'r') as f:
    data = json.load(f)

# Extract lengths and coordinate counts
lengths = []
coord_counts = []

for node_id, node_data in data['node'].items():
    lengths.append(node_data['length'])
    coord_counts.append(len(node_data['odgf_coordinates']))

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(lengths, coord_counts, alpha=0.5)
plt.xlabel('Sequence Length')
plt.ylabel('Number of Coordinates')
plt.title('Sequence Length vs Number of Coordinates')

# Calculate correlation coefficient
from scipy import stats
correlation, p_value = stats.pearsonr(lengths, coord_counts)
print(f"Correlation coefficient: {correlation:.3f}")
print(f"P-value: {p_value:.3f}")

# Add correlation info to plot
plt.text(0.05, 0.95, f'Correlation: {correlation:.3f}', 
         transform=plt.gca().transAxes)

plt.savefig('length_vs_coordinates.png')

# Print detailed statistics
print("\nDetailed Statistics:")
for node_id, node_data in data['node'].items():
    print(f"\nNode: {node_id}")
    print(f"Length: {node_data['length']}")
    print(f"Number of coordinates: {len(node_data['odgf_coordinates'])}")
