def predict_next_values(data):
    """
    Predicts the next 3 stock prices based on the last 10 data points.

    Args:
        data (pd.DataFrame): DataFrame containing 10 rows with a 'Stock Price' column.

    Returns:
        list: List of predicted stock prices [n+1, n+2, n+3].
    """
    try:
        # Get the last stock price (n)
        n = data.iloc[-1]['Stock Price']

        # Find the second highest value in the 10 data points
        second_highest = sorted(data['Stock Price'].unique())[-2]

        # Calculate predictions
        n_plus_1 = second_highest
        n_plus_2 = n + (n_plus_1 - n) / 2
        n_plus_3 = n_plus_1 + (n_plus_2 - n_plus_1) / 4

        # Return predictions as a list
        return [n_plus_1, n_plus_2, n_plus_3]
    except Exception as e:
        raise Exception(f"Error in predict_next_values: {e}")
