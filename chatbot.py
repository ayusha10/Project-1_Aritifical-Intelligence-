print("===================================")
print(" Welcome to  AI Chatbot ")
print("===================================")
print("Type 'exit' anytime to quit.\n")

while True:

    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! Nice to meet you.")

    elif user == "hi":
        print("Bot: Hi! How are you?")

    elif user == "hey":
        print("Bot: Hey there!")

    elif user == "how are you":
        print("Bot: I am doing great. Thanks for asking!")

    elif user == "what is your name ? ":
        print("Bot: My name is  AI Chatbot. How can i help you? ")

    elif user == "who made you":
        print("Bot: I was created as a Rule-Based AI project.")

    elif user == "what can you do":
        print("Bot: I can answer your questions and have a conversation with you.") 

    elif user == "bye":
        print("Bot: Goodbye!")

    elif user == "exit":
        print("Bot: Thank you for chatting.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")