import pytest
from rebuild_ticket_nbr_test import rebuild_ticket_nbr

@pytest.mark.parametrize("input_str, expected", [
    ("fix eev2 1234", "EEV2-1234"),
    ("Fix EeV2-1234", "EEV2-1234"),
    ("fix E2 1234 and EEV2 5678", "EEV2-1234"),
    ("this fixes EV2 3210 as discussed", "EEV2-3210"),
    ("patch\nEE2 1111", "EEV2-1111"),
    ("bugfix    EV2-2022", "EEV2-2022"),
    ("fix applied to EEV2 9876", "EEV2-9876"),
])
def test_rebuild_ticket_nbr(input_str, expected):
    assert rebuild_ticket_nbr(input_str) == expected
