import google.generativeai as genai

Google_Gemini_api_key = "AIzaSyA6KgWwGh5J5SReEnMb4M0PfMSg-WCt6eE"
genai.configure(api_key=Google_Gemini_api_key)

for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel("gemini-2.0-flash-lite")   

response = model.generate_content("quem criou o python?")
response.text
print("Mensagem enviada com sucesso!")

chat = model.start_chat(history=[])
prompt = input("esperando prompt:")

while prompt != "fim" :
    response = chat.send_message(prompt)
    print("resposta:", response.text)
    prompt = input("esperando prompt:")