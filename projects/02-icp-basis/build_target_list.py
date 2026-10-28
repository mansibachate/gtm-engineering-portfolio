"""Turn the raw firm ranking into a target account list for Basis.

Reads data/ipa-top-150-2026.csv, applies the ICP rules below, and writes
data/target-accounts.csv with a status and a reason for every firm.

Run it from this folder:  python3 build_target_list.py
"""

import csv
from pathlib import Path

HERE = Path(__file__).parent
RAW_FILE = HERE / "data" / "ipa-top-150-2026.csv"
OUT_FILE = HERE / "data" / "target-accounts.csv"

# Rule 1: the Big 4 build their own AI and buy through long procurement.
BIG_4 = {"Deloitte", "PwC", "Ernst & Young LLP", "KPMG"}

# Rule 2: firms on Basis's customer logo wall are already customers.
# Names are matched by their first word(s), because rankings and logos
# spell firm names differently ("Wiss" vs. "Wiss & Company LLP").
BASIS_CUSTOMERS = [
    "Baker Tilly", "CohnReznick", "Wiss", "Citrin Cooperman", "Sikich",
    "UHY", "Schneider Downs", "Kaufman Rossin", "Berkowitz Pollack Brant",
    "Lutz", "Anders", "Rea", "Clark Nuber", "Boulay", "MarksNelson",
    "REDW", "Larson Gross", "Trout", "Olsen Thielen", "Pinion",
]

# Rule 3: the sweet spot. Firms above $600M revenue behave like
# enterprises (long cycles, in-house AI teams), so they're tier 2.
MAX_REVENUE_TIER_1 = 600_000_000

# Rule 4: specialist firms that don't do the typical tax + CAS work.
# Not removed, but flagged so a human checks them first.
SPECIALISTS = {
    "Kearney & Company PC": "government audit specialist",
    "Schellman": "cybersecurity compliance audits",
    "Global Tax Management Inc.": "outsourced tax compliance",
    "Cain Watters & Associates LLC": "dental practice planning",
}


def is_basis_customer(firm):
    # "Rea" would also match "Reaves", so require a whole-word match.
    words = firm.replace(",", " ").split()
    for customer in BASIS_CUSTOMERS:
        customer_words = customer.split()
        if words[: len(customer_words)] == customer_words:
            return True
    return False


def classify(row):
    """Return (status, reason) for one firm."""
    firm = row["firm"]
    revenue = int(row["net_revenue_usd"])

    if firm in BIG_4:
        return "remove", "Big 4"
    if is_basis_customer(firm):
        return "remove", "already a Basis customer"
    if firm in SPECIALISTS:
        return "check", SPECIALISTS[firm]
    if revenue > MAX_REVENUE_TIER_1:
        return "tier 2", "very large firm: enterprise-style sale"
    return "tier 1", "in the sweet spot"


def main():
    with RAW_FILE.open() as f:
        firms = list(csv.DictReader(f))

    counts = {}
    for row in firms:
        row["status"], row["reason"] = classify(row)
        counts[row["status"]] = counts.get(row["status"], 0) + 1

    with OUT_FILE.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(firms[0].keys()))
        writer.writeheader()
        writer.writerows(firms)

    print(f"Read {len(firms)} firms from {RAW_FILE.name}")
    for status in ["tier 1", "tier 2", "check", "remove"]:
        print(f"  {status:7} {counts.get(status, 0)}")
    print(f"Wrote {OUT_FILE.name}")


if __name__ == "__main__":
    main()
