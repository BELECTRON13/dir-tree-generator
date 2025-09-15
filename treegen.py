import argparse
from pathlib import Path

def generate_tree(directory, prefix='', output_file=None, ignore_list=None, max_depth=None, current_depth=None):
    if ignore_list is None:
        ignore_list = []

    directory = Path(directory) if isinstance(directory, str) else directory
    
    if not directory.exists() or not directory.is_dir():
        print('Error: The specified path is not valid directory.')
        return
    
    if max_depth  is not None and current_depth > max_depth:
        return
    
    try:

        items = sorted(list(directory.iterdir()), key=lambda x: (x.is_file(), x.name.lower()))

    except PermissionError:
        return
    
    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        connector = '└── ' if is_last else '├── '
        print(prefix + connector + item.name)

        line = prefix + connector + item.name

        if item.is_dir():
            extention = '    ' if is_last else '│   '
            generate_tree(item,
                          prefix + extention,
                          output_file,
                          ignore_list,
                          current_depth + 1
            )