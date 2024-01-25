from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for question in question_data:
    new_question = Question(question["text"],question["answer"])
    question_bank.append(new_question)
    
play = QuizBrain(question_bank)
score = 0
for i in question_bank:
    if play.next_question():
        score += 1  