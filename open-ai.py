import openai

# Set your API key
openai.api_key = 'YOUR_API_KEY'

# Initialize the messages list with the system message
messages = [{"role": "system", "content": "You are an intelligent assistant."}]

while True:
    # Get user input
    user_input = input("User: ")
    
    # Exit loop if user input is empty (optional)
    if not user_input:
        print("Exiting chat.")
        break
    
    # Append user message to the messages list
    messages.append({"role": "user", "content": user_input})
    
    # Call the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    # Extract the reply from the response
    reply = response.choices[0].message['content']
    
    # Print the reply
    print(f"ChatGPT: {reply}")
    
    # Append assistant's reply to the messages list
    messages.append({"role": "assistant", "content": reply})
