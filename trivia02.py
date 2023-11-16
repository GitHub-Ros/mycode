import requests
import html
import random

URL = "https://opentdb.com/api.php?amount=10&category=18&difficulty=hard&type=multiple"

def get_trivia_data(url, num_questions=5):
    response = requests.get(url, params={'amount': num_questions})
    if response.status_code == 200:
        trivia_data = response.json()
        questions = [html.unescape(question['question']) for question in trivia_data['results']]
        return questions, trivia_data['results']
    else:
        print(f"Error: Unable to fetch trivia questions. Status code: {response.status_code}")
        return None, None

def main():
    questions, questions_data = get_trivia_data(URL)

    if questions and questions_data:
        for i, question in enumerate(questions, start=1):
            correct_answer = html.unescape(questions_data[i - 1]['correct_answer'])
            incorrect_answers = [html.unescape(answer) for answer in questions_data[i - 1]['incorrect_answers']]
            all_answers = incorrect_answers + [correct_answer]
            random.shuffle(all_answers)

            print(f"Question {i}: {question}")

            for j, choice in enumerate(all_answers, start=1):
                print(f"{j}. {choice}")

            user_answer = input("Your answer: ")
            if user_answer.lower() == str(all_answers.index(correct_answer) + 1):
                print("Correct!")
            else:
                print(f"Wrong! The correct answer is: {correct_answer}")
            print("-" * 30)

if __name__ == "__main__":
    main()

