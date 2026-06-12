# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - The first time a ran it, it glitched a bit as the entry box was missing. Untill I had to refresh it then it appeared. The general layout of the game looked okay. It seemed like it will not have any problem. It was actually easy to navigate.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - Incorrect hint logic: For instance, the secret code was 93, but after guessing 38 the game displayed "go lower" instead of directing the player to guess higher. And vice versa when a higher number is entered “go higher” it says.
  - Invalid range validation: The game accepts guesses outside the stated range. 
  - New Game button not functioning after game over: Clicking "New Game" refreshes the page and displays "Game over. Start a new game to try again," but a new game is not actually started.
  - Attempt counter off by one: The number of remaining attempts is inaccurate and appears to be off by one. 
  - Difficulty change does not reset game state: Switching difficulty levels retains the previous secret code and used attempts. For example, changing from Normal to Easy keeps the old secret number and carries over attempts already used instead of starting a fresh game.
  - Inconsistent feedback for repeated guesses: Entering the same number multiple times causes the hint to alternate between "guess lower" and "guess higher," even though the guess value has not changed.


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Secret code = 93, guessed 38 | Game should display "Go Higher" because 38 is less than 93 | Game displayed "Go Lower," causing the player to move away from the correct answer | No console errors observed |
| Entered 0 and 100 as guesses | Game should reject values outside the allowed range (1–100) and prompt for a valid input | Game accepted the values and provided misleading hints ("Go Lower" for 0 and "Go Higher" for 100) | No console errors observed |
| Clicked "New Game" after game over | A new game should start with a new secret code and reset attempts | Page refreshed and displayed "Game over. Start a new game to try again," but new game didn't begin | No console errors observed |
| Repeatedly entered the same guess value | Game should provide the same feedback or indicate the guess was already made | Hint alternated between "Guess Higher" and "Guess Lower" despite the input remaining unchanged | No console errors observed |
| 5 attempts allowed | it should display my 5 attempts and decrease in realtime as i attempt guessing | it displays 4 attempts and only gives me 4 attempts | No console errors observed |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - I used ChatGPT, Claude and GitHub Copilot. I utilized ChatGPT for certain commands that I needed for instance when setting up the project at the begining. Then I used GitHub Copilt and Claude for understanding, debugging and fixing the code. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - One example  of a suggestion that was correct that I didn't notice was how the range of the difficult: Hard was smaller than the normal which makes it easier to guess the number. Claude gave me this insight but I used GitHub Copilot to get its sugestion on the fix and if increasing the range would actually make it harder. I then verified the result by testing the game and seeing that it was indeed harder to guess the number.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - One problem I came across was at the beginning when I was trying to set up the project. I asked ChatGPT for the commands to run the project correctly and it suggested installing streamlit. Hiweever, after installing the requirements, the project couldn't still run because my isntalled python version 3.13.13 wasn't being recognized. It kept giving me wrong suggestions on what could be the problem despite giving it full description of the error. After some time I discovered that it was a very small issue and it was with how you run the commands in order for the version to be recognized. I had to run the command with py and not python. I then verified the result by running the project and seeing that it was working fine without any errors.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - Whenever I fix a bug, I asked claude to give test cases that would actually verify the bug I was just fixing. Then I would run them to see if it was actually fixed. I also tried to test the game manually by playing it and trying to reproduce the bug. If I couldn't reproduce it then I would consider it fixed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - One test I ran was to check if the hints were correct after fixing the hint logic. I checked the secret code from the Developer Debug Info and then made guesses that were both higher and lower than the secret code. I verified that the game provided the correct hints ("Go Higher" for lower guesses and "Go Lower" for higher guesses). This test showed me that the hint logic was now working correctly and providing accurate feedback to the player.
- Did AI help you design or understand any tests? How?
  - Yes, AI (Claude to be specific) helped me come up with the test cases which were placed in test_bugs.py. For instance, after fixing the bug that allowed guesses outside the difficulty range, guessing 25 in a 1-20 range should be rejected. I used this test case to verify that the fix was successful.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
