## ENGLISH
<details>
  <summary><strong>ENGLISH INSTALLATION GUIDE<strong></summary>
  
## GPT-3 Based Chatbot

This is a chatbot application that uses OpenAI's GPT-3 API. The Flask web application sends messages from the user through a web page to the OpenAI API and displays the response from the API on the web page.

# Usage

To use this application, you need to first set your OpenAI API key in the `config.cfg` file. You can also customize the `openai_settings` dictionary with the settings you want to use in your GPT-3 API requests.

# Config.cfg


<details>
  <summary><strong>dictionary of configuration parameters<strong></summary>

```
[openai]
engine = This parameter determines which version of the GPT-3 model hosted on OpenAI's servers to use.
temperature = This parameter controls the variation in the model's output. Higher temperature can result in more creative and risky responses, while lower temperature produces safer and more repeatable responses.
max_tokens = This parameter sets the maximum length of the response that the model will generate.
top_p = This parameter sets the probability threshold that the model uses when ranking possible results. A higher Top_p value allows the model to generate responses across a wider range.
frequency_penalty = This parameter reduces the model's tendency to repeat certain words or phrases in its response. Increasing the frequency penalty may cause the model to reduce its use of repetitive responses.
presence_penalty = This parameter reduces the model's tendency to use certain words or phrases in its response. Increasing the presence penalty may cause the model to reduce its use of certain words in its responses.

```
</details>


To start the application, run the following command in the command line:

```
python app.py
```

After the application is successfully started, open `http://localhost:3131` in your browser and start talking to the chatbot.

# Warnings

- Before using this application, you need to acquire an OpenAI API membership.
- This application creates a log file that records the messages sent by the user. For user privacy, this log file should be stored securely.
- This application is recommended to be used for testing purposes only. Chatbots that will be used in real-world applications should go through a more comprehensive training and validation process.

# Contact

If you have any questions or feedback regarding this application, please feel free to contact me.
```
discord: mertcan#0001
instagram: mertcvn.jpg

```
</details>



## TURKCE
<details>
  <summary><strong>TURKCE KURULUM REHBERI<strong></summary>

## GPT-3 Tabanlı Kişiselleştirilmiş Chatbot

Bu, OpenAI'nin GPT-3 API'sini kullanarak bir chatbot uygulamasıdır. Flask web uygulaması, bir web sayfası aracılığıyla kullanıcıdan gelen mesajları OpenAI API'sine gönderir ve API'den gelen yanıtı mesaj baloncuğunda gösterir.

- # Kullanım

Bu uygulamayı kullanmak için önce `ayarlar.cfg` dosyasında OpenAI API anahtarınızı ayarlamanız gerekir. 
Ayrıca `openai_settings` sözlüğünü, GPT-3 API'si isteklerinde kullanmak istediğiniz ayarlarla özelleştirebilirsiniz.

# Ayarlar.cfg
<details>
  <summary><strong>cfg dosyasindaki ayarlarin aciklamalari<strong></summary>

```
[openai]
engine = Bu parametre, OpenAI'nin sunucularında barındırılan GPT-3 modelinin hangi sürümünü kullanacağını belirler.
temperature = Bu parametre, modelin çıktısındaki varyasyonu kontrol eder. Daha yüksek bir temperature degeri, daha yaratıcı ve riskli cevaplar üretebilirken, daha düşük bir temperature daha güvenli ve tekrar edilebilir cevaplar üretir.
max_tokens = Bu parametre, modelin üreteceği cevabın maksimum uzunluğunu belirler. 
top_p =  Bu parametre, modelin olası sonuçları sıralarken kullanacağı olasılık sınırını belirler. Daha yüksek bir Top_p değeri, modelin daha geniş bir yelpazede cevaplar üretmesine izin verir.
frequency_penalty = Bu parametre, modelin belirli kelimeleri veya ifadeleri tekrar etme eğilimini azaltır. Daha yüksek bir frequency penalty, modelin tekrarlı cevapları azaltmasına yol açabilir.
presence_penalty = Bu parametre, modelin belirli kelimeleri veya ifadeleri cevapta kullanma eğilimini azaltır. Daha yüksek bir presence penalty, modelin belirli kelimeleri cevapta kullanma sıklığını azaltmasına yol açabilir.

```
</details>

Uygulamayı başlatmak için, komut satırında şu komutu çalıştırın:

```
python app.py
```

Uygulama başarıyla başlatıldıktan sonra, tarayıcınızda `http://localhost:3131` adresini açın ve chatbot'la konuşmaya başlayabilirsiniz.

- # Uyarılar

- Bu uygulamayı kullanmak için OpenAI API üyeliğiniz olması gerekmektedir.
- Bu uygulama, kullanıcının gönderdiği mesajları kaydeden bir log dosyası oluşturur. Kullanıcı gizliliği için bu log dosyası güvenli bir şekilde saklanmalıdır.
- Bu uygulamanın yalnızca test amaçlı kullanılması önerilir. Gerçek dünya uygulamalarında kullanılacak chatbot'lar, daha kapsamlı bir eğitim ve doğrulama sürecinden geçmelidir.

- # İletişim

Bu uygulamayla ilgili herhangi bir sorunuz veya geri bildiriminiz varsa, lütfen bana ulaşın.
```
discord: mertcan#0001
instagram: mertcvn.jpg

```
</details>