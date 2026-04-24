import random

# Food database (expanded with categories)
foods = [
    {"name": "Pizza", "mood": "comfort", "budget": "medium"},
    {"name": "Pasta", "mood": "comfort", "budget": "low"},
    {"name": "Sushi", "mood": "adventurous", "budget": "high"},
    {"name": "Tacos", "mood": "spicy", "budget": "high"},
    {"name": "Salad", "mood": "healthy", "budget": "low"},
    {"name": "Burger", "mood": "comfort", "budget": "medium"},
    {"name": "Smoothie Bowl", "mood": "healthy", "budget": "medium"},
    {"name": "Fried Rice", "mood": "comfort", "budget": "low"},
    {"name": "Steak", "mood": "adventurous", "budget": "high"},
    {"name": "Chicken Nuggets", "mood": "comfort", "budget": "low"}
]
messages = [
    "Good choice!!",
    "That sounds so good!",
    "You should definitely try this",
    "Trust me on this one!", 
    "You're going to love this!"
]

def tastematch():
    print("Welcome to TasteMatch!")

    while True: 
        mood = input("\nWhat mood are you in? (comfort, spicy, healthy, adventurous) or press Enter to quit: ").lower()

        if mood == "":
            print("Goodbye")
            break
        budget = input("What is your budget (low, medium, high): ").lower()

        