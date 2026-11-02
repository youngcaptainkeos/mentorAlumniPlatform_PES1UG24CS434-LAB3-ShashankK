"""Comprehensive test suite for amusement_park_ride_access.py.

Includes test cases achieving 100% Line (Statement) Coverage and 100% Branch Coverage.
Also imports and re-exports the test suites from CodeCoverageTest and BranchCoverageTest.
"""

import pytest
from amusement_park_ride_access import (
    process_ride_admissions,
    inspect_safety_restraints,
)

# Re-export classes and functions from specific deliverable test files
from CodeCoverageTest_amusement_park_ride_access import *  # noqa: F401, F403
from BranchCoverageTest_amusement_park_ride_access import (  # noqa: F401
    TestProcessRideAdmissionsValidation,
    TestProcessRideAdmissionsRideTypes,
    TestPatronEligibilityAndHealthBranches,
    TestFastLaneAndOverallStatusBranches,
    TestInspectSafetyRestraintsBranches,
)