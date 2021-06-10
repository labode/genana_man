# Manual generation reader
Tool to combine https://github.com/phcerdan/sggen generation output with https://github.com/labode/genana_py id assignment for statistical analysis

## How does it work?
Reads generation/vertex matching from .txt, matches those to vertex coordinates from .dot graph, does a lookup for the associated id labels at these coordinates from the id.nrrd file generated by genana_py.

## Inputs:
- .txt generated by sggen containing generation/vertex table
- .dot generated by sggen graph containing coordinates of nodes and edges
- .nrrd generated by genana_py containing graph w. label ids

## Output:
- .csv containing id/gen matching

## Usage
python main.py gens.csv graph.dot ids.nrrd outputfile