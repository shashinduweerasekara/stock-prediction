import os
import pandas as pd
from data_fetcher import fetch_random_data
from predictor import predict_next_values

def main(input_folder, output_folder):
    """
    Main function to fetch data, predict values, and save output.

    Args:
        input_folder (str): Path to the folder containing input CSV files.
        output_folder (str): Path to the folder where output CSV files will be saved.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        try:
            # Fetch random data
            random_data = fetch_random_data(file_path)
            
            # Predict next 3 values
            predictions = predict_next_values(random_data)

            # Append predictions to the DataFrame
            last_timestamp = random_data.iloc[-1]['Timestamp']
            predicted_timestamps = ['n+1', 'n+2', 'n+3']
            stock_id = random_data.iloc[0]['Stock-ID']

            for i, pred in enumerate(predictions):
                # Create a new DataFrame for the row to be added
                new_row = pd.DataFrame([{
                    'Stock-ID': stock_id,
                    'Timestamp': predicted_timestamps[i],
                    'Stock Price': pred
                }])
                # Concatenate the new row with the existing DataFrame
                random_data = pd.concat([random_data, new_row], ignore_index=True)

            # Save to output folder
            output_file_path = os.path.join(output_folder, f"predicted_{file_name}")
            random_data.to_csv(output_file_path, index=False)
            print(f"Processed and saved: {output_file_path}")
        except Exception as e:
            print(f"Error processing {file_name}: {e}")

if __name__ == "__main__":
    main("data", "output")
