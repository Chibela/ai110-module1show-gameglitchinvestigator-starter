from app import check_guess

# Bug 1: Backward hint messaging
# When guess > secret, message said "Go HIGHER!" instead of "Go LOWER!",
# and when guess < secret, message said "Go LOWER!" instead of "Go HIGHER!".

def test_too_high_message_tells_player_to_go_lower():
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in message but got: '{message}'"

def test_too_low_message_tells_player_to_go_higher():
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in message but got: '{message}'"

# Bug 1 (continued): Backward messages also affected the TypeError fallback path.
# On even attempts the secret is cast to a string, forcing int-vs-str comparison
# into the except block — which had the same swapped messages.

def test_too_high_message_correct_when_secret_is_string():
    # Simulates an even-attempt where secret was converted to str
    outcome, message = check_guess(80, "50")
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in message but got: '{message}'"

def test_too_low_message_correct_when_secret_is_string():
    outcome, message = check_guess(13, "20")
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in message but got: '{message}'"
