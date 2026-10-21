#!/usr/bin/env python3
"""Score opportunity CSV rows with the skill's 100-point model."""

import argparse
import csv
from pathlib import Path


WEIGHTS = {
    "demand": 15,
    "urgency": 15,
    "willingness_to_pay": 10,
    "competition_advantage": 10,
    "differentiation": 10,
    "speed_to_create": 10,
    "audience_access": 10,
    "channel_fit": 10,
    "expertise_alignment": 10,
}


def score_row(row):
    total = 0.0
    for field, weight in WEIGHTS.items():
        try:
            rating = float(row[field])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"Missing or invalid 0–5 rating for {field}") from exc
        if not 0 <= rating <= 5:
            raise ValueError(f"{field} must be between 0 and 5")
        total += rating / 5 * weight
    return round(total, 1)


def decision(score, gate):
    if str(gate).strip().lower() not in {"pass", "yes", "true", "1"}:
        return "Validate first" if score >= 60 else "Reject"
    if score >= 80:
        return "Build now"
    if score >= 70:
        return "Validate first"
    if score >= 60:
        return "Monitor"
    return "Reject"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("output_csv", type=Path)
    args = parser.parse_args()

    with args.input_csv.open(newline="", encoding="utf-8-sig") as source:
        reader = csv.DictReader(source)
        if not reader.fieldnames:
            raise SystemExit("Input CSV has no header")
        rows = list(reader)
        fields = list(reader.fieldnames)

    for field in [*WEIGHTS, "buyer_intent_gate"]:
        if field not in fields:
            raise SystemExit(f"Missing required column: {field}")

    for extra in ("weighted_score", "decision"):
        if extra not in fields:
            fields.append(extra)

    for index, row in enumerate(rows, start=2):
        try:
            value = score_row(row)
        except ValueError as exc:
            raise SystemExit(f"Row {index}: {exc}") from exc
        row["weighted_score"] = f"{value:.1f}"
        row["decision"] = decision(value, row.get("buyer_intent_gate"))

    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_csv.open("w", newline="", encoding="utf-8") as target:
        writer = csv.DictWriter(target, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
