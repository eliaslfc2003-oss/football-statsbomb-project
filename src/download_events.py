from statsbombpy import sb

def get_events(match_id: int):
    return sb.events(match_id=match_id)

if __name__ == "__main__":
    events = get_events(3857256)
    print(events.head())