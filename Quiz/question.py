class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def get_question(self):
        return self.question

    def get_answer(self):
        return self.answer

    def is_answer_correct(self, answer):
        if self.get_answer() == answer:
            return True
        else:
            return False