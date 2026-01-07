def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hi" or user_input == "hello":
        return "Hello!"
    elif user_input == "how are you":
        return "I am fine."
    elif user_input == "what is your name":
        return "My name is Chatbot."
    elif user_input == "what can you do":
        return "I can talk with you."
    elif user_input == "who made you":
        return "I was made using Python."
    elif user_input == "thank you":
        return "You are welcome!"
    elif user_input == "bye":
        return "Bye! Have a nice day."
    else:
        return "Sorry, I do not understand."

print("🤖 Simple Chatbot")
print("Type 'bye' to exit\n")

while True:
    user_message = input("You: ")
    reply = chatbot_response(user_message)
    print("Bot:", reply)

    if user_message.lower() == "bye":
        break
