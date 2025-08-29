#!/usr/bin/python

import os

root_dir = "exercises"

for dirpath, _, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".rs"):
            name = os.path.splitext(filename)[0]
            path = os.path.join(dirpath, filename).replace("\\", "/")
            print(f'[[bin]]\nname = "{name}"\npath = "{path}"\n')
