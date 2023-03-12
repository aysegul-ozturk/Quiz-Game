from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


question_bank = []
for question in question_data:   # question_data is list of dictionaries (json)
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_bank)  # list of Question objects
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print(f"You've completed the quiz\nYour final score was: {quiz.score}/{quiz.question_number}")
