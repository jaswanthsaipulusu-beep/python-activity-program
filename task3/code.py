def analyze_price_fluctuations(product_prices, threshold):
    analysis = {}
    flagged_products = []
    
    for product, prices in product_prices.items():
        if len(prices) < 2:
            analysis[product] = {"max_fluctuation": 0.0, "changes": []}
            continue
        
        changes = []
        for i in range(1, len(prices)):
            prev = prices[i - 1]
            curr = prices[i]
            if prev == 0:
                change = 0.0
            else:
                change = ((curr - prev) / prev) * 100
            changes.append(round(change, 2))
        
        max_fluctuation = max(changes, key=abs) if changes else 0.0
        
        analysis[product] = {
            "max_fluctuation": max_fluctuation,
            "changes": changes
        }
        
        if abs(max_fluctuation) > threshold:
            flagged_products.append(product)
            
    return analysis, flagged_products

if __name__ == "__main__":
    historical_prices = {
        "Product_A": [100.0, 105.0, 102.0, 115.0, 110.0],
        "Product_B": [50.0, 48.0, 45.0, 60.0, 58.0],
        "Product_C": [200.0, 202.0, 201.0, 203.0, 202.0]
    }
    threshold_value = 15.0
    
    results, flagged = analyze_price_fluctuations(historical_prices, threshold_value)
    print("Analysis:", results)
    print("Flagged Products:", flagged)
