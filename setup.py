"""
This script is used to package the csv processing into a command line tool
"""

from setuptools import setup, find_packages

# Function to read the requirements.txt file
def get_repo_requirements(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()
    
setup(
    name="premodule",
    version="0.1.0",
    packages=find_packages(),
    install_requires=get_repo_requirements('requirements.txt'),
    py_modules=["main"],
    entry_points={
        "console_scripts": [
            "premodule=src.main:main",
        ],
    },
    author="Ahmed Boutar",
    description="A command-line tool for processing Spotify Top 2000 tracks and calculating stats related to bpm and genres",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
)