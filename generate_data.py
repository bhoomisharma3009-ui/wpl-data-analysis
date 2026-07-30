"""
Generates a SAMPLE WPL (Women's Premier League) matches dataset.

IMPORTANT: This is a realistically-structured SAMPLE dataset (schema matches the
real Kaggle WPL dataset), used so the project runs end-to-end out of the box.
For an actual resume project, download the real matches.csv from:
https://www.kaggle.com/datasets/sahiltailor/womens-premier-league-2023-2024-ball-by-ball
and replace dataset.csv with it (same column names, so nothing else changes).

A few real, well-known results are anchored in (2023 & 2025 finals won by Mumbai
Indians, 2024 final won by Royal Challengers Bengaluru) but most individual
league-stage match results are randomly generated for demonstration purposes.
"""
import pandas as pd
import numpy as np
import random

random.seed(42)
np.random.seed(42)

teams = ["Mumbai Indians", "Delhi Capitals", "Royal Challengers Bengaluru",
         "UP Warriorz", "Gujarat Giants"]

venues = {
    "Mumbai Indians": ("Brabourne Stadium", "Mumbai"),
    "Delhi Capitals": ("Arun Jaitley Stadium", "Delhi"),
    "Royal Challengers Bengaluru": ("M. Chinnaswamy Stadium", "Bengaluru"),
    "UP Warriorz": ("BRSABV Ekana Stadium", "Lucknow"),
    "Gujarat Giants": ("Narendra Modi Stadium", "Ahmedabad"),
}

rows = []
match_id = 1

for season, final_winner, final_runner_up in [
    (2023, "Mumbai Indians", "Delhi Capitals"),
    (2024, "Royal Challengers Bengaluru", "Delhi Capitals"),
    (2025, "Mumbai Indians", "Delhi Capitals"),
]:
    season_start = pd.Timestamp(f"{season}-02-23")
    match_date = season_start

    # Round-robin league stage (each pair plays once) = 10 matches
    pairs = [(t1, t2) for i, t1 in enumerate(teams) for t2 in teams[i+1:]]
    random.shuffle(pairs)

    for team1, team2 in pairs:
        toss_winner = random.choice([team1, team2])
        toss_decision = random.choice(["bat", "field"])
        winner = random.choices([team1, team2], weights=[0.5, 0.5])[0]
        win_type = random.choice(["runs", "wickets"])
        win_by_runs = random.randint(5, 45) if win_type == "runs" else 0
        win_by_wickets = random.randint(1, 8) if win_type == "wickets" else 0
        venue, city = venues[team1]

        rows.append({
            "match_id": match_id,
            "season": season,
            "date": match_date.strftime("%Y-%m-%d"),
            "team1": team1,
            "team2": team2,
            "venue": venue,
            "city": city,
            "toss_winner": toss_winner,
            "toss_decision": toss_decision,
            "winner": winner,
            "win_by_runs": win_by_runs,
            "win_by_wickets": win_by_wickets,
            "player_of_match": f"Player_{random.randint(1,25)}"
        })
        match_id += 1
        match_date += pd.Timedelta(days=random.choice([1, 2]))

    # Eliminator (3rd vs 4th placed - approximated randomly among non-finalists)
    others = [t for t in teams if t not in (final_winner, final_runner_up)]
    elim_t1, elim_t2 = random.sample(others, 2)
    elim_winner = random.choice([elim_t1, elim_t2])  # winner must be one of the two playing teams
    venue, city = venues[elim_t1]
    rows.append({
        "match_id": match_id, "season": season, "date": match_date.strftime("%Y-%m-%d"),
        "team1": elim_t1, "team2": elim_t2, "venue": venue, "city": city,
        "toss_winner": elim_t1, "toss_decision": "field",
        "winner": elim_winner, "win_by_runs": random.randint(5, 30), "win_by_wickets": 0,
        "player_of_match": f"Player_{random.randint(1,25)}"
    })
    match_id += 1
    match_date += pd.Timedelta(days=2)

    # Final
    venue, city = venues[final_winner]
    rows.append({
        "match_id": match_id, "season": season, "date": match_date.strftime("%Y-%m-%d"),
        "team1": final_winner, "team2": final_runner_up, "venue": venue, "city": city,
        "toss_winner": final_winner, "toss_decision": "field",
        "winner": final_winner, "win_by_runs": 0, "win_by_wickets": random.randint(3, 7),
        "player_of_match": f"Player_{random.randint(1,25)}"
    })
    match_id += 1

df = pd.DataFrame(rows)
df.to_csv("dataset.csv", index=False)
print(f"Generated {len(df)} matches across {df['season'].nunique()} seasons")
print(df.head())
