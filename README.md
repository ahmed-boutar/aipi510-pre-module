# AIPI 510: Data Sourcing & Analytics (Fall 2024)

This directory was cloned from the accompanying GitHub to the Fall 2024 section of AIPI 510, taught by Dr. Brinnae Bent. 
References: 
1 - Dataset Source: https://www.kaggle.com/datasets/iamsumat/spotify-top-2000s-mega-dataset


## Directory Description
This directory contains python scripts used for the processing of a csv file (Spotify - All Time Top 2000s Mega Dataset), unit testing of the processing functionalities, and the packaging of the script into a command line tool. 
The main.py script return displays information about the dataset such as the number of null value per column, the avg, mean, and median bpm per genre.

List of Python scripts included: 
src:
   __init__.py
   main.py
tests
   test_main.py

## How to run
1) python3 -m venv venv
2) source venv/bin/activate
3) pip install -r requirements.txt
From the main directory, please run the following commands
4) python3 src/main.py 
5) python -m unittest tests.test_main


