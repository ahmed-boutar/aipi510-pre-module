# AIPI 510: Data Sourcing & Analytics (Fall 2024)

This directory was cloned from the accompanying GitHub to the Fall 2024 section of AIPI 510, taught by Dr. Brinnae Bent.
References: 
1 - Dataset Source: https://www.kaggle.com/datasets/iamsumat/spotify-top-2000s-mega-dataset


## Directory Description
This directory contains python scripts used for the processing of a csv file (Spotify - All Time Top 2000s Mega Dataset), unit testing of the processing functionalities, and the packaging of the script into a command line tool. 
The main.py script displays information about the dataset such as the number of null value per column, the avg, mean, and median bpm per genre.

List of Python scripts included: 
src:
   __init__.py
   main.py
tests
   test_main.py
setup.py

## How to run
NOTE: Python3.11 is needed to install the dependencies specified in the requirements.txt file, cloned from the AIPI510 classroom repo. Using Python3.12 will cause one of these errors (no module "disutils" found OR module pgkutil has no attribute ImpImporter.
1) Navigate to the directory where the setup.py is
2) Run: python3 -m venv venv OR python -m venv venv
3) Run: source venv/bin/activate
5) Run: pip install -e .  (NOTE: The . is part of the command)
6) Run: premodule
7) To run the testing module use: python -m unittest tests.test_main OR python -m unittest discover -s tests


