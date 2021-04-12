class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def is_answer_correct(self, answer):
        if self.answer == answer:
            return True
        else:
            return False