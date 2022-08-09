from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question_bank.append(Question(q_text=data["question"], q_answer=data["correct_answer"]))

q = QuizBrain(question_bank)

while q.still_has_questions():
    q.next_question()

print(f'You completed the quiz!\nYour final score was: {q.score}/{len(q.question_list)}')




