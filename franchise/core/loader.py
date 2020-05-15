from objects.division import Division
from objects.position import Position
from objects.category import Category
from objects.team import Team
from objects.record import Record
from objects.profile import Profile
from objects.color import Color
from objects.teamnav import TeamNav
from objects.player import Player
from objects.playernav import PlayerNav
from objects.stat import Stat
from objects.teamstat import TeamStat
from objects.oppstat import OppStat
from indie.fetch_logos import fetch_logos
from indie.fetch_headshots import fetch_headshots
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
        "teamnav": list(TeamNav()),
        "player": list(Player()),
        "playernav": list(PlayerNav()),
        "stat": list(Stat()),
        "teamstat": list(TeamStat()),
        "oppstat": list(OppStat())
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
    parser.add_argument(
        "--get-headshots", dest="headshots",
        action="store_true", required=False,
        help="specify the output directory for writing player headshots"
    )
    parser.add_argument(
        "-r", "--reload", dest="reload",
        action="store_true", required=False,
        help="specify the reload command to load fixtures into project database"
    )
    parser.add_argument(
        "-w", "--wipe", dest="wipe",
        action="store_true", required=False,
        help="specify the wipe command to wipe all records from project database"
    )
    parser.add_argument(
        "-b", "--build", dest="build",
        action="store_true", required=False,
        help="specify the build command to build the fixtures from core objects"
    )
    args = parser.parse_args()
    if args.logos:
        outdir = __file__.replace("loader.py", "../app/static/app/logos/")
        fetch_logos(outdir=outdir)
    elif args.headshots:
        outdir = __file__.replace("loader.py", "../app/static/app/headshots/")
        fetch_headshots(outdir)
    elif args.wipe:
        print("[!] Wiping the project database records.")
        wipe_command = __file__.replace("loader.py", "utils/wipe.sh")
        os.system(wipe_command)
    elif args.reload:
        reload_command = __file__.replace("loader.py", "utils/reload.sh")
        os.system(reload_command)
    elif args.build:
        build_fixtures()
    else:
        parser.print_help()
