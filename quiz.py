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

    while quiz_brain.has_questions():
        quiz_brain.show_score()
        quiz_brain.next_question()

