# What is a Company Worth?

## Overview

This lesson covers fundamental valuation methods to determine whether a stock is worth buying. We analyze three key metrics:
1. **Book Value** - The net asset value of a company
2. **Intrinsic Value** - The present value of future cash flows
3. **Market Capitalization** - The current market valuation

---

## What is an Order?

A stock order consists of:
1. **Action**: Buy or sell
2. **Symbol/Ticker**: The company identifier (e.g., AAPL, GOOGL)
3. **Number of Shares**: Quantity to trade
4. **Order Type**: Market order (current price) or limit order (specified price)
5. **Price**: The execution price

---

## Time Value of Money

### Formula: Present Value
```
PV = FV / (1 + IR)^i
```

Where:
- **PV** = Present Value (today's value)
- **FV** = Future Value (value at a future date)
- **IR** = Interest Rate (as a decimal)
- **i** = Number of years into the future

### Example
If the US Government interest rate is 1%:

```
PV = $1 / (1 + 0.01)^1
PV = $1 / 1.01
PV = $0.99
```

**Interpretation**: $1 received one year from now is worth only $0.99 today.

---

## Company Valuation Methods

### 1. Intrinsic Value (IV)

**Concept**: The theoretical "true value" based on future dividend payments, discounted to present value.

#### Formula
```
IV = Annual Dividend / Discount Rate
```

or

```
IV = FV / DR
```

Where:
- **IV** = Intrinsic Value
- **FV** = Future Value (annual dividend payment)
- **DR** = Discount Rate (required rate of return)

#### Key Terms
- **Interest Rate**: Used to calculate future value from present value
- **Discount Rate**: Used to calculate present value from future value (same concept, opposite direction)

#### Example
```
Annual Dividend = $5,000,000
Discount Rate = 5% (0.05)

IV = $5,000,000 / 0.05
IV = $100,000,000
```

**Interpretation**: If a company pays $5M annually in dividends forever, with a 5% discount rate, the company is worth $100M.

---

### 2. Book Value (BV)

**Concept**: The net value of a company's tangible assets after subtracting liabilities.

#### Formula (Conservative Approach)
```
BV = Tangible Assets - Liabilities
```

#### Formula (Including Intangibles)
```
BV = (Tangible Assets + Intangible Assets) - Liabilities
```

Where:
- **Tangible Assets**: Physical items like factories, vehicles, equipment, land, inventory
- **Intangible Assets**: Patents, trademarks, brand value, customer contracts
- **Liabilities**: Loans, debts, obligations

**Note**: Many investors exclude intangible assets for a more conservative valuation.

#### Example 1: Airline Company
```
Tangible Assets:
  - Airplanes: 10 × $10M = $100,000,000

Intangible Assets:
  - Brand Name = $10,000,000

Liabilities:
  - Loan = $20,000,000

BV (excluding intangibles) = $100M - $20M = $80,000,000
BV (including intangibles) = ($100M + $10M) - $20M = $90,000,000
```

#### Example 2: Manufacturing Company
```
Tangible Assets:
  - Factories: 5 × $20M = $100,000,000
  - Machinery = $30,000,000
  - Warehouses = $15,000,000
  - Vehicles: 100 × $50k = $5,000,000
  Total Tangible = $150,000,000

Intangible Assets:
  - Patents = $10,000,000
  - Trademarks = $5,000,000
  Total Intangible = $15,000,000

Liabilities = $50,000,000

BV (excluding intangibles) = $150M - $50M = $100,000,000
BV (including intangibles) = $165M - $50M = $115,000,000
```

---

### 3. Market Capitalization (Market Cap)

**Concept**: The total market value of a company's outstanding shares.

#### Formula
```
Market Cap = Number of Shares × Stock Price
```

#### Example
```
Shares Outstanding = 1,000,000
Stock Price = $75.00

Market Cap = 1,000,000 × $75
Market Cap = $75,000,000
```

---

## Factors Affecting Stock Price

Stock prices are influenced by three main factors:

1. **Company-Specific**: Earnings, management, products, news
2. **Sector/Industry**: Industry trends, regulations, competition
3. **Overall Market**: Economic conditions, interest rates, investor sentiment

---

## Investment Decision Framework

### When to BUY a Stock

A stock may be undervalued (worth buying) if:

✅ **Market Cap < Book Value**
- The market is valuing the company below its net asset value
- You're essentially buying assets at a discount

✅ **Market Cap < Intrinsic Value**
- The market is valuing the company below its future earnings potential
- The dividend yield suggests good returns

### Complete Example: Should You Buy?

#### Company Profile
```
Tangible Assets:
  - Airplanes: 10 × $10M = $100,000,000

Intangible Assets:
  - Brand Name = $10,000,000

Liabilities:
  - Loan = $20,000,000

Dividends:
  - Annual Dividend = $5,000,000
  - Discount Rate = 5%

Market Data:
  - Shares = 1,000,000
  - Stock Price = $75
```

#### Calculations

**1. Book Value (excluding intangibles)**
```
BV = $100M - $20M = $80,000,000
```

**2. Intrinsic Value**
```
IV = $5,000,000 / 0.05 = $100,000,000
```

**3. Market Capitalization**
```
Market Cap = 1,000,000 × $75 = $75,000,000
```

#### Decision

**✅ YES, BUY THIS STOCK**

Reasons:
- Market Cap ($75M) < Book Value ($80M) → $5M discount to assets
- Market Cap ($75M) < Intrinsic Value ($100M) → $25M discount to earnings value
- The stock is trading below both fundamental valuations

**Note**: While this example shows clear undervaluation, such opportunities are rare in efficient markets.

---

## Running the Analysis Script

The `analyze-company-worth.py` script contains six test cases demonstrating different scenarios:

1. **Clear BUY**: Undervalued airline company
2. **OVERVALUED**: Tech startup with high market cap
3. **UNDERVALUED**: Manufacturing company with strong assets
4. **HIGH DEBT**: Retail company with excessive liabilities
5. **GOOD DIVIDEND**: Transportation company with solid dividend yield
6. **GROWTH PREMIUM**: Software company trading at a premium

### Run the script:
```bash
cd "/Users/joshuacadavez/Documents/GitHub/udacity-lessons/Machine Learning for Trading/10 What is a Company Worth"
python analyze-company-worth.py
```

Each test case shows detailed calculations for all three valuation methods and provides a clear buy/don't buy recommendation with supporting reasons.