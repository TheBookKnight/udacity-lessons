# Statistical Analysis of Time Series

This directory demonstrates key statistical techniques for analyzing stock price data.

## Scripts

### compute-global-stats.py
Computes **global statistics** (mean, median, standard deviation) across the entire time period for multiple stocks. Useful for understanding overall performance and volatility.

### compute-rolling-statistics.py
Calculates and plots the **rolling mean** (moving average) using a 20-day window. This smooths out short-term price fluctuations to reveal trends.

### compute-bollinger-bands.py
Generates **Bollinger Bands**—upper and lower bands representing ±2 standard deviations from the rolling mean. These identify overbought/oversold conditions for potential trading signals.

### compute-daily-returns.py
Computes **daily returns** (percentage change day-over-day) using `pct_change()`. This normalizes price movements across different stocks, making them comparable regardless of absolute price.

## How to Run

1. `cd` into this subdirectory
2. Run `uv sync` to install dependencies
3. Run any script: `uv run <script-name>.py`

## Key Concepts

### Rolling Mean
The **rolling mean** is a moving average calculated over a sliding window (e.g., 20 days). It smooths price data to identify trends.

![alt text](image-1.png)

### Bollinger Bands
**Bollinger Bands** consist of:
- Rolling mean (center line)
- Upper band (mean + 2 standard deviations)
- Lower band (mean - 2 standard deviations)

Trading signals:
- Price touches **lower band** → potential buy signal (oversold)
- Price touches **upper band** → potential sell signal (overbought)

![alt text](image.png)

### Daily Returns
**Daily returns** measure the percentage change in price from one day to the next:

$$\text{Daily Return}_t = \frac{\text{Price}_t - \text{Price}_{t-1}}{\text{Price}_{t-1}}$$

This allows comparing stocks with different price ranges (e.g., a \$10 stock vs a \$1000 stock).
