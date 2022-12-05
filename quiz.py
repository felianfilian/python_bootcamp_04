


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


def start():
    new_q = Question("highest building on earth", "Burk Khalifa")
    print(new_q.text)
