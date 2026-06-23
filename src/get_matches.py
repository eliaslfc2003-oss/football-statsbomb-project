from statsbombpy import sb

def get_matches(competition_id: int, season_id: int):
    return sb.matches(competition_id=competition_id, season_id=season_id)

if __name__ == "__main__":
    matches = get_matches(43, 106)
    print(matches[["match_id", "home_team", "away_team", "match_date"]].head())