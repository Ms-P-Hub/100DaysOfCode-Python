from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

play = QuizBrain(question_bank)

while play.still_has_questions():
    play.next_question()
    print()
    
print(f"Quiz is complete. Your final score is {play.score} out of {len(question_bank)}")