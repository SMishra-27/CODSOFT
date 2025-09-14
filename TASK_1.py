# Rule-Based Chatbot Example

def chatbot_response(user_input):
    user_input = user_input.lower()  # make input case-insensitive

    # Greeting responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! Thanks for asking."
    
    # Information responses
    elif "your name" in user_input:
        return "I'm a simple rule-based chatbot created in Python."
    
    elif "time" in user_input:
        from datetime import datetime
        return "The current time is " + datetime.now().strftime("%H:%M:%S")
    
    elif "date" in user_input:
        from datetime import datetime
        return "Today's date is " + datetime.now().strftime("%Y-%m-%d")
    
    # Farewell responses
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a nice day."
    
    # Default response
    else:
        return "I'm not sure I understand. Could you please rephrase?"

# Main chatbot loop
print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Chatbot:", response)
    
    if "bye" in user_input.lower() or "goodbye" in user_input.lower():
        break
