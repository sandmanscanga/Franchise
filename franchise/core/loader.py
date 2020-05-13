from division import Division
from region import Region
from position import Position
from category import Category
import json


def gen_fixtures():
    objects = (
        Division(),
        Region(),
        Position(),
        Category()
    )
    for obj in objects:
        for fixture in obj:
            yield fixture


def main():
    print(json.dumps(list(gen_fixtures())))


if __name__ == "__main__":
    main()
