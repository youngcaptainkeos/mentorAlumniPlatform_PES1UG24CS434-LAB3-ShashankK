"""Module for theme park rider admission, throughput, and safety restraint resolution.

Hardened with defensive input validation against malformed, unexpected,
or adversarial edge-case inputs identified via Hypothesis fuzz testing.
"""

import math
from typing import Optional


def validate_height_and_fastpass(rider_spec: Optional[str]) -> str:
    """Validate rider height and fastpass specification.

    Expected format: "Height:FastPass" (e.g. "140:YES" or "110:NO").

    Args:
        rider_spec: String containing height in cm and FastPass flag.

    Returns:
        Formatted approval/denial string or an informative validation message.
    """
    if not isinstance(rider_spec, str):
        return "Invalid rider specification: Input must be a valid string."

    trimmed = rider_spec.strip()
    if not trimmed or ":" not in trimmed:
        return "Invalid rider specification: Format must be 'Height:FastPass'."

    parts = trimmed.split(":")
    if len(parts) != 2:
        return "Invalid rider specification: Format must be 'Height:FastPass'."

    height_str, pass_str = parts[0].strip(), parts[1].strip()

    try:
        height = int(height_str)
    except (ValueError, TypeError):
        return f"Invalid height '{height_str}': Must be an integer."

    if height <= 0 or height > 300:
        return f"Invalid height '{height}cm': Must be between 1 and 300 cm."

    pass_map = {
        "YES": True,
        "Y": True,
        "TRUE": True,
        "NO": False,
        "N": False,
        "FALSE": False,
    }

    normalized_pass = pass_str.upper()
    if normalized_pass not in pass_map:
        return f"Invalid FastPass status '{pass_str}': Must be YES or NO."

    has_fastpass = pass_map[normalized_pass]
    eligible = height >= 120
    status = "FastPass Priority" if has_fastpass else "Standard Entry"
    return f"Height {height}cm: {'Approved' if eligible else 'Denied'} ({status})"


def compute_dispatch_throughput(ride_metric_str: Optional[str]) -> float:
    """Compute dispatch throughput rate in riders per minute.

    Expected format: "Riders/CycleMinutes" (e.g. "48/2.5").

    Args:
        ride_metric_str: String metric with riders count and cycle duration.

    Returns:
        Computed rate rounded to 2 decimal places, or 0.0 on invalid input.
    """
    if not isinstance(ride_metric_str, str):
        return 0.0

    trimmed = ride_metric_str.strip()
    if not trimmed or "/" not in trimmed:
        return 0.0

    parts = trimmed.split("/")
    if len(parts) != 2:
        return 0.0

    try:
        riders = float(parts[0].strip())
        cycle_mins = float(parts[1].strip())
    except (ValueError, TypeError):
        return 0.0

    # Guard against NaN, Inf, non-positive cycle minutes, or negative riders
    if (
        math.isnan(riders)
        or math.isnan(cycle_mins)
        or math.isinf(riders)
        or math.isinf(cycle_mins)
    ):
        return 0.0

    if cycle_mins <= 0.0 or riders < 0.0:
        return 0.0

    rate = riders / cycle_mins
    return round(rate, 2)


def resolve_safety_restraint_code(zone_code: Optional[str]) -> str:
    """Resolve ride zone code prefix to safety restraint description.

    Expected format starts with CST, WTR, DRP, or WHL (e.g. "CST_01", "WTR_A").

    Args:
        zone_code: Zone code string identifier.

    Returns:
        Description string of corresponding safety restraint mechanism.
    """
    if not isinstance(zone_code, str):
        return "Unknown Restraint (Invalid Zone Code)"

    trimmed = zone_code.strip().upper()
    if not trimmed:
        return "Unknown Restraint (Empty Zone Code)"

    prefix = trimmed[:3]
    restraint_types = {
        "CST": "Over-the-Shoulder Harness",
        "WTR": "Lap Bar and Seatbelt",
        "DRP": "Hydraulic Shoulder Vest",
        "WHL": "Manual Safety Bar",
    }
    return restraint_types.get(prefix, f"Unknown Restraint (Unrecognized Zone '{prefix}')")


def main():
    print("==== Running validate_height_and_fastpass ====")
    r_input = input("Enter rider spec (Height:FastPass, e.g. 140:YES): ")
    print(validate_height_and_fastpass(r_input))

    print("\n==== Running compute_dispatch_throughput ====")
    t_input = input("Enter riders/mins (e.g. 48/2.5): ")
    print("Throughput (riders/min):", compute_dispatch_throughput(t_input))

    print("\n==== Running resolve_safety_restraint_code ====")
    z_input = input("Enter ride zone code (e.g. CST_01, WTR_A): ")
    print("Restraint:", resolve_safety_restraint_code(z_input))


if __name__ == "__main__":
    main()