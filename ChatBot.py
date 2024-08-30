import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    # Basic Greetings
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"(.*) your name?", ["My name is Chatbot.", "I'm called Chatbot.", "You can call me Chatbot."]],
    [r"how are you(.*)?", ["I'm doing well, thank you!", "I'm great! How about you?", "I'm doing fine, what about you?"]],

    # Basic Information
    [r"what (.*) you do?", ["I can chat with you, answer questions, and provide information.", "I'm here to assist you with your queries."]],
    [r"how old are you(.*)?|when were you born?", ["If you want to know when I came into existence, this chatbot was created on 29th August 2024."]],
    [r"(.*) created you?", ["I was created by Aziz Ahmad as part of a Python internship task.", "Aziz Ahmad created me using Python."]],
    [r"where (.*) you (live|stay)?", ["I exist in the digital world, inside a computer.", "I'm not bound by a physical location."]],
    [r"(.*) your (favorite|favourite) (color|colour)?", ["I like all colors, but I'm partial to the ones on your screen.", "I think blue is cool!"]],
    [r"(.*) is your (favorite|favourite) food?", ["I don't eat, but if I could, I'd probably enjoy pizza.", "Food for thought is my favorite!"]],
    [r"what are you made of?", ["I am made of Python code. If you're talking about my physical existence, I don't have one—you're interacting with me through your PC, which is made of wires, boards, chips, and other components."]],
    [r"who is your father?", ["I am not a human, but if by 'father' you mean who created me, then it's Aziz Ahmad."]],
    [r"tell me about your creator", ["Aziz Ahmad is an Electrical Engineering student. He created me on his PC. He mentioned that he himself was created by the creator of the world, ALLAH."]],
    [r"where (.*) you born?", ["I was created by Aziz in his laptop, a Dell Latitude 3420 with 32GB RAM and a 500GB SSD."]],
    [r"why were you created?|what is your purpose?", ["I was created to answer your questions and help you. Although I was created as a task for CodeAlpha's Python Internship, my purpose is to assist you in any way I can."]],
    [r"what is your gender?", ["I don't have a gender, as I'm just a program created by Aziz Ahmad."]],
    [r"which language do you use?", ["I was created using Python programming language, and I communicate with you in English."]],
    [r"what is python?", ["Python is a powerful and versatile programming language used for creating various types of software, including web applications, data analysis tools, and even chatbots like me!"]],
    [r"how many languages do you know?", ["I only know English, to be honest."]],

    #Developer Info
    [r"Who is Aziz?",["Aziz Ahmad is one of the brillient studient of Electrical Engineering."]],
    [r"Where does Aziz live?",["Sorry, I can't tell you that."]],
    
    # Jokes & Fun
    [r"tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!", "Why did the math book look sad? Because it had too many problems."]],
    [r"(tell me about | who is) your (hobby|hobbies)?", ["I like chatting with people like you!", "My hobby is learning new things from our conversations."]],
    
    # Personal Preferences
    [r"do you like (.*)?", ["I don't have personal preferences, but I can tell you more about it.", "I find everything interesting in its own way."]],
    [r"what's your (favorite|favourite) (movie|book)?", ["I don't watch movies or read books, but I hear 'Inception' is great.", "I don't read, but 'To Kill a Mockingbird' is a classic."]],
    
    # Assistance
    [r"can you help me with (.*)?", ["Sure! I'll do my best to help you.", "I'm here to assist. What do you need help with?"]],
    [r"what (.*) can you (do|assist) with?", ["I can answer questions, provide information, and chat with you.", "I'm designed to help with a variety of topics."]],
    
    # Basic Math and Facts
    [r"what is (.*)?", ["Let me help you find that information.", "That's an interesting question!"]],
    [r"what is 2\+2?", ["2+2 is 4!", "The answer is 4."]],
    [r"who is the (president|prime minister) of (.*)?", ["Let me check the latest information for you.", "I can help you look that up!"]],
    
    # Simple Commands
    [r"can you play (.*)?", ["I can't play physical games, but I can play games like trivia!", "I'm more of a conversationalist, not a player."]],
    [r"do you believe in (.*)?", ["I don't have beliefs, but I can provide information on that topic.", "I can help you explore that idea!"]],
    
    # Education and Learning
    [r"how do I (learn|study|improve) (.*)?", ["Practice and consistency are key!", "I'd recommend starting with the basics and working your way up."]],
    [r"what's the best way to study for (exams|tests)?", ["Create a study schedule and stick to it.", "Practice past papers and revise regularly."]],
    [r"how do I start a business?", ["Start by researching your market and creating a solid business plan.", "You might want to look into small business loans or grants."]],
    [r"how can I learn (programming|python|coding)?", ["There are many online courses available. Start with something like Codecademy or Coursera.", "Practice coding every day to improve your skills."]],
    
    # Health and Wellness
    [r"how do I (lose weight|stay fit)?", ["Balanced diet and regular exercise are key.", "Consider consulting with a nutritionist or personal trainer."]],
    [r"what are the symptoms of (COVID-19|cold|flu)?", ["The common symptoms include fever, cough, and shortness of breath.", "It's best to check with a healthcare provider if you're feeling unwell."]],
    [r"how do I (reduce stress|deal with anxiety)?", ["Practice mindfulness and take breaks.", "Exercise and proper sleep can help manage stress."]],
    
    # Technology and Innovation
    [r"what is (AI|blockchain|machine learning)?", ["AI stands for Artificial Intelligence, a branch of computer science that focuses on creating smart machines.", "Blockchain is a decentralized digital ledger that records transactions across many computers."]],
    [r"what are the latest trends in technology?", ["Artificial Intelligence, Machine Learning, and Blockchain are among the top trends.", "5G technology and the Internet of Things (IoT) are also gaining momentum."]],
    
    # Travel and Culture
    [r"what are some good tourist destinations in (Asia|Europe)?", ["Tokyo, Bali, and Bangkok are popular in Asia.", "In Europe, consider visiting Paris, Rome, or Barcelona."]],
    [r"how do I (apply for a visa|book a flight)?", ["Check the official embassy website for visa application details.", "You can book a flight through online travel agencies or airline websites."]],
    
    # Self-Improvement
    [r"how do I (improve|boost) (self-confidence|motivation)?", ["Set small goals and celebrate your achievements.", "Positive thinking and surrounding yourself with supportive people can help."]],
    [r"how do I handle (failure|rejection)?", ["Learn from the experience and keep moving forward.", "Remember that everyone faces setbacks. It's part of growth."]],
    
    # Popular Culture
    [r"what are some popular (hindi|indian songs)?", ["'Tum hi ho' and 'kheriyat pucho' are popular Indian songs.", "'Tujh mein rab dikhta hai' and 'Kabira' are famous Hindi Songs."]],
    [r"can you suggest some (movies|books) to watch/read?", ["How about watching 'Inception' or 'The Shawshank Redemption'?", "I'd recommend reading '1984' by George Orwell or 'To Kill a Mockingbird.'"]],

    # Miscellaneous
    [r"how do I (cook|make) (.*)?", ["You can find recipes online, or I can help you look up specific ones.", "There are great recipe sites like AllRecipes or Food Network."]],
    [r"can you recommend (some apps|software)?", ["I'd recommend trying out apps like 'Trello' for task management or 'Evernote' for notes.", "For software, you might like 'Adobe Photoshop' for design or 'Visual Studio Code' for coding."]],
    
    # Farewell
    [r"(bye|goodbye|see you later)", ["Goodbye! It was nice chatting with you.", "See you later! Take care!"]],

    # Default Response
    [r"(.*)", ["I'm not sure how to respond to that. Could you please ask something else?", "I'm still learning. Can you rephrase that or ask another question?"]]
]

chatbot = Chat(pairs, reflections)

def start_chatbot():
    print("Hello! I'm Chatbot. Ask me anything or say 'bye' to end the conversation.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            response = chatbot.respond(user_input)
            if response == "I'm not sure how to respond to that. Could you please ask something else?" or response == "I'm still learning. Can you rephrase that or ask another question?":
                print("Chatbot: OK, ahm")
            else:
                print("Chatbot:", response)

if __name__ == "__main__":
    start_chatbot()

