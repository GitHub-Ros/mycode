import requests
import html
import random

BASE_URL = "https://opentdb.com/api.php?amount=10&category=18&difficulty=hard&type=multiple"

def get_trivia_data(amount=5, category=None, difficulty=None, q_type=None):
    params = {'amount': amount}
    if category:
        params['category'] = category
    if difficulty:
        params['difficulty'] = difficulty
    if q_type:
        params['type'] = q_type

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        trivia_data = response.json()
        questions = [html.unescape(question['question']) for question in trivia_data['results']]
        return questions, trivia_data['results']
    else:
        print(f"Error: Unable to fetch trivia questions. Status code: {response.status_code}")
        return None, None

def main():
    amount = int(input("Enter the number of questions: "))
    category = input("Enter the category (or press Enter for any): ")
    difficulty = input("Enter the difficulty (easy, medium, hard, or press Enter for any): ")
    q_type = input("Enter the type (multiple, boolean, or press Enter for any): ")

    questions, questions_data = get_trivia_data(amount=amount, category=category, difficulty=difficulty, q_type=q_type)

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
            if user_answer.isdigit() and 1 <= int(user_answer) <= len(all_answers):
                if user_answer == str(all_answers.index(correct_answer) + 1):
                    print("Correct!")
                else:
                    print(f"Wrong! The correct answer is: {correct_answer}")
            else:
                print("Invalid input. Please enter a number corresponding to your choice.")
            print("-" * 30)

if __name__ == "__main__":
    main()

