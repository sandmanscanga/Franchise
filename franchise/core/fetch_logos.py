from framework.driver import get_nfl_json
import os


def fetch_logos(outdir):
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
        if os.path.isfile(outpath):
            print(f"[*] Skipping logo: {outpath}")
            continue

        cmd = f"wget {logo_url} -O {outpath} -q"
        print(f"[+] Getting logo: {logo_url}")
        os.system(cmd)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-o", "--outdir", metavar="outdir",
        type=str, required=False, default="../app/static/app/logos/",
        help="specify the directory to write logos to"
    )
    args = parser.parse_args()
    fetch_logos(args.outdir)
