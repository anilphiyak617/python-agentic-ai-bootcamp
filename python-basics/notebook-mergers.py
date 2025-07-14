import nbformat

# List your files in order
notebooks = ["1.1-basics.ipynb", "1.3-operators.ipynb", "1.4-conditionals.ipynb", "1.5-loops.ipynb", "1.6-data-structures.ipynb"]
merged_nb = nbformat.v4.new_notebook()
merged_nb.cells = []

for nb_file in notebooks:
    with open(nb_file, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
        merged_nb.cells.extend(nb.cells)

# Save the merged notebook
with open("merged.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(merged_nb, f)
