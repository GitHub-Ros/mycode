#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests

URL = "https://opentdb.com/api.php?amount=10&category=18&difficulty=hard&type=multiple"

def get_trivia_data(url, num_questions=5):
    # Make a GET request to the trivia API
    response = requests.get(url, params={'amount': num_questions})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        trivia_data = response.json()

        # Extract questions and answers from the response
        questions = [question['question'] for question in trivia_data['results']]
        answers = [question['correct_answer'] for question in trivia_data['results']]

        return questions, answers
    else:
        # Print an error message if the request was not successful
        print(f"Error: Unable to fetch trivia questions. Status code: {response.status_code}")
        return None, None

def main():
    questions, answers = get_trivia_data(URL)

    # Print questions and answers
    if questions and answers:
        for i, (question, answer) in enumerate(zip(questions, answers), start=1):
            print(f"Question {i}: {question}")
            print(f"Answer {i}: {answer}")
            print("-" * 30)

if __name__ == "__main__":
    main()

