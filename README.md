# Dir-Tree-Generator 🌳

A simple yet powerful Python tool to generate beautiful directory tree structures for documentation and project analysis.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-1.0.0-orange)

---

## ✨ Features

· Generate clean, visual directory structures
· Support for multiple output formats (text, markdown)
· Ignore specific files/folders (like .git, __pycache__)
· Limit traversal depth with max-depth option
· Console output and file export capabilities
· Easy to use command-line interface

---

## 📦 Installation

Option 1: Install as package

```bash
git clone https://github.com/your-username/dir-tree-generator.git
cd dir-tree-generator
pip install -e .
```

Option 2: Use directly

```bash
git clone https://github.com/your-username/dir-tree-generator.git
cd dir-tree-generator
```

---

## 🚀 Quick Start

Basic usage (current directory):

```bash
treegen
```

or

```bash
python treegen.py
```

Generate tree for specific path:

```bash
treegen -p path/to/your/project
```

Save output to file:

```bash
treegen -o structure.md
```

Generate markdown format:

```bash
treegen -f markdown -o STRUCTURE.md
```

Ignore specific files/folders:

```bash
treegen --ignore .git,__pycache__,venv
```

Limit traversal depth:

```bash
treegen --max-depth 2
```

---

## 📋 Usage Examples

```bash
# Generate tree for current directory and display in console
treegen

# Generate tree for a project and save as markdown
treegen -p ~/projects/my-app -o PROJECT_TREE.md

# Generate tree ignoring common directories
treegen --ignore .git,__pycache__,node_modules,venv

# Generate shallow structure (2 levels deep)
treegen --max-depth 2 -o shallow_tree.txt
```

---

## 🎯 Advanced Usage

### Combine multiple options:

```bash
treegen -p src --ignore test,__pycache__ --max-depth 3 -o src_structure.md
```

### Use as Python module:

```python
from treegen import generate_tree

# Generate tree structure
generate_tree("path/to/directory")

# Generate with advanced options
generate_tree(
    "path/to/directory",
    output_file="structure.md",
    ignore_list=[".git", "__pycache__"],
    max_depth=3
)
```

---

## 📊 Output Examples

```
my-project/
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── tests/
│   └── test_main.py
├── data/
│   └── input.csv
├── README.md
└── requirements.txt
```

---

## ⚙️ Configuration Options

| Parameter       | Format               | Default       | Description              |
| --------------- | -------------------- | ------------- | ------------------------ |
| `-p, --path`    | Path                 | `.` (current) | Target directory path    |
| `-o, --output`  | Filename             | None          | Output file name         |
| `--ignore`      | Comma-separated list | Empty         | Files/folders to ignore  |
| `--max-depth`   | Integer              | Unlimited     | Maximum traversal depth  |
| `-v, --version` | -                    | -             | Show version information |
| `-h, --help`    | -                    | -             | Show help message        |

---

## 🤝 Contributing

We welcome contributions! Please feel free to submit issues, feature requests, or pull requests.

---

## 🛠️ Development

### Setup development environment:

```bash
git clone https://github.com/your-username/dir-tree-generator.git
cd dir-tree-generator
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
pip install -e .
```

---

## 📞 Support

If you have any questions or need help, please:

- https://t.me/Belectron13
