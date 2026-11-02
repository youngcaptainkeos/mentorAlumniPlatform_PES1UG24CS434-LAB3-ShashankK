"""Unit tests targeting exhaustive Branch Coverage for amusement_park_ride_access.py.

This test suite methodically verifies every decision point, boolean branch condition,
and boundary threshold to achieve 100% Branch Coverage and 100% Statement Coverage.
"""

import pytest
from amusement_park_ride_access import (
    process_ride_admissions,
    inspect_safety_restraints,
)


class TestProcessRideAdmissionsValidation:
    """Test suite for initial argument validation branch in process_ride_admissions."""

    def test_invalid_groups_non_list_types(self):
        """Branch: not isinstance(groups, list) evaluates to True."""
        with pytest.raises(ValueError, match="Invalid groups list or pass fee"):
            process_ride_admissions("string_not_list", 10.0)

        with pytest.raises(ValueError, match="Invalid groups list or pass fee"):
            process_ride_admissions(None, 10.0)

        with pytest.raises(ValueError, match="Invalid groups list or pass fee"):
            process_ride_admissions({"key": "dict_not_list"}, 10.0)

    def test_invalid_negative_express_fee(self):
        """Branch: express_pass_fee < 0 evaluates to True."""
        with pytest.raises(ValueError, match="Invalid groups list or pass fee"):
            process_ride_admissions([], -0.01)

        with pytest.raises(ValueError, match="Invalid groups list or pass fee"):
            process_ride_admissions([], -50.0)

    def test_valid_empty_groups_zero_revenue(self):
        """Branch: valid list and non-negative fee, but groups is empty."""
        result = process_ride_admissions([], 10.0)
        assert result == {"total_revenue": 0.0, "status": "ZERO_ADMISSIONS"}


class TestProcessRideAdmissionsRideTypes:
    """Test suite covering ride_type classification branches and closed rides."""

    def test_ride_is_closed_branch(self):
        """Branch: not group.get('is_open', False) is True -> continue."""
        groups = [
            {
                "is_open": False,
                "ride_type": "roller_coaster",
                "patrons": [{"height_cm": 150}],
            },
            {
                # Missing 'is_open' key defaults to False
                "ride_type": "family",
                "patrons": [{"height_cm": 150}],
            },
        ]
        result = process_ride_admissions(groups, 5.0)
        assert result == {"total_revenue": 0.0, "status": "ZERO_ADMISSIONS"}

    def test_ride_type_roller_coaster_pricing(self):
        """Branch: ride_type == 'roller_coaster' -> base_ticket = 25.0."""
        groups = [
            {
                "is_open": True,
                "ride_type": "roller_coaster",
                "patrons": [{"height_cm": 160, "is_child": False}],
            }
        ]
        result = process_ride_admissions(groups, 0.0)
        assert result == {"total_revenue": 25.0, "status": "COMPLETED"}

    def test_ride_type_water_ride_pricing(self):
        """Branch: ride_type == 'water_ride' -> base_ticket = 18.0."""
        groups = [
            {
                "is_open": True,
                "ride_type": "water_ride",
                "patrons": [{"height_cm": 140, "is_child": False}],
            }
        ]
        result = process_ride_admissions(groups, 0.0)
        assert result == {"total_revenue": 18.0, "status": "COMPLETED"}

    def test_ride_type_family_pricing(self):
        """Branch: ride_type == 'family' -> base_ticket = 10.0."""
        groups = [
            {
                "is_open": True,
                "ride_type": "family",
                "patrons": [{"height_cm": 140, "is_child": False}],
            }
        ]
        result = process_ride_admissions(groups, 0.0)
        assert result == {"total_revenue": 10.0, "status": "COMPLETED"}

    def test_ride_type_default_fallback(self):
        """Branch: ride_type key omitted -> defaults to 'family'."""
        groups = [
            {
                "is_open": True,
                "patrons": [{"height_cm": 140, "is_child": False}],
            }
        ]
        result = process_ride_admissions(groups, 0.0)
        assert result == {"total_revenue": 10.0, "status": "COMPLETED"}

    def test_ride_type_invalid_rejected_branch(self):
        """Branch: unrecognized ride_type -> rejected_patrons += 1; continue."""
        groups = [
            {
                "is_open": True,
                "ride_type": "haunted_mansion",
                "patrons": [{"height_cm": 150}],
            }
        ]
        result = process_ride_admissions(groups, 5.0)
        assert result == {"total_revenue": 0.0, "status": "ZERO_ADMISSIONS"}


class TestPatronEligibilityAndHealthBranches:
    """Test suite covering patron attributes, health warnings, and height branches."""

    def test_patron_empty_patrons_list(self):
        """Branch: group with empty patrons list."""
        groups = [
            {
                "is_open": True,
                "ride_type": "family",
                "patrons": [],
            }
        ]
        result = process_ride_admissions(groups, 5.0)
        assert result == {"total_revenue": 0.0, "status": "ZERO_ADMISSIONS"}

    def test_patron_missing_or_zero_height(self):
        """Branch: height_cm <= 0 (height omitted or 0)."""
        groups = [
            {
                "is_open": True,
                "ride_type": "family",
                "patrons": [{"health_warning": False}],  # height defaults to 0
            }
        ]
        result = process_ride_admissions(groups, 5.0)
        assert result == {"total_revenue": 0.0, "status": "ZERO_ADMISSIONS"}

    def test_patron_negative_height(self):
        """Branch: height_cm <= 0 (negative height value)."""
        groups = [
            {
                "is_open": True,
                "ride_type": "family",
                "patrons": [{"height_cm": -20}],
            }
        ]
        result = process_ride_admissions(groups, 5.0)
        assert result == {"total_revenue": 0.0, "status": "ZERO_ADMISSIONS"}

    def test_health_warning_on_roller_coaster_breaks_group(self):
        """Branch: has_health_warning True on roller_coaster -> group_total = 0.0 and break."""
        groups = [
            {
                "is_open": True,
                "ride_type": "roller_coaster",
                "patrons": [
                    {"height_cm": 150, "health_warning": False, "is_child": False},
                    {"height_cm": 160, "health_warning": True},  # breaks loop
                    {"height_cm": 170, "health_warning": False},  # skipped by break
                ],
            }
        ]
        result = process_ride_admissions(groups, 0.0)
        assert result == {"total_revenue": 0.0, "status": "ZERO_ADMISSIONS"}

    def test_health_warning_on_non_roller_coaster_continues(self):
        """Branch: has_health_warning True on water_ride -> group_total += 0.0, no break."""
        groups = [
            {
                "is_open": True,
                "ride_type": "water_ride",
                "patrons": [
                    {"height_cm": 150, "health_warning": True},  # rejected, no break
                    {"height_cm": 140, "health_warning": False, "is_child": False},  # accepted $18
                ],
            }
        ]
        result = process_ride_admissions(groups, 0.0)
        assert result == {"total_revenue": 18.0, "status": "COMPLETED"}

    def test_patron_under_120cm_rejected(self):
        """Branch: height_cm < 120 (boundary check: 119cm)."""
        groups = [
            {
                "is_open": True,
                "ride_type": "family",
                "patrons": [{"height_cm": 119}],
            }
        ]
        result = process_ride_admissions(groups, 0.0)
        assert result == {"total_revenue": 0.0, "status": "ZERO_ADMISSIONS"}

    def test_patron_at_120cm_child_discount(self):
        """Branch: height_cm == 120, is_child is True -> base_ticket * 0.60."""
        groups = [
            {
                "is_open": True,
                "ride_type": "family",
                "patrons": [{"height_cm": 120, "is_child": True}],
            }
        ]
        result = process_ride_admissions(groups, 0.0)
        # 10.0 * 0.60 = 6.0
        assert result == {"total_revenue": 6.0, "status": "COMPLETED"}

    def test_patron_adult_full_ticket(self):
        """Branch: height_cm >= 120, is_child is False -> base_ticket."""
        groups = [
            {
                "is_open": True,
                "ride_type": "family",
                "patrons": [{"height_cm": 150, "is_child": False}],
            }
        ]
        result = process_ride_admissions(groups, 0.0)
        assert result == {"total_revenue": 10.0, "status": "COMPLETED"}


class TestFastLaneAndOverallStatusBranches:
    """Test suite covering fast_lane addition and final return status branches."""

    def test_fast_lane_applied_when_true(self):
        """Branch: group.get('has_fast_lane', False) is True."""
        groups = [
            {
                "is_open": True,
                "ride_type": "family",
                "has_fast_lane": True,
                "patrons": [{"height_cm": 140, "is_child": False}],
            }
        ]
        result = process_ride_admissions(groups, 12.50)
        assert result == {"total_revenue": 22.50, "status": "COMPLETED"}

    def test_fast_lane_omitted_when_false(self):
        """Branch: group.get('has_fast_lane', False) is False."""
        groups = [
            {
                "is_open": True,
                "ride_type": "family",
                "has_fast_lane": False,
                "patrons": [{"height_cm": 140, "is_child": False}],
            }
        ]
        result = process_ride_admissions(groups, 12.50)
        assert result == {"total_revenue": 10.0, "status": "COMPLETED"}

    def test_status_safety_audit_rejections_greater_than_four(self):
        """Branch: rejected_patrons > 4 -> status 'SAFETY_AUDIT'."""
        groups = [
            {
                "is_open": True,
                "ride_type": "family",
                "patrons": [
                    {"height_cm": 100},  # 1
                    {"height_cm": 100},  # 2
                    {"height_cm": 100},  # 3
                    {"height_cm": 100},  # 4
                    {"height_cm": 100},  # 5
                    {"height_cm": 140, "is_child": False},  # accepted
                ],
            }
        ]
        result = process_ride_admissions(groups, 0.0)
        assert result["status"] == "SAFETY_AUDIT"
        assert result["total_revenue"] == 10.0

    def test_status_completed_exact_four_rejections_boundary(self):
        """Branch: rejected_patrons == 4 (boundary: NOT > 4) and total_revenue > 0."""
        groups = [
            {
                "is_open": True,
                "ride_type": "family",
                "patrons": [
                    {"height_cm": 100},  # 1
                    {"height_cm": 100},  # 2
                    {"height_cm": 100},  # 3
                    {"height_cm": 100},  # 4
                    {"height_cm": 140, "is_child": False},  # accepted $10
                ],
            }
        ]
        result = process_ride_admissions(groups, 0.0)
        assert result["status"] == "COMPLETED"
        assert result["total_revenue"] == 10.0

    def test_status_zero_admissions_with_fewer_rejections(self):
        """Branch: rejected_patrons <= 4 and total_revenue == 0.0."""
        groups = [
            {
                "is_open": True,
                "ride_type": "family",
                "patrons": [
                    {"height_cm": 100},  # 1
                    {"height_cm": 100},  # 2
                ],
            }
        ]
        result = process_ride_admissions(groups, 0.0)
        assert result == {"total_revenue": 0.0, "status": "ZERO_ADMISSIONS"}


class TestInspectSafetyRestraintsBranches:
    """Test suite covering every decision branch in inspect_safety_restraints."""

    def test_restraint_streams_falsy_branches(self):
        """Branch: if not restraint_streams -> 'NO_DATA'."""
        assert inspect_safety_restraints([]) == "NO_DATA"
        assert inspect_safety_restraints(None) == "NO_DATA"
        assert inspect_safety_restraints(()) == "NO_DATA"

    def test_restraint_streams_empty_stream_element(self):
        """Branch: inner sensor_readings stream is empty."""
        assert inspect_safety_restraints([[]]) == "SAFE"

    def test_restraint_streams_all_latched_safe(self):
        """Branch: all sensor values are 1 (latched) -> 'SAFE'."""
        streams = [
            [1, 1, 1, 1],
            [1, 1],
        ]
        assert inspect_safety_restraints(streams) == "SAFE"

    def test_restraint_streams_isolated_unlatched_resets_streak(self):
        """Branch: sensor_val == 0 followed by sensor_val != 0 (streak reset)."""
        streams = [
            [0, 1, 0, 1, 0, 1],
            [1, 0, 1],
        ]
        assert inspect_safety_restraints(streams) == "SAFE"

    def test_restraint_streams_emergency_lock_streak_reaches_two(self):
        """Branch: unlatched_streak reaches >= 2 -> 'EMERGENCY_LOCK'."""
        streams = [
            [1, 0, 0, 1],
        ]
        assert inspect_safety_restraints(streams) == "EMERGENCY_LOCK"

    def test_restraint_streams_emergency_lock_in_secondary_stream(self):
        """Branch: first stream is safe, second stream triggers EMERGENCY_LOCK."""
        streams = [
            [1, 1, 1],
            [0, 0],
        ]
        assert inspect_safety_restraints(streams) == "EMERGENCY_LOCK"
