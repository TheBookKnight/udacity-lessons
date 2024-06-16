'''Build a dataframe in pandas'''
import pandas as pd


def test_run():
    # Defines date range
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date, end_date)

    # Create an empty dataframe
    # setup dates as indices
    df1 = pd.DataFrame(index=dates)

    # Read SPY data into temporary dataframe
    dfSPY = pd.read_csv("data/SPY.csv",
                        # use Dates as the index columnss
                        index_col="Date",
                        parse_dates=True,
                        usecols=['Date', 'Adj Close'],
                        # identify which values are Not A Number, they are NaN
                        na_values=['nan']
                        )

    # Join the two dataframes using DataFrame.join()
    df1 = df1.join(dfSPY)

    # Drop NaN values (which are weekends and holidays defined by NSYE)
    df1 = df1.dropna()
    print(df1)


if __name__ == "__main__":
    test_run()
