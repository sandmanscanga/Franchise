from framework.driver import get_nfl_json
import argparse
import os


def main(args):
    outdir = args.outdir.rstrip("/")
    os.makedirs(outdir, exist_ok=True)

    nfl_json = get_nfl_json()
    for team_json in nfl_json.values():
        json_data = team_json.get("stats")
        json_data = json_data.get("page").get("content")
        json_data = json_data.get("stats").get("team")

        logo_url = json_data.get("logo")
        abbrev = json_data.get("abbrev")
        outpath = f"{outdir}/{abbrev}.png"

        cmd = f"wget {logo_url} -O {outpath} -q"
        print(f"GET {logo_url}")
        os.system(cmd)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-o", "--outdir", metavar="outdir",
        type=str, required=False, default="logos",
        help="specify the directory to write logos to"
    )
    args = parser.parse_args()
    main(args)
