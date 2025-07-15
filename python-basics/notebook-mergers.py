import nbformat

# List your files in order
notebooks = ["1.5-loops.ipynb", "1.6-data-structures.ipynb", "1.7-sets.ipynb", "1.8-dictionaries.ipynb", "1.9-tuples.ipynb", "2.0-function.ipynb", "3.1-maps.ipynb"]
merged_nb = nbformat.v4.new_notebook()
merged_nb.cells = []

for nb_file in notebooks:
    with open(nb_file, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
        merged_nb.cells.extend(nb.cells)

# Save the merged notebook
with open("merged.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(merged_nb, f)
