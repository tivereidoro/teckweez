#!/usr/bin/python3
import os
import random
from pyfiglet import figlet_format
from question_bank import quiz_areas


# Quiz UI border
border: str = "==========================================="


def main():
    # Introduction
    os.system('cls' if os.name == 'nt' else 'clear')
    print(border)
    print(figlet_format("TecKweez", font="standard"))
    print(border)
    print(
        """
        -- Welcome to TecKweez --

Test your knowledge about tech even
as you learn, on TecKweez..

Choose your niche and kweez away..🚀
        """
    )

    while True:
        print(border)
        print()
        # Display available quiz areas
        print("Available Tech Niches..\n")
        for i, area in enumerate(quiz_areas, 1):
            print(f"{i}. {area}")

        print()
        while True:
            try:
                choice = int(input("Choose your niche: (Enter 1 or 2 or 3 ...) ")) - 1
                if choice not in range(len(quiz_areas)) or type(choice) != int:
                    continue
                else:
                    break
            except ValueError:
                continue
        print()
        quiz_area = list(quiz_areas.keys())[choice]
        questions = quiz_areas[quiz_area]
        os.system('cls' if os.name == 'nt' else 'clear')
        print(border)
        print(f"\nStarting {quiz_area} quiz...\n")
        play_quiz_game(questions)

        # Ask user if they want to play again
        print()
        play_again = input("Do you want to play again? (Y/n): ")
        if play_again.lower() in ["y", "yes"]:
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        else:   # play_again.lower() in ["n", "no"]:
            break

    os.system('cls' if os.name == 'nt' else 'clear')
    print(border)
    print(figlet_format("Thank you for playing TecKweez!", font="standard"))
    print(border)
    print("\nThank you for playing TecKweez! 🚀 🚀 🚀\n")


def get_random_question(questions: list) -> dict:
    """Returns a random question from the questions list."""
    return random.choice(questions)


def check_answer(question: dict, answer) -> bool:
    """Check if the provided answer is correct for the given question."""
    return question["answer"].lower() == answer.lower()


def ask_question(question):
    """Ask the user a question and return their answer."""
    print(question["question"])
    print()
    for option in question["options"]:
        print(option)
    while True:
        print()
        answer = input("Enter your answer (A, B, C, or D): ")
        if answer.upper() in ["A", "B", "C", "D"]:
            return answer.upper()
        else:
            continue


def play_quiz_game(questions):
    """Play the quiz game."""
    score = 0
    for i in range(len(questions)):
        print(border)
        print()
        print(f"Question {i + 1}.", end=" ")
        question = get_random_question(questions)
        answer = ask_question(question)
        print()
        if check_answer(question, answer):
            score += 1
            print("Correct!")
        else:
            print("Oops, not quite right!")
            print(f"\nThe correct answer is {question['answer']}.\n")

        # print(f"Your current score is: {score}/{len(questions)}\n")

    # Final score
    print(border)
    print()
    if score == 1:
        print(f"You got {score} question right, out of {len(questions)}\n")
    else:
        print(f"You got {score} questions right, out of {len(questions)}\n")

    print(f"Your final score is: {round(score / len(questions) * 100)}%\n")
    print(border)
    print("####### That's the end of the quiz! #######")


# Call main function
if __name__ == "__main__":
    main()


#####################################################
#                                                   #
#               Author: Tivere IDORO                #
#                                                   #
#               CS50p Final Project.                #
#                                                   #
#   https://cs50.harvard.edu/python/2022/project/   #
#                                                   #
#####################################################
