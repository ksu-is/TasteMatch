import random

# Food database 
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
    print("🍽️ Welcome to TasteMatch!")

    while True: 
        mood = input("\nWhat mood are you in? (comfort, spicy, healthy, adventurous) or press Enter to quit: ").lower()

        if mood == "":
            print("Goodbye")
            break
        budget = input("What is your budget (low, medium, high): ").lower()

        # Filter foods based on user input
        matches = []
        for food in foods:
            if food["mood"] == mood and food["budget"] == budget:
                matches.append(food["name"])

        # If not exact matches, fallback to mood only
        if not matches:
            for food in foods:
                if food["mood"] == mood:
                    matches.append(food["name"])

        # If still no matches, random fallback
        if not matches:
            matches = [food["name"] for food in foods]

        choice = random.choice(matches)
        message = random.choice(messages)

        print(f"\n You should try: {choice}🍴")
        print(f"{message}")

# Run the program
tastematch()
