import random
# For the timer function
import threading
# Score as zero
score = 0
# Prints this once timer has finished
def time_up():
    print("Time's up!")


# Defines function used in quiz code
def ask_question(quiz, time):
    # Sets the score as global, so that it is editable inside and outside function
    global score
    number_of_loops = 1
    wrong_questions = []
    correct_questions = []
    print("\nYou get " + str(time) + " seconds to answer each question.\n")
    for question in random.sample(quiz, 5):
        print(str(number_of_loops) + ". " + question.get("question"))
        print(question.get("choices"))
        # If timer finishes, goto next question
        timer = threading.Timer(time, time_up)
        timer.start()
        a1 = input("\nType your answer: ")
        # If the answer isn't a, b, c, or d, it keeps asking for an answer
        while a1.lower() not in ["a", "b", "c", "d"]:
            print("that's not a choice!\n")
            a1 = input("\nType your answer: ")
        # If the user's answer matches the actual answer, it adds the question and answer to a list and adds 1 to the score
        if a1.lower() == question.get("answer"):
            print("well done\n")
            score += 1
            correct_questions.append(question.get("question"))
            correct_questions.append("You chose: " + question.get("answer"))
            correct_questions.append("")
        else:
            # It add the question to the list of wrong questions  and answers, and keeps the score the same
            print("better luck next time\n")
            score = score
            wrong_questions.append(question.get("question"))
            wrong_questions.append("The  correct answer was: " + question.get("answer"))
            wrong_questions.append("")
        # Adds 1 to the umber of loops (for the question number)
        number_of_loops += 1
    # Prints the list of correct questions and answers
    print("\nCorrect Questions:\n")
    for qa in correct_questions:
        print(qa)
    # Prints the list of wrong questions and correct answers
    print("\nWrong Questions:\n")
    for aq in wrong_questions:
        print(aq)