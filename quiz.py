from quiz_model import Question
from quiz_data import question_data
from quiz_brain import  QuizBrain

def start():
    lifes = 3
    question_bank = []
    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    while lifes > 0:
        print(f"LIFES: {lifes}")
        quiz_brain = QuizBrain(question_bank)
        if not quiz_brain.next_question():
            lifes -= 1

