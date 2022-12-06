
class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 5
        self.question_bank = question_bank

    def next_question(self):
        current_question = self.question_bank[self.question_number]
        choice = input(f"Q.{self.question_number} {current_question.text} yea(a) or no(b)\n")

        if choice == "a" and current_question.answer == "True" or choice == "b" and current_question.answer == "False":
            print("perfect")
        else:
            print("You are wrong")

