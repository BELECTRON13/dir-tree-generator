from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dir-tree-generator",
    version="1.0.0",
    author="Mohammadali",
    author_email="mohammadhoseinpoor167@gmail.com",
    description="A Python script to generate directory tree structures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/belectron13/dir-tree-generator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: Software Development :: Documentation",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "treegen=treegen:main",
        ],
    },
)