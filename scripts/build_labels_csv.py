"""Combine the batch annotation JSON files in labels/ into one CSV.

One row per image. The annotations column holds a JSON list of boxes:
{"type", "x", "y", "width", "height", "id"}, in pixels. An empty list means
the image was reviewed and has no crabs.

Usage: python scripts/build_labels_csv.py
"""
import csv
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LABELS_DIR = os.path.join(ROOT, "labels")
OUT_PATH = os.path.join(ROOT, "crab_labels.csv")


def batch_number(path):
    return int(re.search(r"Batch(\d+)_", os.path.basename(path)).group(1))


def main():
    rows = []
    for path in sorted(glob.glob(os.path.join(LABELS_DIR, "*.json")), key=batch_number):
        with open(path) as f:
            batch = json.load(f)
        for filename, entry in batch["data"].items():
            # Filenames look like 119586.jpg or 119586_b.jpg: number = submission ID.
            submission_id = re.match(r"(\d+)", filename).group(1)
            rows.append({
                "Submission ID": submission_id,
                "Image Filename": filename,
                "ImageURL": "",  # filled in later from a submission -> URL lookup
                "annotations": json.dumps(entry["annotations"], separators=(",", ":")),
                "Source File": os.path.basename(path),
            })

    with open(OUT_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUT_PATH}")


if __name__ == "__main__":
    main()
