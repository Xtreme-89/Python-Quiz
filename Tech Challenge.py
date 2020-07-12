import ast

import random

score = 0

print("Would you like to do the easy quiz or the hard quiz?")
easy_hard = input("\neasy/hard: ")

with open('hard_questions.txt') as qh:
    quiz_hard = ast.literal_eval(qh.read())

with open('easy_questions.txt') as qe:
    quiz_easy = ast.literal_eval(qe.read())


def ask_question(quiz):
    global score
    number_of_loops = 1
    wrong_questions = []
    correct_questions = []
    for question in random.sample(quiz, 5):
        print(str(number_of_loops) + ". " + question.get("question"))
        print(question.get("choices"))
        a1 = input("\nType your answer: ")

        while a1.lower() not in ["a", "b", "c", "d"]:
            print("that's not a choice!\n")
            a1 = input("\nType your answer: ")

        if a1.lower() == question.get("answer"):
            print("well done\n")
            score += 1
            correct_questions.append(question.get("question"))
            correct_questions.append("You chose: " + question.get("answer"))
            correct_questions.append("")
        else:
            print("better luck next time\n")
            score = score
            wrong_questions.append(question.get("question"))
            wrong_questions.append("The  correct answer was: " + question.get("answer"))
            wrong_questions.append("")
        number_of_loops += 1
    print("\nCorrect Questions:\n")
    for qa in correct_questions:
        print(qa)

    print("\nWrong Questions:\n")
    for aq in wrong_questions:
        print(aq)


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
