'''
This script is used to test the functions from main.py
'''

import unittest
import pandas as pd
from src.main import load_dataset, get_df_shape, get_columns, get_null_by_column, calculate_bpm_stats_per_genre


class TestProcessingCSV(unittest.TestCase):

    def setUp(self):
        self.test_data = pd.read_csv("data/Spotify-2000.csv")
    
    def test_load_dataset(self):
        df = load_dataset("data/Spotify-2000.csv")
        self.assertEqual(len(df), 1994)
        column_names = get_columns(self.test_data)
        for col in column_names:
            self.assertIn(col, df.columns)
    
    def test_get_df_shape(self):
        dataset_shape = get_df_shape(self.test_data)
        self.assertEqual(dataset_shape, self.test_data.shape)
    
    def test_get_null_by_column(self):
        df_not_null = get_null_by_column(self.test_data)
        self.assertTrue((df_not_null[1] == 0).all())
    
    def test_calculate_bpm_stats_per_genre(self):
        """Testing if the calculate function handles an empty dataset properly"""
        empty_df = pd.DataFrame(columns=get_columns(self.test_data))
        avg_bpm_per_genre, bpm_stats_per_genre = calculate_bpm_stats_per_genre(empty_df)

        self.assertTrue(avg_bpm_per_genre.empty)
        self.assertTrue(bpm_stats_per_genre.empty)

if __name__ == "__main":
    unittest.main()

    
        
