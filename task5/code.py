def allocate_resources(inventory, activities):
    remaining_inventory = inventory.copy()
    sorted_activities = sorted(activities, key=lambda x: x["priority"], reverse=True)
    allocations = {}
    
    for act in sorted_activities:
        name = act["name"]
        demands = act["demand"]
        allocated = {}
        for item, qty in demands.items():
            available = remaining_inventory.get(item, 0)
            given = min(qty, available)
            allocated[item] = given
            remaining_inventory[item] = available - given
        
        shortages = {item: demands[item] - allocated[item] for item in demands}
        allocations[name] = {
            "allocated": allocated,
            "shortage": shortages
        }
        
    return allocations, remaining_inventory

if __name__ == "__main__":
    available_inventory = {
        "Projectors": 3,
        "Laptops": 5,
        "Microphones": 4
    }
    
    activity_requests = [
        {"name": "Tech Symposium", "priority": 1, "demand": {"Projectors": 2, "Laptops": 4, "Microphones": 2}},
        {"name": "Cultural Fest", "priority": 3, "demand": {"Projectors": 2, "Laptops": 2, "Microphones": 3}},
        {"name": "Debate Club", "priority": 2, "demand": {"Projectors": 1, "Laptops": 1, "Microphones": 1}}
    ]
    
    results, left_over = allocate_resources(available_inventory, activity_requests)
    print("Allocations:", results)
    print("Remaining Inventory:", left_over)
