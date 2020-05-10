from utils.logger import Logger
from bs4 import BeautifulSoup
import requests
import json
import os

LOGGER = Logger("main")


@LOGGER
def load_json(url, filepath, reinit=False):
    logger = LOGGER.get_logger(load_json.__name__)
    if not os.path.isfile(filepath) or reinit:
        logger.debug("(-) Cache miss!")
        r = requests.get(
            url=url,
            timeout=10,
            allow_redirects=False
        )
        soup = BeautifulSoup(r.text, "lxml")
        for tag in soup.findAll("script"):
            if "__espnfitt__" in str(tag):
                partial_json = "=".join(str(tag).split("=")[2:])
                json_data = partial_json.replace(";</script>", "")
                dirpath = "/".join(filepath.split("/")[:-1])
                os.makedirs(dirpath, exist_ok=True)
                with open(filepath, "w") as f:
                    f.write(json_data)
                json_dict = json.loads(json_data)
                break
        else:
            raise Exception(f"JSON not found: {url}")
    else:
        logger.debug("(+) Cache hit!")
        with open(filepath, "r") as f:
            json_dict = json.load(f)
    return json_dict


def process_team_index():
    url = "https://www.espn.com/nfl/teams"
    filepath = "cache/json/nfl/teams/index.json"

    json_dict = load_json(url, filepath)

    json_dict = json_dict.get("page")
    json_dict = json_dict.get("content")
    json_dict = json_dict.get("leagueTeams")

    groups = {}
    for column in json_dict.get("columns"):
        for group in column.get("groups"):
            div_reg = group.get("nm")

            teams = []
            for tm in group.get("tms"):
                team_name = tm.get("n")
                team_logo = tm.get("p")
                team_id = tm.get("id")

                links = {}
                for lk in tm.get("lk"):
                    title = lk.get("l")
                    if title == "Tickets":
                        continue
                    url = lk.get("u")
                    links[title] = url

                team = {
                    "id": team_id,
                    "name": team_name,
                    "logo": team_logo,
                    "links": links
                }
                teams.append(team)

            groups[div_reg] = teams

    return groups


def main():
    groups = process_team_index()
    print(json.dumps(groups))


if __name__ == "__main__":
    main()
