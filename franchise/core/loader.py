from division import Division
from region import Region
from position import Position
from category import Category
from team import Team
import argparse
import json
import os


def build_fixtures():
    objects = {
        "division": list(Division()),
        "region": list(Region()),
        "position": list(Position()),
        "category": list(Category()),
        "team": list(Team())
    }

    fixtures = []
    for key, value in objects.items():
        filename = f"core/cache/fixtures/{key}.json"
        filedir = "/".join(filename.split("/")[:-1])
        os.makedirs(filedir, exist_ok=True)
        with open(filename, "w") as f:
            json.dump(value, f)
        fixtures += value

    return fixtures


def main(args):
    fixtures = build_fixtures()
    if args.outfile:
        with open(args.outfile, "w") as f:
            json.dump(fixtures, f)
    else:
        print(json.dumps(fixtures))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-o", "--outfile", metavar="outfile",
        type=str, required=False, default=None,
        help="specify output filename to write fixtures to"
    )
    args = parser.parse_args()
    main(args)
