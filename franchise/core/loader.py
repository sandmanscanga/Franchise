from framework.driver import get_nfl_json
from objects.division import Division
from objects.position import Position
from objects.category import Category
from objects.team import Team
import json
import os


def build_fixtures():
    cache_dir = __file__.replace("loader.py", "cache")

    obj_map = {
        "division": list(Division()),
        "position": list(Position()),
        "category": list(Category()),
        "team": list(Team())
    }

    fixture_dir = f"{cache_dir}/fixtures"
    os.makedirs(fixture_dir, exist_ok=True)

    fixtures = []
    for key, value in obj_map.items():
        filename = f"{fixture_dir}/{key}.json"
        with open(filename, "w") as f:
            json.dump(value, f)
        fixtures += value

    with open(f"{fixture_dir}/all.json", "w") as f:
        json.dump(fixtures, f)


if __name__ == "__main__":
    build_fixtures()
