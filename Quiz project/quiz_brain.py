class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        
    def next_question(self):
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {self.question_list[self.question_number-1].text}. Type 'True' or 'False': ").capitalize()
        if answer == self.question_list[self.question_number-1].answer:
            return True
        return False
            
        