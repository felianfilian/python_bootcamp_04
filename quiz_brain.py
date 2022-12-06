
class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_bank = question_bank
        self.score = 0

    def has_questions(self):
        return self.question_number < len(self.question_bank)

    def next_question(self):
        current_question = self.question_bank[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number} {current_question.text} yes(a) or no(b)\n")
        if choice == "a":
            choice = "True"
        if choice == "b":
            choice = "False"
        self.check_answer(choice, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer or user_answer == correct_answer:
            print("perfect")
            self.score += 1
        else:
            print("You are wrong")

    def show_score(self):
        print("Score: " + str(self.score) + " / " + str(len(self.question_bank)))


