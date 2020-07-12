import ast

import random

from ask_question_func import ask_question

score = 0

print("Would you like to do the easy quiz or the hard quiz?")
easy_hard = input("\neasy/hard: ")

with open('hard_questions.txt') as qh:
    quiz_hard = ast.literal_eval(qh.read())

with open('easy_questions.txt') as qe:
    quiz_easy = ast.literal_eval(qe.read())


if easy_hard.lower() == "easy":
    print("\n   Welcome to the Quiz of Books!\nThis quiz will be about Harry Potter\n")
    ask_question(quiz_easy)

elif easy_hard.lower() == "hard":
    print("\n     Welcome to the General Knowledge Quiz!\nThis quiz is about random facts about the world\n")

    ask_question(quiz_hard)

else:
    print("Ok, so you want no quiz.\n")

info = open("info.txt", "w")

name = input("Enter your name:  ")
age = input("Enter your age:  ")

if easy_hard.lower() == "easy":
  info.write("You chose the EASY quiz.\n\n")
elif easy_hard.lower() == "hard":
  info.write("You chose the HARD quiz.\n\n")
else:
  info.write("You didn't do the quiz.\n\n")

info = open("info.txt", "a")

info.write("Your name: " + name + "\n")

info.write("Your age: " + str(age) + "\n")

info.write("You got: " + str(score) + "/5")
