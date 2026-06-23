# football-statsbomb-project

A Python project for exploring and analyzing football data using StatsBomb open data.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python src/football_statsbomb/get_competitions.py
python src/football_statsbomb/get_matches.py
python src/football_statsbomb/download_events.py
```