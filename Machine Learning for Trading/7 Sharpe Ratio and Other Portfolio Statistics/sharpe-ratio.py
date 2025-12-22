import os
import pandas as pd
import numpy as np

NUM_TRADING_DAYS = 252

def run_sharpe_ratio():
    """Calculate and print the Sharpe ratio for a given stock symbol."""
    def symbol_to_path(symbol, base_dir="data"):
        """Return CSV file path given ticker symbol."""
        return os.path.join(base_dir, "{}.csv".format(str(symbol)))

    def get_data(symbols, dates):
        """Read stock data (adjusted close) for given symbols from CSV files."""
        df = pd.DataFrame(index=dates)

        for symbol in symbols:
            df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                                  parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
            df_temp = df_temp.rename(columns={'Adj Close': symbol})
            df = df.join(df_temp)
        
        # Drop rows with missing data
        df = df.dropna()
        return df

    def compute_daily_returns(df):
        """Compute and return the daily return values."""
        daily_returns = df.pct_change()
        daily_returns.iloc[0, :] = 0  # set daily returns for row 0 to 0
        return daily_returns

    # Define a date range (using the actual data range in AAPL.csv)
    dates = pd.date_range('2023-05-26', '2024-05-24')

    # Choose stock symbols to read
    symbols = ['AAPL']

    # Get stock data
    df = get_data(symbols, dates)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)

    # Compute Sharpe ratio
    sharpe_ratio = np.sqrt(NUM_TRADING_DAYS) * (daily_returns['AAPL'].mean() / daily_returns['AAPL'].std())
    print("Sharpe Ratio for AAPL: ", sharpe_ratio)


run_sharpe_ratio()