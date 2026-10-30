def analyze_water_distribution(data):
    analysis_results = {}
    for area, records in data.items():
        total_supply = sum(r["supply"] for r in records)
        total_demand = sum(r["demand"] for r in records)
        shortage = max(0, total_demand - total_supply)
        fulfillment = (total_supply / total_demand * 100) if total_demand > 0 else 100.0
        analysis_results[area] = {
            "total_supply": total_supply,
            "total_demand": total_demand,
            "total_shortage": shortage,
            "fulfillment_percentage": round(fulfillment, 2)
        }
    
    sorted_areas = sorted(
        analysis_results.items(),
        key=lambda x: x[1]["fulfillment_percentage"]
    )
    
    return analysis_results, sorted_areas

if __name__ == "__main__":
    water_data = {
        "North Zone": [
            {"day": 1, "supply": 400, "demand": 500},
            {"day": 2, "supply": 450, "demand": 500},
            {"day": 3, "supply": 420, "demand": 480}
        ],
        "South Zone": [
            {"day": 1, "supply": 600, "demand": 600},
            {"day": 2, "supply": 580, "demand": 600},
            {"day": 3, "supply": 590, "demand": 610}
        ],
        "East Zone": [
            {"day": 1, "supply": 200, "demand": 450},
            {"day": 2, "supply": 250, "demand": 450},
            {"day": 3, "supply": 220, "demand": 460}
        ]
    }
    
    summary, ranked = analyze_water_distribution(water_data)
    print("Summary:", summary)
    print("Most Underserved Area:", ranked[0][0])
