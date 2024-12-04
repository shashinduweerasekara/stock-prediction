# Stock Price Prediction

## Overview
This project predicts the next three stock prices for given input files based on historical data.

## How It Works
1. Randomly selects 10 rows of data from each input file.
2. Predicts the next three prices using a simple algorithm:
   - **n+1**: Second highest value in the selected rows.
   - **n+2**: Halfway between the last value and `n+1`.
   - **n+3**: A quarter difference between `n+1` and `n+2`.

## Requirements
- Python 3.7 or above
- Libraries: `pandas`, `numpy`

## Setup Instructions
1. Clone this repository or copy the project folder.
2. Install required libraries:
   ```bash
   pip install pandas numpy
