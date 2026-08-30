import pandas as pd
import sys
from markdown_table_extractor import extract_tables
from dataclasses import dataclass

"""
I made this program to generate the challenge index for The Joseph Challenge,
using the README.md file of joseph's my-ctf-challenges repo as the data source
"""

if len(sys.argv) != 2:
    print("usage: python3 ./generate-challenge-index.py path/to/README.md")
    exit(1)

content = None
with open(sys.argv[1], "r") as f:
    content = f.read()

@dataclass
class Challenge:
    link: str
    difficulty: str
    category: str

chals = []

tables = extract_tables(content)
table = pd.concat(tables, ignore_index=True)
table["Solved?"] = "No"
table["Writeup"] = pd.Series(["Not written"] * len(table))
del table["Solves"]

items = []
difficulties = ["👶", "⭐️", "⭐️⭐️", "⭐️⭐️⭐️", "⭐️⭐️⭐️⭐️"]
for difficulty in difficulties:
    group = table[table.Difficulty == difficulty]
    del group["Difficulty"]
    items.append(f"## Difficulty: {difficulty}")
    items.append(group.to_markdown(index=False))

out = "\n\n".join(items)
with open("out.md", "w") as f:
    content = f.write(out)
