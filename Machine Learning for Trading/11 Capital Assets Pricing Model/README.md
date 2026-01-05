# Capital Assets Pricing Model (CAPM)

## Portfolio Fundamentals

**Portfolio Weights:**
- $w_i$ = portion of funds allocated to asset $i$
- Constraint: $\sum |w_i| = 1.0$
- Absolute value accounts for short positions (negative weights)

**Example Portfolio:**
| Stock | Weight |
|-------|--------|
| Google | 0.4 |
| Apple | 0.3 |
| Oracle | 0.5 |
| Netflix | -0.2 (short) |

**Portfolio Returns:**

$$r_p(t) = \sum_{i} w_i \cdot r_i(t)$$

**Example Calculation:**
- Stock A: +1% return, weight = 75%
- Stock B: -2% return, weight = -25% (short)
- Portfolio return: $(0.75 \times 0.01) + (-0.25 \times -0.02) = 0.0125 = 1.25\%$

## Market Portfolio

**Major Market Indices:**
- **US:** S&P 500
- **UK:** FTSE 100
- **Japan:** TOPIX

**Market Sectors:**
- Energy
- Technology
- Manufacturing
- Finance

**Cap-Weighted Index:**

$$w_i = \frac{\text{market cap}_i}{\sum \text{market caps}}$$

## The CAPM Equation

The Capital Assets Pricing Model relates an asset's return to the market return:

$$r_i(t) = \beta_i \cdot r_m(t) + \alpha_i(t)$$

Where:
- $r_i(t)$ = return of asset $i$ at time $t$
- $r_m(t)$ = market return at time $t$
- $\beta_i$ = systematic risk (market sensitivity)
- $\alpha_i(t)$ = excess return (residual)

**Components:**
- **Market component:** $\beta_i \cdot r_m(t)$ (explained by market movements)
- **Residual:** $\alpha_i(t)$ (asset-specific performance)

## CAPM vs Active Management

### Passive Management
- Strategy: Buy and hold index funds
- Assumption: Cannot predict $\alpha$ consistently
- Expected $\alpha = 0$ over time

### Active Management
- Strategy: Select individual stocks with custom weights
- Goal: Identify positive $\alpha$ opportunities
- Overweight stocks expected to outperform
- Underweight or short stocks expected to underperform

## Using CAPM in Practice

**Beta Interpretation:**
- $\beta > 1$: Stock is more volatile than market (amplifies market movements)
- $\beta = 1$: Stock moves with market
- $\beta < 1$: Stock is less volatile than market (defensive)

**Market Scenarios:**
- **Bull market (rising):** High $\beta$ stocks capture more upside
- **Bear market (falling):** Low $\beta$ stocks provide downside protection

**Efficient Market Hypothesis:** According to EMH, consistently beating the market is not possible because all information is already priced in.

## Arbitrage Pricing Theory (APT)

APT extends CAPM by decomposing $\beta$ into multiple factors:

$$r_i(t) = \alpha_i + \beta_{i,1} \cdot f_1(t) + \beta_{i,2} \cdot f_2(t) + ... + \beta_{i,k} \cdot f_k(t) + \epsilon_i(t)$$

**Common Factors:**
- Market index return
- Sector-specific returns (finance, tech, energy, etc.)
- Size factor (small-cap vs large-cap)
- Value factor (growth vs value stocks)
- Momentum

**Advantages:**
- More accurate risk assessment
- Better captures multiple sources of systematic risk
- Useful for portfolio construction and hedging