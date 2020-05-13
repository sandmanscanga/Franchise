from bs4 import BeautifulSoup
import requests
import json
import time
import os


def fetch_json(url, filepath, reinit=False):
    if not os.path.isfile(filepath) or reinit:
        print(f"GET {url}")
        r = requests.get(
            url=url,
            timeout=10,
            allow_redirects=False
        )
        html = r.text
        filedir = "/".join(filepath.split("/")[:-1])
        os.makedirs(filedir, exist_ok=True)
        with open(filepath, "w") as f:
            f.write(html)
    else:
        with open(filepath, "r") as f:
            html = f.read()

    soup = BeautifulSoup(html, "lxml")
    for tag in soup.findAll("script"):
        if "__espnfitt__" in str(tag):
            partial_json = "=".join(str(tag).split("=")[2:])
            json_data = partial_json.replace(";</script>", "")
            json_dict = json.loads(json_data)
            break
    else:
        raise Exception(f"JSON not found: {url}")

    return json_dict


def get_team_index(json_dict):
    teams = []

    json_dict = json_dict.get("page")
    json_dict = json_dict.get("content")
    json_dict = json_dict.get("leagueTeams")

    for column in json_dict.get("columns"):
        for group in column.get("groups"):
            div_reg = group.get("nm")
            (division, region) = div_reg.split()

            for tm in group.get("tms"):
                team_name = tm.get("n")
                team_logo = tm.get("p")
                team_id = tm.get("id")

                links = {}
                for lk in tm.get("lk")[1:-1]:
                    title = lk.get("t")
                    uri = lk.get("u")
                    links[title] = f"https://www.espn.com{uri}"

                teams.append({
                    "division": division,
                    "region": region,
                    "id": team_id,
                    "name": team_name,
                    "logo": team_logo,
                    "links": links
                })

    return teams


def get_nfl_json(reinit=False):
    cache_dir = __file__.replace("framework/driver.py", "cache")
    nfl_json_path = f"{cache_dir}/nfl.json"

    if not os.path.isfile(nfl_json_path) or reinit:
        url = "https://www.espn.com/nfl/teams"
        filepath = f"{cache_dir}/nfl.html"
        json_dict = fetch_json(url, filepath)

        teams = get_team_index(json_dict)

        nfl_json = {}
        for team in teams:
            team_links = team.get("links")
            (team_abbr, team_name) = list(team_links.values())[0].split("/")[-2:]

            team_parts = {}
            for link_title, team_link in team_links.items():
                link_path = f"{cache_dir}/teams/{team_name}/{link_title}.html"
                team_json_part = fetch_json(team_link, link_path)
                team_parts[link_title] = team_json_part

            nfl_json[team_name] = team_parts

        nfl_json_dir = "/".join(nfl_json_path.split("/")[:-1])
        os.makedirs(nfl_json_dir, exist_ok=True)
        with open(nfl_json_path, "w") as f:
            json.dump(nfl_json, f)
    else:
        with open(nfl_json_path, "r") as f:
            nfl_json = json.load(f)

    return nfl_json
