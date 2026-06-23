from statsbombpy import sb

def get_competitions():
    return sb.competitions()

if __name__ == "__main__":
    comps = get_competitions()
    print(comps.head())