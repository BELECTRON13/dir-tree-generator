import argparse
from pathlib import Path

def generate_tree(directory, prefix=''):
    directory = Path(directory)
    
    if not directory.exists() or not directory.is_dir():
        print('Error: The specified path is not valid directory.')
        return
    
    items = sorted(list(directory.iterdir()), key=lambda x: (x.is_file(), x.name))

    for index, item in enumerate(items):
        connector = '├──' if index < len(items) - 1 else '└──'
        print(prefix + connector + item.name)

        if item.is_dir():
            extention = '│   ' if index < len(items) - 1 else '    '
            generate_tree(item, prefix + extention)