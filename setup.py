import setuptools

with open ("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Skyscraper",
    version="0.1",
    author="Glibesyck Solodzhuk",
    author_email="hlib.solodzhuk@ucu.edu.ua",
    description="For working with skyscraper.py",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/glibesyck/Skyscraper.git",
    packages=setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8'
)