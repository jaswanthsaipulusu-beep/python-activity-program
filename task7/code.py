def analyze_retail_orders(inventory, records):
    updated_inventory = inventory.copy()
    analysis_results = {}
    inconsistencies = []
    
    for product, data in records.items():
        ordered = data.get("ordered", 0)
        dispatched = data.get("dispatched", 0)
        returned = data.get("returned", 0)
        
        product_errors = []
        if dispatched > ordered:
            product_errors.append("Dispatched quantity exceeds ordered quantity.")
        if returned > dispatched:
            product_errors.append("Returned quantity exceeds dispatched quantity.")
            
        if product_errors:
            inconsistencies.append({product: product_errors})
            continue
            
        outstanding = ordered - dispatched
        current_stock = updated_inventory.get(product, 0)
        new_stock = current_stock - dispatched + returned
        updated_inventory[product] = new_stock
        
        analysis_results[product] = {
            "outstanding_orders": outstanding,
            "updated_stock": new_stock
        }
        
    return analysis_results, updated_inventory, inconsistencies

if __name__ == "__main__":
    initial_inventory = {
        "Item_X": 100,
        "Item_Y": 50,
        "Item_Z": 200
    }
    
    order_records = {
        "Item_X": {"ordered": 40, "dispatched": 35, "returned": 5},
        "Item_Y": {"ordered": 20, "dispatched": 25, "returned": 2},
        "Item_Z": {"ordered": 60, "dispatched": 60, "returned": 0}
    }
    
    analysis, stock, errors = analyze_retail_orders(initial_inventory, order_records)
    print("Analysis:", analysis)
    print("Updated Inventory:", stock)
    print("Inconsistencies:", errors)
