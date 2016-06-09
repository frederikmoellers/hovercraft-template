#!/usr/bin/env python3

from bs4 import BeautifulSoup
import sys

with open(sys.argv[1], "r") as f:
    tree = BeautifulSoup(f, 'html.parser')

for note in tree.find_all("div", class_ = "notes"):
    note.decompose()

print(tree)
