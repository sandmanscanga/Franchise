from division import Division
from region import Region
from position import Position
from category import Category
from team import Team
import json
import os


def build_fixtures():
    fixture_dir = "core/cache/fixtures"
    os.makedirs(fixture_dir, exist_ok=True)

    objects = {
        "division": list(Division()),
        "region": list(Region()),
        "position": list(Position()),
        "category": list(Category()),
        "team": list(Team())
    }

    fixtures = []
    for key, value in objects.items():
        filename = f"{fixture_dir}/{key}.json"
        with open(filename, "w") as f:
            json.dump(value, f)
        fixtures += value

    with open(f"{fixture_dir}/all.json", "w") as f:
        json.dump(fixtures, f)


if __name__ == "__main__":
    build_fixtures()
