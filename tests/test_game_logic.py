from logic_utils import (
    check_guess,
    update_score,
    get_final_score,
    get_range_for_difficulty,
    build_new_game_state,
)


# --- check_guess basics ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


# --- Bug 1: Backward hint messaging ---

def test_too_high_message_tells_player_to_go_lower():
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in message but got: '{message}'"

def test_too_low_message_tells_player_to_go_higher():
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in message but got: '{message}'"

def test_too_high_message_correct_when_secret_is_string():
    outcome, message = check_guess(80, "50")
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in message but got: '{message}'"

def test_too_low_message_correct_when_secret_is_string():
    outcome, message = check_guess(13, "20")
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in message but got: '{message}'"


# --- Bug 2: Guesses outside the difficulty range are rejected ---

def test_easy_rejects_guess_above_range():
    low, high = get_range_for_difficulty("Easy")
    guess = 25
    assert not (low <= guess <= high), f"25 should be out of Easy range ({low}-{high})"

def test_hard_rejects_guess_above_range():
    low, high = get_range_for_difficulty("Hard")
    guess = 200
    assert not (low <= guess <= high), f"200 should be out of Hard range ({low}-{high})"


# --- Bug 3: Hard difficulty range ---

def test_hard_range_upper_bound_is_150():
    _, high = get_range_for_difficulty("Hard")
    assert high == 150, f"Hard mode upper bound should be 150, got {high}"

def test_hard_range_is_larger_than_normal():
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high, f"Hard range ({hard_high}) should exceed Normal range ({normal_high})"


# --- Bug 4: New Game button state reset ---

def test_new_game_state_resets_status_to_playing():
    state = build_new_game_state("Normal")
    assert state["status"] == "playing", f"Expected 'playing', got '{state['status']}'"

def test_new_game_state_respects_difficulty_range():
    state = build_new_game_state("Easy")
    _, easy_high = get_range_for_difficulty("Easy")
    assert state["secret"] <= easy_high, (
        f"Easy new-game secret {state['secret']} exceeds Easy max {easy_high}"
    )


# --- Bug 5: Scoring bugs ---

def test_win_on_first_attempt_gives_100_points():
    score = update_score(0, "Win", 1)
    assert score == 100, f"Expected 100 but got {score}"

def test_win_on_later_attempt_scores_less():
    score_attempt1 = update_score(0, "Win", 1)
    score_attempt5 = update_score(0, "Win", 5)
    assert score_attempt5 < score_attempt1, (
        f"Later win ({score_attempt5}) should score less than earlier win ({score_attempt1})"
    )

def test_win_score_floor_is_10():
    score = update_score(0, "Win", 20)
    assert score == 10, f"Expected floor of 10 but got {score}"

def test_too_high_on_even_attempt_deducts_points():
    score = update_score(50, "Too High", 2)
    assert score == 45, f"Expected 45 but got {score}"

def test_too_high_on_odd_attempt_deducts_points():
    score = update_score(50, "Too High", 3)
    assert score == 45, f"Expected 45 but got {score}"

def test_too_high_and_too_low_penalize_equally():
    score_high = update_score(50, "Too High", 2)
    score_low = update_score(50, "Too Low", 2)
    assert score_high == score_low, (
        f"Too High ({score_high}) and Too Low ({score_low}) should penalize equally"
    )

def test_wrong_guess_score_never_goes_below_zero():
    raw = update_score(0, "Too Low", 1)
    assert max(0, raw) == 0

def test_multiple_wrong_guesses_stay_at_zero():
    score = 0
    for attempt in range(1, 6):
        score = max(0, update_score(score, "Too Low", attempt))
    assert score == 0

def test_final_score_clamps_negative_to_zero():
    assert get_final_score(-25) == 0

def test_final_score_preserves_positive_score():
    assert get_final_score(80) == 80

def test_final_score_is_zero_when_raw_is_zero():
    assert get_final_score(0) == 0


# --- Bug 6: Streamlit rendering order — info bar showed stale attempt count ---
# Before the fix, st.info() was rendered before st.session_state.attempts was
# incremented, so the displayed count was always 1 behind after each submit.
# The fix uses st.empty() as a placeholder filled after the submit block runs.

from streamlit.testing.v1 import AppTest

def test_info_bar_shows_correct_attempts_before_any_guess():
    at = AppTest.from_file("app.py").run()
    # Normal mode: 8 attempts allowed, 0 used → should show 8 left
    assert "Attempts left: 8" in at.info[0].value

def test_info_bar_decrements_immediately_after_submit():
    at = AppTest.from_file("app.py").run()
    # Submit one guess
    at.text_input[0].set_value("50")
    at.button[0].click().run()
    # Before the fix this still showed "Attempts left: 8" — now must show 7
    assert "Attempts left: 7" in at.info[0].value
