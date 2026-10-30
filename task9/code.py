import statistics

def analyze_sports_performance(players_data):
    analysis_results = {}
    
    for player, scores in players_data.items():
        if not scores:
            continue
        avg_score = statistics.mean(scores)
        std_dev = statistics.pstdev(scores) if len(scores) > 1 else 0.0
        
        if len(scores) >= 2:
            if scores[-1] > scores[0]:
                trend = "Improving"
            elif scores[-1] < scores[0]:
                trend = "Declining"
            else:
                trend = "Stable"
        else:
            trend = "Single Match"
            
        analysis_results[player] = {
            "average_score": round(avg_score, 2),
            "consistency_std_dev": round(std_dev, 2),
            "trend": trend,
            "total_score": sum(scores)
        }
        
    ranked_players = sorted(
        analysis_results.items(),
        key=lambda x: (x[1]["average_score"], -x[1]["consistency_std_dev"]),
        reverse=True
    )
    
    return analysis_results, ranked_players

if __name__ == "__main__":
    match_scores = {
        "Player_A": [85, 90, 88, 92, 95],
        "Player_B": [70, 80, 75, 90, 95],
        "Player_C": [88, 87, 89, 88, 88],
        "Player_D": [60, 70, 65, 80, 75]
    }
    
    analysis, rankings = analyze_sports_performance(match_scores)
    print("Analysis:", analysis)
    print("Rankings:", rankings)
