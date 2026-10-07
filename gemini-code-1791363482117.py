import random
from datetime import date, timedelta

# Dictionary storing keywords and possible replies
responses = {
    "hello": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "how are you": [
        "I am just a bot, but I am doing great!",
        "I'm a bot, but I feel awesome!"
    ],
    "what is your name": ["I am CodeBot.", "You can call me CodeBot."],
    "what can you do": [
        "I can chat with you, calculate your BMI, and calculate your exact age!",
        "I can answer basic questions, calculate Body Mass Index (BMI), and find your age in years, months, and days."
    ],
    "thank you": ["You're welcome!", "No problem!", "Happy to help!"],
    "bye": ["Goodbye! Have a nice day!", "See you later!", "Bye! Take care!"]
}

def calculate_bmi():
    """Interactive function to ask for weight/height and return the calculated BMI category."""
    print("CodeBot: Sure! Let's calculate your BMI.")
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height (in cm or meters): "))
        
        # Convert height from centimeters to meters if necessary
        if height > 3:
            height = height / 100

        bmi = weight / (height ** 2)
        
        # Determine category based on standard BMI ranges
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        return f"Your BMI is {bmi:.2f}, which is categorized as: {category}."
    except ValueError:
        return "Invalid input! Please enter numerical values for weight and height."

def calculate_age():
    """Interactive function to ask for birth date and return exact age in years, months, and days."""
    print("CodeBot: Let me calculate your age!")
    try:
        day = int(input("Enter your birth day (DD): "))
        month = int(input("Enter your birth month (MM): "))
        year = int(input("Enter your birth year (YYYY): "))

        today = date.today()
        birth_date = date(year, month, day)

        # Basic age subtraction
        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        # Adjust if days are negative
        if days < 0:
            months -= 1
            prev_month = date(today.year, today.month, 1) - timedelta(days=1)
            days += prev_month.day

        # Adjust if months are negative
        if months < 0:
            years -= 1
            months += 12

        return f"Your Age is: {years} years, {months} months, and {days} days."
    except ValueError:
        return "Invalid date entered! Please enter valid numbers for day, month, and year."

def get_response(user_input):
    """Checks user input against dictionary keys and returns a response."""
    user_input = user_input.lower()
    
    # Check for feature keywords
    if "bmi" in user_input:
        return calculate_bmi()
    elif "age" in user_input:
        return calculate_age()
    
    # Search for matching keywords in the input sentence
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
            
    # Default fallback message if no keyword matches
    return "Sorry, I didn't understand that. Can you rephrase?"

# Start of the chatbot interface
print("Hello! I am CodeBot. How can I help you?")
print("Type 'bmi' for BMI calculator, 'age' for Age calculator, or 'bye' to exit.\n")

# Main conversational loop
while True:
    user_input = input("You: ")
    
    # Check if the user wants to exit
    if "bye" in user_input.lower():
        print("CodeBot:", random.choice(responses["bye"]))
        break
    
    # Get and print the response
    response = get_response(user_input)
    print("CodeBot:", response)

print("\nThank you for chatting with us!")