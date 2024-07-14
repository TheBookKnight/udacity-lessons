"""Plot a histogram"""

import pandas as pd
import matplotlib.pyplot as plt

from utils.stock import get_data, plot_data


def compute_daily_returns(df):
    """Compute and return the daily return values"""
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.iloc[0, :] = 0  # set daily returns for row 0 to 0
    return daily_returns


def test_run():
    # Read data
    dates = pd.date_range('2010-01-01', '2012-12-31')
    symbols = ['SPY']
    df = get_data(symbols, dates)
    plot_data(df, title="Stock Data", ylabel="Stock Value", xlabel="Date")

    # Compute daily returns
    daily_returns = compute_daily_returns(df)

    # Plot a histogram
    daily_returns.hist(bins=20)
    plt.show()


test_run()
