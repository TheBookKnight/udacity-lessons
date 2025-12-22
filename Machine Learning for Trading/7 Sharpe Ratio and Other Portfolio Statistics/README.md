# Sharpe Ratio and Other Portfolio Statistics

The **Sharpe Ratio** measures risk-adjusted return—it tells you how much excess return you're getting per unit of risk (volatility).

**Higher is better:**
- Higher return → higher Sharpe Ratio
- Lower volatility/risk → higher Sharpe Ratio

## Formula

$$\text{Sharpe Ratio} = \frac{\text{mean}(R_p - R_f)}{\text{std}(R_p - R_f)}$$

Where:
- $R_p$ = portfolio (or stock) daily returns
- $R_f$ = daily risk-free rate

## Risk-Free Rate

Common choices for the risk-free rate:
1. **LIBOR** (London Interbank Offered Rate)
2. **3-month Treasury Bill**
3. **0%** (simplified assumption)

To convert annual interest rate to daily:

$$R_f^{\text{daily}} = \left(1 + \frac{R_f^{\text{annual}}}{252}\right)^{\frac{1}{252}} - 1$$

Note: 252 is the approximate number of trading days per year.

## Annualization

Sharpe Ratio varies by sampling frequency. To standardize, we annualize:

$$SR_{\text{annual}} = K \times SR$$

Where $K = \sqrt{\text{samples per year}}$:
- **Daily:** $K = \sqrt{252}$
- **Weekly:** $K = \sqrt{52}$
- **Monthly:** $K = \sqrt{12}$

## Example Calculation

For daily returns with:
- Mean daily return = 0.001 (0.1%)
- Risk-free rate = 0.0002 (0.02%)
- Std dev = 0.01 (1%)

$$SR_{\text{annual}} = \frac{0.001 - 0.0002}{0.01} \times \sqrt{252} = 0.8 \times 15.875 \approx 12.7$$

## Script

Run [sharpe-ratio.py](sharpe-ratio.py) to calculate the annualized Sharpe Ratio for AAPL stock using 2012 data.

### How to Run

1. `cd` into this subdirectory
2. Run `uv sync` to install dependencies
3. Run `uv run sharpe-ratio.py`
