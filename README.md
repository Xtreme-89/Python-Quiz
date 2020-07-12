# Python-Quiz
## Technology Projects

You’re going to develop a multiple-choice, brain-teaser program in Python that could be used to test the user’s knowledge.
You can choose the topic of the questions in your brain-teaser.
Can you complete the following tasks?

---

## Task
- Create a program on Python that will ask the user 10 questions on the topic of your choice. A scoring system will be used which will be set to 0 at the start of the program.
- The program should take the user’s response and check whether the answer is correct. If it’s correct then their score should increase by 1.
- At the end of the 10 questions the program should take the user’s name and age – these should be stored in an external file along with their total score.
- Print the total score to the user.
- Using iteration, can you develop your program to include two different levels (easy and hard)? The user can choose which one to play.
- If they choose easy then they have a timer of 10 seconds to answer each question.
- If they choose hard then they have a timer of 4 seconds to answer each question.
---
## Solution Approach

- I created two files, one for hard questions and one for the easy questions.
- I then **imported** the two files and used **ast** to scan for **python literals.**
- I used this to identify the questions as a list of dictionaries. 
- Next, I used a function to randomly pick questions from either the *easy* file or the *hard* file (depending on what the user selected)
- The function then calculates the score, and tells you the score at the end.
- Finally, it creates a new file, called `info.txt` which has all the information about the user's quiz (e.g. name, age, easy/hard, score)
---
## Improvement Scopes

- 