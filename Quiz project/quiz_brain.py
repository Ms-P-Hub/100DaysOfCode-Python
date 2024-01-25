class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        
    def next_question(self,question_list):
        score = 0
        for i in range(len(question_list)):
            answer = input(f"Q{i+1}. {question_list[i].text}. Type 'True' or 'False': ").capitalize()
            if answer == question_list[i].answer:
                score += 1
            print(f"Your Score: {score}")
            
        