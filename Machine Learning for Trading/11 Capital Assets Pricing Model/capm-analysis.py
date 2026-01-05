"""
Capital Assets Pricing Model (CAPM) Analysis

This script demonstrates:
1. Calculating portfolio returns with long and short positions
2. Computing beta and alpha using linear regression
3. Analyzing risk-return relationship
4. Comparing passive vs active management approaches
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def calculate_portfolio_return(weights, returns):
    """
    Calculate portfolio return given weights and individual returns.
    
    Args:
        weights: Dictionary of {stock: weight}
        returns: Dictionary of {stock: return}
    
    Returns:
        Portfolio return
    """
    portfolio_return = sum(weights[stock] * returns[stock] for stock in weights)
    return portfolio_return


def calculate_beta_alpha(stock_returns, market_returns):
    """
    Calculate beta and alpha using linear regression.
    
    CAPM: r_i = alpha + beta * r_m + epsilon
    
    Args:
        stock_returns: Array of stock returns
        market_returns: Array of market returns
    
    Returns:
        Tuple of (beta, alpha, r_squared)
    """
    # Linear regression: stock_returns = alpha + beta * market_returns
    slope, intercept, r_value, p_value, std_err = stats.linregress(
        market_returns, stock_returns
    )
    
    beta = slope
    alpha = intercept
    r_squared = r_value ** 2
    
    return beta, alpha, r_squared


def example_portfolio_returns():
    """Example 1: Calculate portfolio returns with long and short positions."""
    print("=" * 60)
    print("Example 1: Portfolio Returns Calculation")
    print("=" * 60)
    
    # Portfolio with long and short positions
    weights = {
        'Google': 0.4,
        'Apple': 0.3,
        'Oracle': 0.5,
        'Netflix': -0.2  # Short position
    }
    
    # Daily returns (as decimals)
    returns_scenario1 = {
        'Google': 0.015,   # +1.5%
        'Apple': 0.008,    # +0.8%
        'Oracle': -0.005,  # -0.5%
        'Netflix': 0.020   # +2.0%
    }
    
    # Verify weights sum to 1.0 (absolute values)
    total_weight = sum(abs(w) for w in weights.values())
    print(f"\nTotal portfolio weight (absolute): {total_weight:.2f}")
    
    # Calculate portfolio return
    portfolio_return = calculate_portfolio_return(weights, returns_scenario1)
    
    print("\nPortfolio Composition:")
    for stock, weight in weights.items():
        position_type = "Long" if weight > 0 else "Short"
        print(f"  {stock:10s}: {weight:6.1%} ({position_type})")
    
    print("\nDaily Returns:")
    for stock, ret in returns_scenario1.items():
        print(f"  {stock:10s}: {ret:6.2%}")
    
    print(f"\nPortfolio Return: {portfolio_return:.4f} ({portfolio_return:.2%})")
    
    # Show contribution of each stock
    print("\nContribution to Portfolio Return:")
    for stock in weights:
        contribution = weights[stock] * returns_scenario1[stock]
        print(f"  {stock:10s}: {contribution:7.4f} ({contribution:.2%})")


def example_capm_regression():
    """Example 2: Calculate beta and alpha using simulated data."""
    print("\n" + "=" * 60)
    print("Example 2: CAPM Beta and Alpha Calculation")
    print("=" * 60)
    
    # Simulate 252 trading days (1 year)
    np.random.seed(42)
    days = 252
    
    # Market returns (e.g., S&P 500)
    market_returns = np.random.normal(0.0005, 0.01, days)  # Mean ~0.05%, std ~1%
    
    # Stock returns with different betas
    stocks = {
        'Tech Stock (High Beta)': {
            'beta': 1.5,
            'alpha': 0.0002,  # Slight outperformance
        },
        'Utility Stock (Low Beta)': {
            'beta': 0.6,
            'alpha': -0.0001,  # Slight underperformance
        },
        'Market Index Fund': {
            'beta': 1.0,
            'alpha': 0.0,  # Tracks market exactly
        }
    }
    
    print("\nSimulated Stock Characteristics:")
    print(f"Days simulated: {days}")
    print(f"Market avg return: {market_returns.mean():.4%} daily")
    print(f"Market volatility: {market_returns.std():.4%} daily\n")
    
    # Generate stock returns based on CAPM
    results = {}
    for stock_name, params in stocks.items():
        beta = params['beta']
        alpha = params['alpha']
        
        # CAPM equation with random noise
        noise = np.random.normal(0, 0.005, days)
        stock_returns = alpha + beta * market_returns + noise
        
        # Calculate beta and alpha using regression
        calc_beta, calc_alpha, r_squared = calculate_beta_alpha(
            stock_returns, market_returns
        )
        
        results[stock_name] = {
            'true_beta': beta,
            'calc_beta': calc_beta,
            'true_alpha': alpha,
            'calc_alpha': calc_alpha,
            'r_squared': r_squared,
            'returns': stock_returns,
            'avg_return': stock_returns.mean(),
            'volatility': stock_returns.std()
        }
    
    # Display results
    print(f"{'Stock':<30} {'True β':<10} {'Calc β':<10} {'True α':<12} {'Calc α':<12} {'R²':<8}")
    print("-" * 90)
    for stock_name, data in results.items():
        print(f"{stock_name:<30} "
              f"{data['true_beta']:<10.3f} "
              f"{data['calc_beta']:<10.3f} "
              f"{data['true_alpha']:<12.6f} "
              f"{data['calc_alpha']:<12.6f} "
              f"{data['r_squared']:<8.3f}")
    
    print("\nPerformance Summary:")
    print(f"{'Stock':<30} {'Avg Return':<15} {'Volatility':<15}")
    print("-" * 60)
    for stock_name, data in results.items():
        print(f"{stock_name:<30} "
              f"{data['avg_return']:<15.4%} "
              f"{data['volatility']:<15.4%}")
    
    return market_returns, results


def example_beta_scenarios():
    """Example 3: Compare portfolio performance across market scenarios."""
    print("\n" + "=" * 60)
    print("Example 3: Beta Strategy in Different Market Conditions")
    print("=" * 60)
    
    scenarios = {
        'Bull Market': 0.10,      # Market up 10%
        'Bear Market': -0.15,     # Market down 15%
        'Flat Market': 0.02       # Market up 2%
    }
    
    portfolios = {
        'Aggressive (β=1.5)': 1.5,
        'Moderate (β=1.0)': 1.0,
        'Defensive (β=0.5)': 0.5
    }
    
    print("\nPortfolio Returns by Market Scenario:")
    print(f"{'Scenario':<20} " + " ".join(f"{p:>18}" for p in portfolios.keys()))
    print("-" * 80)
    
    for scenario, market_return in scenarios.items():
        returns = []
        for portfolio_name, beta in portfolios.items():
            # Assuming alpha = 0 for simplicity
            portfolio_return = beta * market_return
            returns.append(portfolio_return)
        
        print(f"{scenario:<20} " + 
              " ".join(f"{r:>17.2%}" for r in returns))
    
    print("\nKey Insights:")
    print("  • High beta (>1): Amplifies market movements (higher risk, higher potential return)")
    print("  • Low beta (<1): Dampens market movements (lower risk, lower potential return)")
    print("  • Beta = 1: Moves in line with the market")


def example_active_vs_passive():
    """Example 4: Compare active vs passive management."""
    print("\n" + "=" * 60)
    print("Example 4: Active vs Passive Management")
    print("=" * 60)
    
    # Simulate 5 years of monthly returns
    np.random.seed(42)
    months = 60
    
    # Market index return
    market_returns = np.random.normal(0.008, 0.04, months)  # ~10% annual return
    
    # Passive portfolio (index fund with minimal tracking error)
    passive_returns = market_returns + np.random.normal(0, 0.002, months)
    
    # Active portfolio (trying to beat market, but with mixed results)
    # Some alpha, but also higher costs and variability
    active_returns = 1.1 * market_returns + np.random.normal(0.002, 0.05, months)
    
    # Calculate cumulative returns
    market_cumulative = (1 + market_returns).cumprod() - 1
    passive_cumulative = (1 + passive_returns).cumprod() - 1
    active_cumulative = (1 + active_returns).cumprod() - 1
    
    print("\n5-Year Performance Summary:")
    print(f"{'Strategy':<20} {'Total Return':<15} {'Avg Monthly':<15} {'Volatility':<15}")
    print("-" * 65)
    print(f"{'Market Index':<20} "
          f"{market_cumulative[-1]:<15.2%} "
          f"{market_returns.mean():<15.4%} "
          f"{market_returns.std():<15.4%}")
    print(f"{'Passive (Index Fund)':<20} "
          f"{passive_cumulative[-1]:<15.2%} "
          f"{passive_returns.mean():<15.4%} "
          f"{passive_returns.std():<15.4%}")
    print(f"{'Active Management':<20} "
          f"{active_cumulative[-1]:<15.2%} "
          f"{active_returns.mean():<15.4%} "
          f"{active_returns.std():<15.4%}")
    
    # Calculate Sharpe ratios (assuming risk-free rate = 0.002 monthly)
    risk_free_rate = 0.002
    
    sharpe_market = (market_returns.mean() - risk_free_rate) / market_returns.std()
    sharpe_passive = (passive_returns.mean() - risk_free_rate) / passive_returns.std()
    sharpe_active = (active_returns.mean() - risk_free_rate) / active_returns.std()
    
    print("\nRisk-Adjusted Performance (Sharpe Ratio):")
    print(f"  Market Index:       {sharpe_market:.3f}")
    print(f"  Passive Portfolio:  {sharpe_passive:.3f}")
    print(f"  Active Portfolio:   {sharpe_active:.3f}")


def main():
    """Run all CAPM examples."""
    print("\nCAPITAL ASSETS PRICING MODEL (CAPM) - EXAMPLES\n")
    
    # Example 1: Portfolio returns
    example_portfolio_returns()
    
    # Example 2: Beta and alpha calculation
    example_capm_regression()
    
    # Example 3: Beta strategies
    example_beta_scenarios()
    
    # Example 4: Active vs passive
    example_active_vs_passive()
    
    print("\n" + "=" * 60)
    print("Analysis Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
