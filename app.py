# Flask kütüphanesinden Flask, render_template, request ve jsonify modüllerini içe aktar
# openai ve os modüllerini içe aktar
from flask import Flask, render_template, request, jsonify
import openai
import os

# Flask uygulamasını oluştur
app = Flask(__name__)

# OpenAI API anahtarı
openai.api_key = "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"

# Log dosyasını ayarla
log_file = "log.txt"

# prompt içeriğini brief.txt dosyasından oku
with open("brief.txt", "r", encoding="utf-8") as f:
    prompt = f.read()

# templates dizinindeki index.html dosyasını sunmak için Flask route oluştur
@app.route('/')
def home():
    return render_template('index.html')

# OpenAI'dan yanıt almak için API endpoint'i oluştur
@app.route('/get-response', methods=['POST'])
def get_response():
    # Get message from client-side form input
    message = request.json['message']

    # anıt oluşturmak için OpenAI'nin GPT-3 API'sını çağır
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{prompt}\n{message}\n",
        temperature=0.6,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # OpenAI API yanıtından yanıt metnini ayıkla
    bot_response = response.choices[0].text.strip()

    # Mesajı ve yanıtı log dosyasına yaz
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"Message: {message}\n")
        f.write(f"Response: {bot_response}\n\n")

    return jsonify({'message': bot_response})

if __name__ == '__main__':
    app.run()
