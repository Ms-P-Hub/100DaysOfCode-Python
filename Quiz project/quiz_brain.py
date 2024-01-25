class QuizBrain:
    score = 0
    
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number}: {self.question_list[self.question_number-1].text}. Type 'True' or 'False': "
        ).capitalize()
        # # while (not answer == 'True') or (not answer == 'False'):
        # #     print("Invalid input. Please answer (True/False)")
        # #     answer = input(f"Q.{self.question_number}: {self.question_list[self.question_number-1].text}. Type 'True' or 'False': ").capitalize()
        # return answer == self.question_list[self.question_number-1].answer
        self.check_answer(answer, self.question_list[self.question_number - 1].answer)

    def still_has_questions(self):
        return self.question_number != len(self.question_list)

    def check_answer(self, user_answer, current_answer):
        if user_answer == current_answer:
            self.score += 1
            print(
                f"You got it right!\nYour current score is {self.score}/{self.question_number}\n"
            )
        else:
            print(
                f"That was incorrect!\nYour current score is {self.score}/{self.question_number}\n"
            )
