import ast

import random

from ask_question_func import ask_question
#to set the value for the score
score = 0

# Asks the user to choose
print("Would you like to do the easy quiz or the hard quiz?")
easy_hard = input("\neasy/hard: ")
# Opens easy and hard files and sets the lists of dictionaries as variables
with open('hard_questions.txt') as qh:
    quiz_hard = ast.literal_eval(qh.read())

with open('easy_questions.txt') as qe:
    quiz_easy = ast.literal_eval(qe.read())

# If the user chose easy, it passes the list of dictionaries in "quiz_easy", same for hard
if easy_hard.lower() == "easy":
    print("\n   Welcome to the Quiz of Books!\nThis quiz will be about Harry Potter\n")
    ask_question(quiz_easy, 8)
# Calls on imported function and chooses quiz and time
elif easy_hard.lower() == "hard":
    print("\n     Welcome to the General Knowledge Quiz!\nThis quiz is about random facts about the world\n")
    ask_question(quiz_hard, 4)
# If user doesn't input hard or easy, it doesn't do the quiz, score 0
else:
    print("Ok, so you want no quiz.\n")
# Tells user their score
print("\nYour Score: " + str(score) + "/10")
# Creates a new file
info = open("info.txt", "w")
# User inputs name and age
name = input("Enter your name:  ")
age = input("Enter your age:  ")
# Writes the user's Quiz data onto the new file
if easy_hard.lower() == "easy":
  info.write("You chose the EASY quiz.\n\n")
elif easy_hard.lower() == "hard":
  info.write("You chose the HARD quiz.\n\n")
else:
  info.write("You didn't do the quiz.\n\n")

info.write("Your name: " + name + "\n")

info.write("Your age: " + str(age) + "\n")

info.write("You got: " + str(score) + "/10")
