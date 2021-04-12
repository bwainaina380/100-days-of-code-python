from quiz import Quiz
from score import Score
from questions_list import questions

quiz = Quiz(Score(), questions)
quiz.start_quiz()