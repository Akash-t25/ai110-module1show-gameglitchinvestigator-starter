from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_check_guess_high_and_low():
    # When guess > secret, outcome should be "Too High"
    outcome_high, _ = check_guess(75, 50)
    assert outcome_high == "Too High"

    # When guess < secret, outcome should be "Too Low"
    outcome_low, _ = check_guess(25, 50)
    assert outcome_low == "Too Low"
