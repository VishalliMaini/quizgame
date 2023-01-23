from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
#creating a list containing multiple objects
question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_ans=question["answer"]
    newquestion=Question(question_text,question_ans)
    question_bank.append(newquestion)

quiz=QuizBrain(question_bank)
while(quiz.still_has_questions()):
    quiz.next_question()

print("You have completed the quiz ")
print(f"Your final score was:{quiz.score}/{quiz.question_number}")