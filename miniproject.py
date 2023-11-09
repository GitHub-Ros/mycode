#!/usr/bin/env python3
import random
# List of project ideas for different technology stacks
tech_project_ideas = {
    "Web Development": [
        "Create a portfolio website to showcase your work using HTML, CSS, and JavaSctipt.",
        "Build a blogging platform with user authentication using Django.",
        "Develop a simple e-commerce website using React and Redux."
    ],
    "Data Science": [
        "Analyze and visualize a dataset of your choice using Python and Matplotlib.",
        "Create a machine learning model for sentiment analysis.",
        "Build a recommendation system for movies or books."
    ],
    "Game Development":[
        "Develop a 2D platformer game using Pygame.",
        "Create a text-based adventure game in Python.",
        "Build a simple puzzle game using Unity."
    ]

}
def generate_project_idea(tech_stack):
    if tech_stack in tech_project_ideas:
        ideas = tech_project_ideas[tech_stack]
        if ideas:
            return random.choice(ideas)
        else:
            return "No project ideas available for this tech stack."
    else:
        return "Tech stack not found. Please choose a valid option."

def display_menu():
    print("Welcome to the project generator menu: ")
    print("1. Generate Project Idea")
    print("2. About the Tool")
    print("3. Exit")

def main():
    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == "1":
            tech_stack = input("Enter your preferred technology stack: ")
            idea = generate_project_idea(tech_stack) # Pass the tech_stack as an argument
            print("Project Idea: ", idea)
        elif choice == "2":
            print("This tool helps you generate ideas for your next project")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
