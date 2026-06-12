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

# Bug 2: Game rejects guesses outside the allowed difficulty range

def test_easy_rejects_guess_above_range():
    # Easy mode is 1–20; a guess of 25 should be outside the valid range
    from logic_utils import get_range_for_difficulty
    low, high = get_range_for_difficulty("Easy")
    guess = 25
    assert not (low <= guess <= high), f"25 should be out of Easy range ({low}–{high})"

def test_hard_rejects_guess_above_range():
    # Hard mode is 1–150; a guess of 200 should be outside the valid range
    from logic_utils import get_range_for_difficulty
    low, high = get_range_for_difficulty("Hard")
    guess = 200
    assert not (low <= guess <= high), f"200 should be out of Hard range ({low}–{high})"

# Bug 3: Hard difficulty range was smaller than Normal (1–50 vs 1–100), making it easier

def test_hard_range_upper_bound_is_150():
    # Hard mode should go up to 150, not 50
    from logic_utils import get_range_for_difficulty
    _, high = get_range_for_difficulty("Hard")
    assert high == 150, f"Hard mode upper bound should be 150, got {high}"

def test_hard_range_is_larger_than_normal():
    # Hard mode should have a wider range than Normal to be genuinely harder
    from logic_utils import get_range_for_difficulty
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high, f"Hard range ({hard_high}) should exceed Normal range ({normal_high})"
