def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    # FIXME: Logic breaks here
    if difficulty == "Hard":
        return 1, 150
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def build_new_game_state(difficulty: str) -> dict:
    """Return a fresh state dict for a new game at the given difficulty."""
    import random
    low, high = get_range_for_difficulty(difficulty)
    return {
        "secret": random.randint(low, high),
        "attempts": 0,
        "status": "playing",
        "history": [],
    }
