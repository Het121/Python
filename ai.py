import openai
openai.api_key = ''
messages = [{"role":"system",
           "content":"You are a intelligent assitant."}]
while True:
    message = input("User : ")
    if message:
        messages.append(
            {}
        )
