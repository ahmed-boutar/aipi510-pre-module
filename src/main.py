'''
This Python script does the processing work on the dataset included in the /data
folder. 
'''
import pandas as pd

def load_dataset(path):
    """Loading dataset locally"""
    df = pd.read_csv(path)
    return df

def get_df_shape(df):
    """Retrieve shape of dataset"""
    return df.shape

def get_columns(df):
    """Retrieve column names"""
    return df.columns.values

def get_null_by_column(df):
    """Check for null values and organize them by columns"""
    return df.isnull().sum()


def calculate_bpm_stats_per_genre(df):
    """Calculate avg, mean, and median bpm per genre"""
    avg_bpm_per_genre = df.groupby('Top Genre')['Beats Per Minute (BPM)'].mean()
    bpm_stats_per_genre = df.groupby('Top Genre')['Beats Per Minute (BPM)'].agg(['mean', 'median'])
    return avg_bpm_per_genre, bpm_stats_per_genre

def display_bpm_stats(avg_bpm_per_genre, bpm_stats_per_genre):
    """Display bpm stats per genre"""
    print("\nAverage BPM per genre")
    print(avg_bpm_per_genre)
    print("\nMean and median BPM per genre")
    print(bpm_stats_per_genre)

def main():
    file_path = "data/Spotify-2000.csv"

    #load dataset
    df = load_dataset(file_path)

    #csv processing
    print("Dataset dimensions:")
    print(get_df_shape(df))
    print("\nDataset Columns:")
    print(get_columns(df))
    print("\nNull values per column:")
    print(get_null_by_column(df))
    avg_bpm_per_genre, bpm_stats_per_genre = calculate_bpm_stats_per_genre(df)
    display_bpm_stats(avg_bpm_per_genre, bpm_stats_per_genre)

if __name__ == "__main__":
    main()
