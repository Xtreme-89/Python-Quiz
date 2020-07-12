import random

score = 0

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