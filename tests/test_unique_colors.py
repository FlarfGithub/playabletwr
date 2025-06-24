import re
import sys
from pathlib import Path


def main():
    colors_path = Path(__file__).resolve().parents[1] / "common" / "countries" / "colors.txt"
    tag_regex = re.compile(r"^([A-Z0-9]{3})\s*=\s*\{")
    counts = {}

    with colors_path.open(encoding="utf-8") as f:
        for line in f:
            match = tag_regex.match(line)
            if match:
                tag = match.group(1)
                counts[tag] = counts.get(tag, 0) + 1

    duplicates = {tag: count for tag, count in counts.items() if count > 1}
    if duplicates:
        for tag, count in duplicates.items():
            print(f"Duplicate tag {tag} found {count} times", file=sys.stderr)
        sys.exit(1)
    print("No duplicates found")


if __name__ == "__main__":
    main()
