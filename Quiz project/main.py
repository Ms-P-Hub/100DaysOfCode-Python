from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

play = QuizBrain(question_bank)
score = 0

while play.still_has_questions():
    if play.next_question():
        score += 1
        print(f"You got it right!\nYour current score is {score}/{len(question_bank)}\n")
    else:
         print(f"That was incorrect!\nYour current score is {score}/{len(question_bank)}\n")