import pandas as pd
import matplotlib.pyplot as plt


def show_plot():
    df = pd.read_csv("data/AAPL.csv")
    print(df['Adj Close'])
    df[['Adj Close', 'Close']].plot()
    plt.xlabel('Date')
    plt.ylabel('Stock Value')
    plt.show()  # must be called to show plots


def get_mean_volume():
    """Return the mean volume for stock indicated by symbol.

    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("data/AAPL.csv")  # read in data
    print(df.mean())


def read_last_five_rows():
    df = pd.read_csv("data/AAPL.csv")
    # Prints last 5 rows of the data frame in each sheet
    for n, d in df.items():
        print('Sheet Name:{}'.format(n))
        print(d.tail())


def test_run():
    show_plot()


if __name__ == "__main__":
    test_run()
