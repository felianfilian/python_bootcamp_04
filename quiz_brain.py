
class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 5
        self.question_bank = question_bank

    def next_question(self):
        return self.question_bank[self.question_number]

