class Score:
    def __init__(self):
        self.score = 0

    def update_score(self, is_answer_correct):
        if is_answer_correct == True:
            self.score += 1
        else:
            self.score -= 1

    def get_score(self):
        return self.score