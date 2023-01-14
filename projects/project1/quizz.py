#! /usr/bin/env python3
#  -*- coding:utf-8 -*-


## Description
"""
The quizz is a series of randomly selected questions that the user has to answered.
Number of selected question is define by user.
For each question, user has three attempt.
If answer is correct, then user have one point, else, no point.
"""

## module
import random


## function

def start_quizz(number_of_chance):

    ## load (question, answer) tuples from a separate file in json format
    questions = { 1:("revolution", "1789"), 2:("moutarde", "yes"), 3:("albanie", "yes") }
    #question_file_path = ""
    #with open(question_file, "r") as filin:
    #    questions = json.load(filin)
    
    number_of_all_questions = list(range(1, len(questions)+1))
    
    
    # get random question, the number is defined by the user
    how_many_question = int(input("How many question do you want to answer ? : "))
    chosen_question = []
    for _ in range(how_many_question):
        random.shuffle(number_of_all_questions)
        chosen_question.append(number_of_all_questions.pop())
    
    
    ## now let the quizz begin
    # initiate user points
    points = 0
    # looping over the different questions that have been randomly selected
    for number in chosen_question:
        # unpacking question and answer from tuple
        question, answer = questions[number]
        limit = 0
        print(question)
        while True:
            if limit < number_of_chance:
                if input("Your answer : ") != answer:
                    limit += 1
                    print(f"No, try again, you still have {number_of_chance - limit} chance(s)")
                else:
                    points += 1
                    print("Yes, good answer.")
                    break
            else:
                print("Sorry, you spend all your try. Next question.")
                break
    
    print(f"Quizz over, you have a result of {points} / {how_many_question} points.")
    
if __name__ == "__main__":
    start_quizz(3)

