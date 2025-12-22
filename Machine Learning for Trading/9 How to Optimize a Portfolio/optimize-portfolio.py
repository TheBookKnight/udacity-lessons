"""Optimize portfolio allocation using optimization techniques."""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

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

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    import os
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def portfolio_performance(weights, mean_returns, cov_matrix):
    """Calculate portfolio performance: return and volatility."""
    returns = np.sum(mean_returns * weights) * 252
    std_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)
    return returns, std_dev

def negative_sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate=0.01):
    """Calculate the negative Sharpe ratio of the portfolio."""
    p_returns, p_std_dev = portfolio_performance(weights, mean_returns, cov_matrix)
    sharpe_ratio = (p_returns - risk_free_rate) / p_std_dev
    return -sharpe_ratio

def optimize_portfolio(symbols, dates):
    """Optimize portfolio allocation to maximize Sharpe ratio."""
    df = get_data(symbols, dates)
    daily_returns = df.pct_change().dropna()
    mean_returns = daily_returns.mean()
    cov_matrix = daily_returns.cov()

    num_assets = len(symbols)
    args = (mean_returns, cov_matrix)
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0, 1) for asset in range(num_assets))
    initial_guess = num_assets * [1. / num_assets,]

    result = spo.minimize(negative_sharpe_ratio, initial_guess, args=args,
                          method='SLSQP', bounds=bounds, constraints=constraints)

    return result

if __name__ == "__main__":
    symbols = ['GLD', 'GOOG', 'IBM', 'SPY']
    dates = pd.date_range('2010-01-01', '2012-12-31')
    
    print("Optimizing portfolio for:", symbols)
    print(f"Date range: {dates[0].date()} to {dates[-1].date()}\n")
    
    result = optimize_portfolio(symbols, dates)
    
    if result.success:
        print("Optimization successful!")
        print("\nOptimized portfolio allocation:")
        for symbol, weight in zip(symbols, result.x):
            print(f"  {symbol}: {weight:>6.2%}")
        
        # Calculate and display performance metrics
        df = get_data(symbols, dates)
        daily_returns = df.pct_change().dropna()
        mean_returns = daily_returns.mean()
        cov_matrix = daily_returns.cov()
        
        ann_return, ann_volatility = portfolio_performance(result.x, mean_returns, cov_matrix)
        sharpe_ratio = (ann_return - 0.01) / ann_volatility
        
        print(f"\nPortfolio Performance:")
        print(f"  Expected Annual Return: {ann_return:>6.2%}")
        print(f"  Annual Volatility:      {ann_volatility:>6.2%}")
        print(f"  Sharpe Ratio:           {sharpe_ratio:>6.2f}")
    else:
        print("Optimization failed!")
        print(result.message)
        
        