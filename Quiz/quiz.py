class Quiz:
    def __init__(self, score, questions):
        self.score = score
        self.questions = questions

    def show_question(self):
        for question in self.questions:
            answer = input(question["question"])
            self.score.update_score(question.is_answer_correct(answer))
            if question.is_answer_correct(answer) == False:
                print("You got the wrong answer")
                print(f"Your final score is {self.score.get_score()}")
                break
            else:
                print("Correct")
                print(f"Your current score is {self.score.get_score()}")
        print(f"Congratulations! You got all answers. Your final score is {self.score.get_score()}")