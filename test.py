import pytest
from parse_commit_message import parse_commit_message

@pytest.mark.parametrize("input_str, expected", [
    # Standard case
    ("[release-1.2.3] EEV2-1234", ("EEV2-1234", "release-1.2.3")),

    # Lowercase, extra spaces, and missing dash
    ("release 1.2.3 eev2 1234", ("EEV2-1234", "release-1.2.3")),

    # Missing one E
    ("[release-1.2.3] EV2-1234", ("EEV2-1234", "release-1.2.3")),

    # Three Es
    ("release-1.2.3 EEEV2-1234", ("EEV2-1234", "release-1.2.3")),

    # No dash in ticket
    ("release-1.2.3 eev21234", ("EEV2-1234", "release-1.2.3")),

    # Missing V
    ("release-1.2.3 ee2 1234", ("EEV2-1234", "release-1.2.3")),

    # Extra V
    ("release-1.2.3 eevv2-1234", ("EEV2-1234", "release-1.2.3")),

    # Weird spacing
    ("release   -   1.2.3   E E V 2   -   1234", ("EEV2-1234", "release-1.2.3")),

    # release without dash
    ("release1.2.3 eev2-1234", ("EEV2-1234", "release-1.2.3")),

    # Ticket before release
    ("eev2 1234 release 1.2.3", ("EEV2-1234", "release-1.2.3")),

    # Capitalized Release
    ("Release-1.2.3 EEv2 1234", ("EEV2-1234", "release-1.2.3")),
])

def test_rebuild_ticket_nbr(input_str, expected):
    assert parse_commit_message(input_str) == expected