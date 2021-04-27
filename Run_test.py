from multiplechoice import Question

question_prompts = ["What is my middle name? \n(a) James\n(b) Jack\n (c) Thomas\n (d) Joel\n\n",
                    "What day of the month was I born?\n (a) 8th \n (b) 9th \n (c) 27th \n (d) 11th\n\n",
                    "Am I left-handed or right handed? \n (a) right \n (b) left \n (c) wrong\n \n",
                    "What am I currently majoring in? \n (a) Electrical Technology \n (b) Industrial Electronics \n (c) Computer Science \n (d) Industrial Maintenance\n \n "
                    ]
questions = [
    Question(question_prompts[0], "d"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)
