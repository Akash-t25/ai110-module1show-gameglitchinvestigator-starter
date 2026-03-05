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

- [ ] Describe the game's purpose.
A number guessing game where the player tries to guess a secret 
number within a limited number of attempts, receiving hints after each guess.
- [ ] Detail which bugs you found.
- Hints were backwards (Go HIGHER when should say Go LOWER)
  - Secret number was converted to a string on even attempts causing wrong comparisons
  - Hard mode range (1-50) was easier than Normal mode (1-100)

- [ ] Explain what fixes you applied.
- Fixed check_guess function to return correct hints
  - Removed string conversion of secret number on even attempts
  - Refactored check_guess into logic_utils.py
  - All 4 pytest tests now pass

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
![Fixed Game Screenshot](screenshot.png)


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
