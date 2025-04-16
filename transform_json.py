import json

# Read the JSON file
with open('cooked.json', 'r') as f:
    data = json.load(f)

# Create new sequence section
sequences = {}

# Extract sequences from nodes and store them
for node_id, node_data in data['node'].items():
    if 'sequence' in node_data:
        sequences[node_id] = node_data['sequence']
        del node_data['sequence']  # Remove sequence from node

# Add sequences section after 'edge' if it exists, or after 'node' if not
new_data = {}
for key in data:
    new_data[key] = data[key]
    if key == 'edge':
        new_data['sequence'] = sequences

# If 'edge' wasn't found, add sequences after 'node'
if 'sequence' not in new_data:
    final_data = {}
    for key in new_data:
        final_data[key] = new_data[key]
        if key == 'node':
            final_data['sequence'] = sequences
else:
    final_data = new_data

# Write the modified JSON back to file
with open('cooked.json', 'w') as f:
    json.dump(final_data, f, indent=4)
