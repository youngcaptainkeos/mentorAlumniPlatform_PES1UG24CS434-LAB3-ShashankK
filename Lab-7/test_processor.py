"""Property-based fuzz testing suite using Hypothesis for processor.py.

Tests robust error handling, edge cases, malformed strings, null inputs,
and boundary condition properties across all module functions.
"""

import math
from hypothesis import given, strategies as st
from processor import (
    validate_height_and_fastpass,
    compute_dispatch_throughput,
    resolve_safety_restraint_code,
)


# ==============================================================================
# Mandatory Handout Fuzz Tests: No-Crash Properties on Arbitrary Inputs / None
# ==============================================================================

@given(st.text() | st.none())
def test_validate_height_and_fastpass_no_crash(s):
    """Fuzz test: validate_height_and_fastpass must not crash on any string or None."""
    try:
        result = validate_height_and_fastpass(s)
        assert isinstance(result, str)
    except Exception as e:
        assert False, f"validate_height_and_fastpass crashed with: {e}"


@given(st.text() | st.none())
def test_compute_dispatch_throughput_safe(s):
    """Fuzz test: compute_dispatch_throughput must not crash on any string or None."""
    try:
        result = compute_dispatch_throughput(s)
        assert isinstance(result, float)
        assert not math.isnan(result)
        assert not math.isinf(result)
    except Exception as e:
        assert False, f"compute_dispatch_throughput crashed with: {e}"


@given(st.text() | st.none())
def test_resolve_safety_restraint_code_safe(s):
    """Fuzz test: resolve_safety_restraint_code must not crash on any string or None."""
    try:
        result = resolve_safety_restraint_code(s)
        assert isinstance(result, str)
    except Exception as e:
        assert False, f"resolve_safety_restraint_code crashed with: {e}"


# ==============================================================================
# Invariant & Domain Property Tests
# ==============================================================================

@given(
    height=st.integers(min_value=1, max_value=300),
    fastpass=st.sampled_from(["YES", "NO", "yes", "no", "True", "False"]),
)
def test_validate_height_and_fastpass_valid_inputs(height, fastpass):
    """Property test: Valid height and fastpass combinations must return formatted approval status."""
    spec = f"{height}:{fastpass}"
    result = validate_height_and_fastpass(spec)
    assert isinstance(result, str)
    if height >= 120:
        assert "Approved" in result
    else:
        assert "Denied" in result


@given(
    riders=st.floats(min_value=0.0, max_value=10000.0, allow_nan=False, allow_infinity=False),
    cycle_mins=st.floats(min_value=0.01, max_value=120.0, allow_nan=False, allow_infinity=False),
)
def test_compute_dispatch_throughput_positive_rates(riders, cycle_mins):
    """Property test: Positive riders and cycle duration must compute non-negative rate."""
    metric = f"{riders}/{cycle_mins}"
    rate = compute_dispatch_throughput(metric)
    assert rate >= 0.0
    expected = round(riders / cycle_mins, 2)
    assert abs(rate - expected) < 0.02


@given(
    zone_prefix=st.sampled_from(["CST", "WTR", "DRP", "WHL", "cst", "wtr", "drp", "whl"]),
    suffix=st.text(alphabet=st.characters(whitelist_categories=('Lu', 'Ll', 'Nd', 'Pc'))),
)
def test_resolve_safety_restraint_code_known_zones(zone_prefix, suffix):
    """Property test: Known zone prefixes must resolve to standard restraint descriptions."""
    code = f"{zone_prefix}_{suffix}"
    result = resolve_safety_restraint_code(code)
    assert any(
        kw in result
        for kw in ["Harness", "Lap Bar", "Vest", "Safety Bar"]
    )