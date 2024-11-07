from skbuild import setup
from setuptools import find_packages
import os, sys


cmake_args = []
python_executable = sys.executable
cmake_args.append(f"-DPYTHON_EXECUTABLE:FILEPATH={python_executable}")

# Read the long description from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Define the setup configuration
setup(
    name="quMeas",
    version="1.0",
    author="Oinam Romesh Meitei",
    author_email="oinam.meitei@fau.de",
    description="A high-performance multi-threaded library for Pauli measurements on quantum computers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oimeitei/qumeas",
    packages=find_packages(where='python'),
    package_dir={'': 'python'},
    cmake_install_dir='qumeas',
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C++",
        "Operating System :: OS Independent",
        "License :: Aphache 2.0",  
        "Topic :: Quantum Computing :: Scientific/Engineering :: Physics",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy",
        "scipy"
    ],
    # cmake_args=cmake_args,
)
