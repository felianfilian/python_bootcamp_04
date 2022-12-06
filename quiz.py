from quiz_model import Question
from quiz_data import question_data
from quiz_brain import  QuizBrain

def start():
    question_bank = []
    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz_brain = QuizBrain(question_bank)
    choice = input(f"{quiz_brain.next_question().text} yea(a) or no(b)")
    if choice == "a" and quiz_brain.next_question().answer == "True":
        print("perfect")
    else:
        print("You are wrong")
    if choice == "b" and quiz_brain.next_question().answer == "False":
        print("perfect")
    else:
        print("You are wrong")
