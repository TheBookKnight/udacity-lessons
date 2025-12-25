def calculate_book_value(tangible_assets, intangible_assets, liabilities, include_intangible=False):
    """
    Calculate the book value of a company.
    
    Args:
        tangible_assets: Dictionary of tangible assets with their values
        intangible_assets: Dictionary of intangible assets with their values
        liabilities: Total liabilities
        include_intangible: Whether to include intangible assets in book value
    
    Returns:
        Book value of the company
    """
    total_tangible = sum(tangible_assets.values())
    total_intangible = sum(intangible_assets.values())
    
    if include_intangible:
        book_value = total_tangible + total_intangible - liabilities
    else:
        book_value = total_tangible - liabilities
    
    return book_value, total_tangible, total_intangible


def calculate_intrinsic_value(annual_dividend, discount_rate):
    """
    Calculate the intrinsic value of a company based on dividend discount model.
    
    Args:
        annual_dividend: Annual dividend payment per share (FV)
        discount_rate: Discount rate as a decimal (e.g., 0.05 for 5%)
    
    Returns:
        Intrinsic value of the company
    """
    if discount_rate == 0:
        raise ValueError("Discount rate cannot be zero")
    
    intrinsic_value = annual_dividend / discount_rate
    return intrinsic_value


def calculate_market_cap(num_shares, stock_price):
    """
    Calculate the market capitalization of a company.
    
    Args:
        num_shares: Number of outstanding shares
        stock_price: Current stock price
    
    Returns:
        Market capitalization
    """
    market_cap = num_shares * stock_price
    return market_cap


def should_buy_stock(book_value, intrinsic_value, market_cap):
    """
    Determine whether to buy a stock based on value comparison.
    
    Args:
        book_value: Book value of the company
        intrinsic_value: Intrinsic value of the company
        market_cap: Market capitalization
    
    Returns:
        Tuple of (decision, reasons)
    """
    reasons = []
    
    if market_cap < book_value:
        reasons.append(f"Market Cap (${market_cap:,.0f}) < Book Value (${book_value:,.0f})")
    
    if market_cap < intrinsic_value:
        reasons.append(f"Market Cap (${market_cap:,.0f}) < Intrinsic Value (${intrinsic_value:,.0f})")
    
    decision = len(reasons) > 0
    
    return decision, reasons


def analyze_company(name, tangible_assets, intangible_assets, liabilities,
                   annual_dividend, discount_rate, num_shares, stock_price,
                   include_intangible=False):
    """
    Perform a complete analysis of whether to buy a company's stock.
    """
    print(f"\n{'='*80}")
    print(f"ANALYZING: {name}")
    print(f"{'='*80}\n")
    
    # Calculate Book Value
    print("📊 BOOK VALUE CALCULATION:")
    print("-" * 40)
    book_value, total_tangible, total_intangible = calculate_book_value(
        tangible_assets, intangible_assets, liabilities, include_intangible
    )
    
    print("Tangible Assets:")
    for asset, value in tangible_assets.items():
        print(f"  - {asset}: ${value:,.0f}")
    print(f"  Total Tangible: ${total_tangible:,.0f}")
    
    print("\nIntangible Assets:")
    for asset, value in intangible_assets.items():
        print(f"  - {asset}: ${value:,.0f}")
    print(f"  Total Intangible: ${total_intangible:,.0f}")
    
    print(f"\nLiabilities: ${liabilities:,.0f}")
    
    if include_intangible:
        print(f"\nBV = (Tangible + Intangible) - Liabilities")
        print(f"BV = (${total_tangible:,.0f} + ${total_intangible:,.0f}) - ${liabilities:,.0f}")
    else:
        print(f"\nBV = Tangible Assets - Liabilities")
        print(f"BV = ${total_tangible:,.0f} - ${liabilities:,.0f}")
    
    print(f"📈 Book Value = ${book_value:,.0f}")
    
    # Calculate Intrinsic Value
    print(f"\n💰 INTRINSIC VALUE CALCULATION:")
    print("-" * 40)
    intrinsic_value = calculate_intrinsic_value(annual_dividend, discount_rate)
    print(f"Annual Dividend: ${annual_dividend:,.0f}")
    print(f"Discount Rate: {discount_rate * 100}%")
    print(f"\nIV = Annual Dividend / Discount Rate")
    print(f"IV = ${annual_dividend:,.0f} / {discount_rate}")
    print(f"📈 Intrinsic Value = ${intrinsic_value:,.0f}")
    
    # Calculate Market Cap
    print(f"\n🏢 MARKET CAPITALIZATION CALCULATION:")
    print("-" * 40)
    market_cap = calculate_market_cap(num_shares, stock_price)
    print(f"Number of Shares: {num_shares:,}")
    print(f"Stock Price: ${stock_price:.2f}")
    print(f"\nMarket Cap = Shares × Price")
    print(f"Market Cap = {num_shares:,} × ${stock_price:.2f}")
    print(f"📈 Market Cap = ${market_cap:,.0f}")
    
    # Decision
    print(f"\n🎯 INVESTMENT DECISION:")
    print("-" * 40)
    decision, reasons = should_buy_stock(book_value, intrinsic_value, market_cap)
    
    print(f"Book Value: ${book_value:,.0f}")
    print(f"Intrinsic Value: ${intrinsic_value:,.0f}")
    print(f"Market Cap: ${market_cap:,.0f}")
    
    if decision:
        print(f"\n✅ RECOMMENDATION: BUY")
        print("\nReasons:")
        for reason in reasons:
            print(f"  ✓ {reason}")
        print("\nThe stock appears undervalued!")
    else:
        print(f"\n❌ RECOMMENDATION: DON'T BUY")
        print("\nReasons:")
        print(f"  ✗ Market Cap (${market_cap:,.0f}) >= Book Value (${book_value:,.0f})")
        print(f"  ✗ Market Cap (${market_cap:,.0f}) >= Intrinsic Value (${intrinsic_value:,.0f})")
        print("\nThe stock appears fairly valued or overvalued.")
    
    print(f"\n{'='*80}\n")


def main():
    # Test Case 1: Clear BUY - Undervalued airline company
    analyze_company(
        name="AirTransport Co. (CLEAR BUY)",
        tangible_assets={
            "Airplanes (10 × $10M)": 100_000_000,
        },
        intangible_assets={
            "Brand Name": 10_000_000,
        },
        liabilities=20_000_000,
        annual_dividend=5_000_000,
        discount_rate=0.05,
        num_shares=1_000_000,
        stock_price=75.00,
        include_intangible=False
    )
    
    # Test Case 2: Clear DON'T BUY - Overvalued tech startup
    analyze_company(
        name="TechStartup Inc. (OVERVALUED)",
        tangible_assets={
            "Office Equipment": 2_000_000,
            "Servers": 3_000_000,
        },
        intangible_assets={
            "Patents": 15_000_000,
            "Brand Value": 20_000_000,
        },
        liabilities=5_000_000,
        annual_dividend=500_000,
        discount_rate=0.08,
        num_shares=5_000_000,
        stock_price=50.00,
        include_intangible=False
    )
    
    # Test Case 3: BUY - Manufacturing company with strong assets
    analyze_company(
        name="GlobalManufacturing Corp. (UNDERVALUED)",
        tangible_assets={
            "Factories (5 × $20M)": 100_000_000,
            "Machinery": 30_000_000,
            "Warehouses": 15_000_000,
            "Vehicles (100 × $50k)": 5_000_000,
        },
        intangible_assets={
            "Patents": 10_000_000,
            "Trademarks": 5_000_000,
        },
        liabilities=50_000_000,
        annual_dividend=8_000_000,
        discount_rate=0.06,
        num_shares=2_000_000,
        stock_price=45.00,
        include_intangible=False
    )
    
    # Test Case 4: DON'T BUY - Heavily indebted retail company
    analyze_company(
        name="RetailChain LLC (HIGH DEBT)",
        tangible_assets={
            "Store Locations (20 × $2M)": 40_000_000,
            "Inventory": 15_000_000,
            "Distribution Centers": 10_000_000,
        },
        intangible_assets={
            "Brand Recognition": 25_000_000,
        },
        liabilities=80_000_000,
        annual_dividend=1_000_000,
        discount_rate=0.10,
        num_shares=500_000,
        stock_price=30.00,
        include_intangible=False
    )
    
    # Test Case 5: BUY - Transportation company with good dividend yield
    analyze_company(
        name="FreightMasters Inc. (GOOD DIVIDEND)",
        tangible_assets={
            "Trucks (200 × $150k)": 30_000_000,
            "Warehouses (3 × $5M)": 15_000_000,
            "Land": 10_000_000,
        },
        intangible_assets={
            "Customer Contracts": 8_000_000,
        },
        liabilities=25_000_000,
        annual_dividend=4_000_000,
        discount_rate=0.07,
        num_shares=1_500_000,
        stock_price=35.00,
        include_intangible=False
    )
    
    # Test Case 6: DON'T BUY - High valuation software company
    analyze_company(
        name="CloudSoft Technologies (GROWTH PREMIUM)",
        tangible_assets={
            "Office Space": 8_000_000,
            "Computers & Equipment": 2_000_000,
        },
        intangible_assets={
            "Software IP": 50_000_000,
            "Customer Base": 30_000_000,
        },
        liabilities=10_000_000,
        annual_dividend=2_000_000,
        discount_rate=0.05,
        num_shares=3_000_000,
        stock_price=80.00,
        include_intangible=False
    )


if __name__ == "__main__":
    main()
