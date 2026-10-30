def analyze_energy_conservation(energy_data):
    analysis_results = {}
    for appliance, data in energy_data.items():
        before = data["before"]
        after = data["after"]
        absolute_savings = before - after
        percentage_savings = (absolute_savings / before * 100) if before > 0 else 0.0
        
        analysis_results[appliance] = {
            "before": before,
            "after": after,
            "absolute_savings": round(absolute_savings, 2),
            "percentage_savings": round(percentage_savings, 2)
        }
    
    ranked_appliances = sorted(
        analysis_results.items(),
        key=lambda x: x[1]["absolute_savings"],
        reverse=True
    )
    
    return analysis_results, ranked_appliances

if __name__ == "__main__":
    energy_records = {
        "Air Conditioner": {"before": 450.0, "after": 320.0},
        "Refrigerator": {"before": 150.0, "after": 130.0},
        "Lighting": {"before": 80.0, "after": 40.0},
        "Washing Machine": {"before": 120.0, "after": 100.0}
    }
    
    analysis, rankings = analyze_energy_conservation(energy_records)
    print("Analysis:", analysis)
    print("Ranked Appliances:", rankings)
