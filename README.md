# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Game purpose:** A number-guessing game where the player picks a difficulty (Easy 1–20, Normal 1–100, Hard 1–150), then guesses the secret number within a limited number of attempts, earning points for correct guesses and losing points for wrong ones.
- [x] **Bugs found:**
  1. **Backward hints** — `check_guess` returned "Go HIGHER" when the guess was too high and "Go LOWER" when it was too low.
  2. **Difficulty change didn't reset state** — switching difficulty kept the old secret number and attempt count, so the new range was never applied properly.
  3. **New Game button didn't fully restart** — clicking New Game reset the state variables but Streamlit's top-down rendering meant the win/loss screen still appeared; the game wasn't truly restarted.
  4. **Stale info bar** — the info bar (attempts left, score) was placed before the submit logic, so it always showed the previous turn's values. Fixed by using `st.empty()` to reserve the slot at the top and writing to it after all logic ran, ensuring it always reflects the current state.
  5. **Wrong Hard difficulty range** — Hard mode used 1–50 instead of 1–150.
  6. **Out-of-range guesses accepted** — the app let players guess numbers outside the difficulty's valid range.
- [x] **Fixes applied:**
  1. Swapped the "Too High" / "Too Low" hint messages in `check_guess`.
  2. Added a difficulty-change check in `app.py` that resets the secret and attempts whenever the player switches modes.
  3. Added `st.rerun()` after the New Game button handler so Streamlit re-renders from a clean state.
  4. Replaced the inline `st.info()` with `info_bar = st.empty()` at the top and `info_bar.info(...)` at the bottom of the script, so the bar always shows up-to-date values.
  5. Updated `get_range_for_difficulty` to return `(1, 150)` for Hard.
  6. Added a range check in `app.py` before accepting a submitted guess.

## 📸 Demo Walkthrough

1. Launch the app with `python -m streamlit run app.py` and select a difficulty from the sidebar.
2. Open the "Developer Debug Info" expander to peek at the secret number (useful for testing).
3. Type a number in the input box and click **Submit Guess** — the info bar shows attempts remaining and your current score.
4. Follow the "Go HIGHER" / "Go LOWER" hints until you guess correctly.
5. Click **New Game** at any point (including after a win or loss) to reset and play again.

## 🧪 Test Results

```
pytest tests/
============================= test session starts =============================
platform win32 -- Python 3.13.13, pytest-9.0.3, pluggy-1.6.0
collected 24 items

tests/test_game_logic.py::test_winning_guess PASSED
tests/test_game_logic.py::test_too_high_message_tells_player_to_go_lower PASSED
tests/test_game_logic.py::test_too_low_message_tells_player_to_go_higher PASSED
tests/test_game_logic.py::test_too_high_message_correct_when_secret_is_string PASSED
tests/test_game_logic.py::test_too_low_message_correct_when_secret_is_string PASSED
tests/test_game_logic.py::test_easy_rejects_guess_above_range PASSED
tests/test_game_logic.py::test_hard_rejects_guess_above_range PASSED
tests/test_game_logic.py::test_hard_range_upper_bound_is_150 PASSED
tests/test_game_logic.py::test_hard_range_is_larger_than_normal PASSED
tests/test_game_logic.py::test_new_game_state_resets_status_to_playing PASSED
tests/test_game_logic.py::test_new_game_state_respects_difficulty_range PASSED
tests/test_game_logic.py::test_win_on_first_attempt_gives_100_points PASSED
tests/test_game_logic.py::test_win_on_later_attempt_scores_less PASSED
tests/test_game_logic.py::test_win_score_floor_is_10 PASSED
tests/test_game_logic.py::test_too_high_on_even_attempt_deducts_points PASSED
tests/test_game_logic.py::test_too_high_on_odd_attempt_deducts_points PASSED
tests/test_game_logic.py::test_too_high_and_too_low_penalize_equally PASSED
tests/test_game_logic.py::test_wrong_guess_score_never_goes_below_zero PASSED
tests/test_game_logic.py::test_multiple_wrong_guesses_stay_at_zero PASSED
tests/test_game_logic.py::test_final_score_clamps_negative_to_zero PASSED
tests/test_game_logic.py::test_final_score_preserves_positive_score PASSED
tests/test_game_logic.py::test_final_score_is_zero_when_raw_is_zero PASSED
tests/test_game_logic.py::test_info_bar_shows_correct_attempts_before_any_guess PASSED
tests/test_game_logic.py::test_info_bar_decrements_immediately_after_submit PASSED

========================= 24 passed in 1.17s =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
