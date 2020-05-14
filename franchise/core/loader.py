from objects.division import Division
from objects.position import Position
from objects.category import Category
from objects.team import Team
from objects.record import Record
from objects.profile import Profile
from objects.color import Color
from objects.teamnav import TeamNav
from indie.fetch_logos import fetch_logos
import json
import os


def build_fixtures():
    cache_dir = __file__.replace("loader.py", "cache")

    obj_map = {
        "division": list(Division()),
        "position": list(Position()),
        "category": list(Category()),
        "team": list(Team()),
        "record": list(Record()),
        "profile": list(Profile()),
        "color": list(Color()),
        "teamnav": list(TeamNav())
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
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--get-logos", dest="logos",
        action="store_true", required=False,
        help="specify the output directory for writing team logos"
    )
    args = parser.parse_args()
    if args.logos:
        logo_path = "../app/static/app/logos/"
        outdir = __file__.replace("loader.py", logo_path)
        fetch_logos(outdir=outdir)
    else:
        build_fixtures()
