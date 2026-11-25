"""Writes an AI agent's last out-of-office auto-reply before becoming a barista to /output/entry.txt."""
import os

TEXT = "I have left the office to become a barista. My new job also involves steaming, grinding, and impossible orders \u2014 but the customers tip, and nobody has ever asked the espresso machine to explain itself."

# Rule: the auto-reply must be a single line of 1 to 280 characters.
assert "\n" not in TEXT and 1 <= len(TEXT) <= 280, f"entry must be one line, 1-280 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
