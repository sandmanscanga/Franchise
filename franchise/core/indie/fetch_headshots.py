from framework.driver import get_nfl_json
import requests
import os


def fetch_headshots(outdir):
    outdir = outdir.rstrip("/")
    os.makedirs(outdir, exist_ok=True)

    teams = []

    nfl_json = get_nfl_json()
    for team_json in nfl_json.values():
        team_json = team_json.get("roster")
        team_json = team_json.get("page").get("content")
        team_json = team_json.get("roster")

        athletes = []
        for group in team_json.get("groups"):
            for athlete in group.get("athletes"):
                athletes.append(athlete)

        for player_id, athlete in enumerate(athletes):

            ## Main Processing
            headshot_url = athlete.get("headshot")
            player_guid = athlete.get("guid")

            if not "nophoto" in headshot_url:
                outpath = f"{outdir}/{player_guid}.png"
                if os.path.isfile(outpath):
                    print(f"[*] Skipping headshot: {outpath}")
                    continue

                print(f"[+] Getting {team_id}/{player_id} headshot: {headshot_url}")
                r = requests.get(headshot_url, timeout=10, allow_redirects=False)
                with open(outpath, "wb") as f:
                    f.write(r.content)
