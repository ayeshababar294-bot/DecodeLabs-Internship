print("=" * 60)
print("🤖 AI ASSISTANT CHATBOT")
print("=" * 60)
print("Hello! I am DecodeBot, your Rule-Based AI Assistant.")
print("Type 'help' to see available commands.")
print("Type 'bye' or 'exit' to end the chat.\n")

while True:
    user = input("You: ").lower().strip()

    # Greetings
    if user in ["hi", "hello", "hey", "salam", "assalamualaikum"]:
        print("Bot: Hello! It's nice to meet you. How can I help you today?")

    # How are you
    elif user == "how are you?":
        mood = input("Bot: I am doing great! How are you feeling today? ").lower()

        if mood in ["good", "fine", "great", "awesome"]:
            print("Bot: That's wonderful to hear! I hope you continue to have a great day.")
        elif mood in ["sad", "bad", "upset"]:
            print("Bot: I'm sorry to hear that. Stay positive and remember that better days are ahead.")
        else:
            print("Bot: Thank you for sharing your feelings with me.")

    # Name
    elif user == "what is your name?":
        print("Bot: My name is DecodeBot. I am a simple rule-based AI chatbot designed to answer predefined questions.")

    # Creator
    elif user == "who made you?":
        print("Bot: I was created by a DecodeLabs AI Intern named Ayesha Babar as part of an Artificial Intelligence learning project.")

    # AI
    elif user == "what is ai?":
        print("Bot: AI stands for Artificial Intelligence. It is a field of computer science that enables machines to perform tasks that normally require human intelligence, such as learning, reasoning, and problem solving.")

    # Python
    elif user == "what is python?":
        print("Bot: Python is a high-level and easy-to-learn programming language. It is widely used in web development, data science, automation, and Artificial Intelligence.")

    # Internship
    elif user == "what is internship?":
        print("Bot: An internship is a short-term learning experience where students or beginners gain practical skills and real-world work experience in a professional environment.")

    # Chatbot
    elif user == "what is a chatbot?":
        print("Bot: A chatbot is a software application that can communicate with users through text or voice. It is commonly used for customer support, information services, and virtual assistance.")

    # Machine Learning
    elif user == "what is machine learning?":
        print("Bot: Machine Learning is a branch of Artificial Intelligence that allows computers to learn from data and improve their performance without being explicitly programmed.")

    # Purpose
    elif user == "what can you do?":
        print("Bot: I can answer basic questions, provide simple information, and demonstrate rule-based decision-making using if-else conditions.")

    # Help
    elif user == "help":
        print("\n📌 Available Questions:")
        print("• How are you?")
        print("• What is your name?")
        print("• Who made you?")
        print("• What is AI?")
        print("• What is Python?")
        print("• What is Internship?")
        print("• What is a Chatbot?")
        print("• What is Machine Learning?")
        print("• What can you do?")
        print("• Thank you")
        print("• Bye / Exit\n")

    # Thanks
    elif user in ["thanks", "thank you"]:
        print("Bot: You're welcome! I am always happy to help.")

    # Exit
    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Thank you for chatting with me. Have a wonderful day!")
        break

    # Unknown
    else:
        print("Bot: Sorry, I do not understand that question.")
        print("Bot: Please type 'help' to see the list of available questions.")