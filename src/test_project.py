import pytest
from unittest.mock import patch
from project import get_random_question, check_answer, ask_question, quiz_areas


def test_get_random_question():
    questions = quiz_areas["ML/AI"]
    question = get_random_question(questions)
    assert question in questions


def test_check_answer_correct():
    questions = quiz_areas["DevOps"]
    question = questions[1]
    assert check_answer(question, "A") == True


def test_check_answer_incorrect():
    questions = quiz_areas["Cyber Security"]
    question = questions[1]
    assert check_answer(question, "B") == False


@patch('builtins.input', return_value='C')
def test_ask_question(mock_input):
    question = quiz_areas["Web Development"][0]
    answer = ask_question(question)
    assert answer == "C"


if __name__ == "__main__":
    pytest.main()
