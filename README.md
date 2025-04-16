# Dat Hacks - Pan Genome Sequence Analysis Project

This project analyzes genomic sequence data and their associated ODGF coordinates.

## Data Files
- `chr1_25240000_25460000_data.json`: Genomic sequence data for chromosome 1 region 25240000-25460000
- `hacks.json`: Contains sequence length and ODGF coordinate data
- Various visualization outputs (*.png files)

## Scripts
- `analyze_coordinates.py`: Analyzes correlation between sequence length and ODGF coordinates
- `modify_sequences.py`: Script for sequence modifications

## Key Findings
- Strong correlation (0.985) between sequence length and number of ODGF coordinates
- Coordinate patterns:
  - Sequences <1000bp: 2 coordinates
  - 15-35kb sequences: 2-3 coordinates
  - >70kb sequences: 5+ coordinates
