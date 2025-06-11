import openai


openai.api_key = "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"

def chat():
    print("Welcome to the AI Chatbot. Type 'exit' to quit.")
    conversation = []

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break

        conversation.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=conversation
        )

        reply = response['choices'][0]['message']['content']
        print("Bot:", reply.strip())
        conversation.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    chat()
      