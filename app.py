from flask import Flask, render_template, request, jsonify
import openai
import os
import configparser
from dotenv import load_dotenv
import os
load_dotenv()

# Flask uygulamasını oluştur
app = Flask(__name__)

# Ayarları oku
config = configparser.ConfigParser()
config.read('ayarlar.cfg')

# OpenAI API anahtarını ayarla
openai_key=os.getenv("OPENAI_API_KEY")
openai.api_key = openai_key


# templates dizinindeki index.html dosyasını sunmak için Flask route oluştur
@app.route('/')
def home():
    return render_template('index.html')



# prompt içeriğini brief.txt dosyasından oku
with open("brief.txt", "r", encoding="utf-8") as f:
    prompt = f.read()



# OpenAI API istekleri için sözlük oluştur
openai_settings = {
    'engine': config['openai']['engine'],
    'temperature': float(config['openai']['temperature']),
    'max_tokens': int(config['openai']['max_tokens']),
    'top_p': float(config['openai']['top_p']),
    'frequency_penalty': float(config['openai']['frequency_penalty']),
    'presence_penalty': float(config['openai']['presence_penalty'])
}

# OpenAI'den yanıt almak için API endpoint'i oluştur
@app.route('/get-response', methods=['POST'])
def get_response():
    # Get message from client-side form input
    message = request.json['message']

    # anıt oluşturmak için OpenAI'nin GPT-3 API'sını çağır
    response = openai.Completion.create(
        prompt=f"{prompt}\n{message}\n",
        **openai_settings
    )
    # OpenAI API yanıtından yanıt metnini ayıkla
    bot_response = response.choices[0].text.strip()

    # Mesajı ve yanıtı log dosyasına yaz
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"Message: {message}\n")
        f.write(f"Response: {bot_response}\n\n")

    return jsonify({'message': bot_response})

# Log dosyasını ayarla
log_file = "log.txt"


if __name__ == '__main__':
    app.run(debug=True)
    
    app.run(host='0.0.0.0', port=(int(os.environ.get('5000'))))