import pandas as pd
import random

def fetch_random_data(file_path):
    """
    Fetches 10 consecutive data points from a random start index in a CSV file.

    Args:
        file_path (str): Path to the input CSV file.

    Returns:
        pd.DataFrame: DataFrame containing 10 consecutive rows of data.

    Raises:
        Exception: If the file is empty or has fewer than 10 rows.
    """
    try:
        # Load the CSV file
        df = pd.read_csv(file_path)
        
        # Check if there are enough rows
        if len(df) < 10:
            raise ValueError("Not enough data points in the file.")

        # Sort the data by the Timestamp column
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%d-%m-%Y', errors='coerce')
        df = df.sort_values(by='Timestamp')

        # Select a random starting index
        start_index = random.randint(0, len(df) - 10)
        return df.iloc[start_index:start_index + 10]
    except Exception as e:
        raise Exception(f"Error in fetch_random_data: {e}")
