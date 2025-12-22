# How to Optimize a Portfolio

Portfolio optimization finds the ideal allocation of capital across multiple stocks to maximize risk-adjusted returns (Sharpe ratio).

## Script: optimize-portfolio.py

This script uses **Modern Portfolio Theory** and optimization to find the optimal portfolio weights for a given set of stocks.

### How It Works

1. **Load historical price data** for multiple stocks
2. **Calculate daily returns** and compute statistics:
   - Mean returns (expected return for each stock)
   - Covariance matrix (captures correlations between stocks)
3. **Define the optimization problem**:
   - **Objective**: Maximize Sharpe ratio (minimize negative Sharpe ratio)
   - **Constraints**: Weights must sum to 100%
   - **Bounds**: Each weight between 0% and 100%
4. **Run optimizer** to find optimal allocation

### Portfolio Metrics

**Expected Annual Return:**
$$R_p = \sum_{i=1}^{n} w_i \cdot r_i \times 252$$

**Annual Volatility (Risk):**
$$\sigma_p = \sqrt{w^T \Sigma w} \times \sqrt{252}$$

**Sharpe Ratio:**
$$SR = \frac{R_p - R_f}{\sigma_p}$$

Where:
- $w_i$ = weight of stock $i$
- $r_i$ = mean daily return of stock $i$
- $\Sigma$ = covariance matrix
- $R_f$ = risk-free rate (0.01 or 1% assumed)
- 252 = trading days per year

## Why Optimize Different Criteria?

### 1. Maximum Cumulative Return
**Easiest to solve** - just allocate 100% to the single best-performing stock.

**Problem**: Ignores risk. One stock can be extremely volatile.

### 2. Minimum Volatility
Finds the least risky portfolio.

**Problem**: May have very low returns. Safe but unprofitable.

### 3. Maximum Sharpe Ratio (Best Choice)
Balances risk and return - finds the portfolio with the best risk-adjusted returns.

**Why it works**: 
- Penalizes high volatility
- Rewards high returns
- Naturally diversifies across stocks

## Optimization Setup

### Objective Function
We minimize the **negative Sharpe ratio** because optimizers find minima:

```python
f(weights) = -Sharpe_Ratio(weights)
```

### Constraints
- **Sum constraint**: $\sum w_i = 1$ (weights sum to 100%)

### Bounds
- Each weight: $0 \leq w_i \leq 1$ (no short selling, no leverage)

### Initial Guess
Equal allocation: each stock gets $\frac{1}{n}$ of the portfolio.

## How to Run

1. `cd` into this subdirectory
2. Run `uv sync` to install dependencies
3. Run `uv run optimize-portfolio.py`

## Example Output

```
Optimizing portfolio for: ['GLD', 'GOOG', 'IBM', 'SPY']
Date range: 2010-01-01 to 2012-12-31

Optimization successful!

Optimized portfolio allocation:
  GLD:  51.40%
  GOOG:  0.00%
  IBM:  48.60%
  SPY:   0.00%

Portfolio Performance:
  Expected Annual Return:  14.92%
  Annual Volatility:       13.47%
  Sharpe Ratio:             1.03
```

## Key Takeaways

- **Diversification reduces risk**: Optimal portfolios rarely put 100% in one stock
- **Correlation matters**: Stocks that move independently provide better diversification
- **Risk-adjusted returns**: A portfolio with lower returns but much lower volatility can have a better Sharpe ratio than a high-return, high-risk portfolio