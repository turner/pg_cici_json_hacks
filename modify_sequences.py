import json

# Read the JSON file
with open('hacks.json', 'r') as f:
    data = json.load(f)

# For each node in the data
for node_id in data['node']:
    # Get the current sequence
    sequence = data['node'][node_id]['sequence']
    # Keep only the first 4 nucleotides
    data['node'][node_id]['sequence'] = sequence[:4]

# Write the modified data back to the file
with open('hacks.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Successfully modified sequences in hacks.json")
