# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, the hints were completely backwards and the range display 
was wrong. Here are the three bugs I noticed:

**Bug 1: Hints are backwards**
- Expected: If my guess was too low, the game should tell me to go higher
- Actual: The game told me to go LOWER when my guess was 2 and the secret was 62

**Bug 2: Range display mismatch**
- Expected: The instruction box should show the correct range for the selected difficulty
- Actual: On Easy mode (range 1-20), the box still said "Guess a number between 1 and 100"

**Bug 3: Hard mode is easier than Normal**
- Expected: Hard mode should have a wider range, making it harder to guess the number
- Actual: Hard mode uses range 1-50 while Normal uses 1-100, making Hard actually easier

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used claude and claude code for this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Claude correctly identified that the `check_guess` function had backwards hints,
where `guess > secret` was returning "Go HIGHER!" instead of "Go LOWER!". I verified
this by playing the game and confirming that after the fix, guessing 18 with a secret
of 66 correctly showed "Go HIGHER!".
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Claude initially warned that the 3 pre-existing pytest tests would fail because they
compared the full tuple against a plain string. This was correct that they would fail,
but it was misleading because it made it seem like a bigger problem than it was. I fixed
it by asking Claude to unpack the tuples correctly and all 4 tests passed.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
I verified my fixes by running `python3 -m pytest` in the terminal which confirmed
all 4 tests passed. I also manually tested the live game by running `python3 -m streamlit run app.py` and guessing numbers to confirm the hints were
correct. For example, guessing 18 with a secret of 66 correctly showed "Go HIGHER!".
AI helped me design the test for check_guess by generating the test case that unpacked
the tuple correctly.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?
The secret number kept changing in the original app because Streamlit reruns the entire
script every time a user interacts with it, generating a new random number each time.
Streamlit "reruns" means the whole Python file runs from top to bottom on every interaction.
Session state is like a memory that persists between these reruns. The fix was using
`st.session_state.secret` so the secret is only generated once and stored.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
One habit I want to reuse is adding FIXME comments to mark bugs before fixing them,
since it gives a clear target for AI tools to focus on. Next time I work with AI on
a coding task, I would verify every AI suggestion by testing it myself before moving on
rather than assuming it is correct. This project changed how I think about AI generated
code because I now understand that AI can introduce subtle bugs like type mismatches
that are hard to spot without careful testing.
