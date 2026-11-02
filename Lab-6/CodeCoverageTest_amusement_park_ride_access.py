"""Unit tests targeting comprehensive Code (Line) Coverage for amusement_park_ride_access.py.

This test suite executes every statement across both functions to exceed the
required 90% code coverage threshold, reaching 100% line coverage.
"""

import pytest
from amusement_park_ride_access import (
    process_ride_admissions,
    inspect_safety_restraints,
)


def test_single_adult_family_ride():
    """Initial baseline test: single adult on open family ride."""
    groups = [
        {
            "is_open": True,
            "ride_type": "family",
            "has_fast_lane": False,
            "patrons": [
                {"height_cm": 150, "health_warning": False, "is_child": False}
            ],
        }
    ]
    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 10.0
    assert result["status"] == "COMPLETED"


def test_invalid_groups_list():
    """Validates ValueError when groups is not a list."""
    with pytest.raises(ValueError, match="Invalid groups list or pass fee"):
        process_ride_admissions("not_a_list", 5.0)


def test_invalid_negative_express_pass_fee():
    """Validates ValueError when express_pass_fee is negative."""
    with pytest.raises(ValueError, match="Invalid groups list or pass fee"):
        process_ride_admissions([], -2.5)


def test_closed_ride_skipped():
    """Verifies that closed rides are skipped and generate no revenue."""
    groups = [
        {
            "is_open": False,
            "ride_type": "family",
            "patrons": [{"height_cm": 150}],
        }
    ]
    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 0.0
    assert result["status"] == "ZERO_ADMISSIONS"


def test_roller_coaster_adult():
    """Tests adult admission on roller coaster ($25 base ticket)."""
    groups = [
        {
            "is_open": True,
            "ride_type": "roller_coaster",
            "patrons": [{"height_cm": 160, "is_child": False}],
        }
    ]
    result = process_ride_admissions(groups, 0.0)
    assert result["total_revenue"] == 25.0
    assert result["status"] == "COMPLETED"


def test_water_ride_child():
    """Tests child admission on water ride ($18 * 0.60 = $10.80)."""
    groups = [
        {
            "is_open": True,
            "ride_type": "water_ride",
            "patrons": [{"height_cm": 130, "is_child": True}],
        }
    ]
    result = process_ride_admissions(groups, 0.0)
    assert result["total_revenue"] == 10.80
    assert result["status"] == "COMPLETED"


def test_unknown_ride_type_rejected():
    """Tests that unknown ride types reject patrons and skip group."""
    groups = [
        {
            "is_open": True,
            "ride_type": "haunted_mansion",
            "patrons": [{"height_cm": 150}],
        }
    ]
    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 0.0
    assert result["status"] == "ZERO_ADMISSIONS"


def test_invalid_patron_height():
    """Tests that non-positive height is rejected."""
    groups = [
        {
            "is_open": True,
            "ride_type": "family",
            "patrons": [{"height_cm": 0}],
        }
    ]
    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 0.0
    assert result["status"] == "ZERO_ADMISSIONS"


def test_health_warning_water_ride():
    """Tests health warning on water ride: patron rejected, group continues."""
    groups = [
        {
            "is_open": True,
            "ride_type": "water_ride",
            "patrons": [
                {"height_cm": 140, "health_warning": True},
                {"height_cm": 140, "health_warning": False, "is_child": False},
            ],
        }
    ]
    result = process_ride_admissions(groups, 0.0)
    assert result["total_revenue"] == 18.0
    assert result["status"] == "COMPLETED"


def test_health_warning_roller_coaster_break():
    """Tests health warning on roller coaster: group total resets and breaks."""
    groups = [
        {
            "is_open": True,
            "ride_type": "roller_coaster",
            "patrons": [
                {"height_cm": 160, "health_warning": False},
                {"height_cm": 150, "health_warning": True},
            ],
        }
    ]
    result = process_ride_admissions(groups, 0.0)
    assert result["total_revenue"] == 0.0
    assert result["status"] == "ZERO_ADMISSIONS"


def test_under_height_patron_rejected():
    """Tests patron under 120cm height restriction."""
    groups = [
        {
            "is_open": True,
            "ride_type": "family",
            "patrons": [{"height_cm": 110}],
        }
    ]
    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 0.0
    assert result["status"] == "ZERO_ADMISSIONS"


def test_fast_lane_express_pass():
    """Tests group with fast lane pass added to group total."""
    groups = [
        {
            "is_open": True,
            "ride_type": "family",
            "has_fast_lane": True,
            "patrons": [{"height_cm": 150, "is_child": False}],
        }
    ]
    result = process_ride_admissions(groups, 15.0)
    assert result["total_revenue"] == 25.0
    assert result["status"] == "COMPLETED"


def test_safety_audit_triggered():
    """Tests triggering SAFETY_AUDIT status when rejected_patrons > 4."""
    groups = [
        {
            "is_open": True,
            "ride_type": "family",
            "patrons": [
                {"height_cm": 100},  # rejected 1
                {"height_cm": 90},   # rejected 2
                {"height_cm": 80},   # rejected 3
                {"height_cm": 70},   # rejected 4
                {"height_cm": 60},   # rejected 5
                {"height_cm": 150, "is_child": False},  # accepted $10
            ],
        }
    ]
    result = process_ride_admissions(groups, 0.0)
    assert result["total_revenue"] == 10.0
    assert result["status"] == "SAFETY_AUDIT"


def test_inspect_safety_restraints_no_data():
    """Tests inspect_safety_restraints with empty or null streams."""
    assert inspect_safety_restraints([]) == "NO_DATA"
    assert inspect_safety_restraints(None) == "NO_DATA"


def test_inspect_safety_restraints_safe():
    """Tests inspect_safety_restraints when all streams are safe."""
    streams = [
        [1, 1, 1, 1],
        [1, 0, 1, 0, 1],
    ]
    assert inspect_safety_restraints(streams) == "SAFE"


def test_inspect_safety_restraints_emergency_lock():
    """Tests inspect_safety_restraints triggering EMERGENCY_LOCK (streak >= 2)."""
    streams = [
        [1, 1, 0, 0, 1],
    ]
    assert inspect_safety_restraints(streams) == "EMERGENCY_LOCK"
