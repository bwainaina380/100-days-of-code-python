from question import Question

class Quiz:
    def __init__(self, score, questions_list):
        self.score = score
        self.questions_list = questions_list
        self.questions = []

    def generate_questions(self):
        for question in self.questions_list:
            self.questions.append(Question(question["question"], question["answer"]))

    def start_quiz(self):
        self.generate_questions()
        for question in self.questions:
            answer = input(question.get_question())
            self.score.update_score(question.is_answer_correct(answer))
            if question.is_answer_correct(answer) == False:
                print("You got the wrong answer")
                print(f"Your final score is {self.score.get_score()}\n")
                break
            else:
                print("Correct")
                print(f"Your current score is {self.score.get_score()}\n")