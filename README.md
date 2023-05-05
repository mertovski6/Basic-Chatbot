## ENGLISH
<details>
  <summary><strong>ENGLISH INSTALLATION GUIDE<strong></summary>
  
## GPT-3 Based Chatbot

This is a chatbot application that uses OpenAI's GPT-3 API. The Flask web application sends messages from the user through a web page to the OpenAI API and displays the response from the API on the web page.

# Usage

To use this application, you need to first set your OpenAI API key in the `app.py` file. 
You can also customize the `ayarlar.cfg` file with the settings you want to use in your GPT-3 API requests.



# Config.cfg
<details>
  <summary><strong>dictionary of configuration parameters<strong></summary>

- `prompt`: The user's input as a string.
- `model`: The GPT-3 model to use, e.g. "text-davinci-002".
- `temperature`: Controls the "creativity" of the generated text. Higher values result in more creative responses.
- `max_tokens`: The maximum number of tokens (words) to generate in the response.
- `top_p`: The maximum probability of selecting a candidate response.
- `frequency_penalty`: The amount of penalty to apply to tokens that have been recently generated. Higher values result in less repetition in the generated text.
- `presence_penalty`: The amount of penalty to apply to tokens that have been generated in the prompt. Higher values result in more novelty in the generated text.
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
brief.txt dosyası ise, OpenAI API'si için bir başlangıç metni veya bir "prompt" içeren bir dosyadır. Bu dosya, uygulama tarafından OpenAI API'sine gönderilen her istek için kullanılır ve her istek, prompt ile birlikte OpenAI API'sine gönderilir. OpenAI API'si, prompt'ı kullanarak bir yanıt üretir ve bu yanıt uygulama tarafından alınır ve kullanıcının web sayfasında görmesi için sunulur.
- # Kullanım

Bu uygulamayı kullanmak için önce `app.py` dosyasında OpenAI API anahtarınızı ayarlamanız gerekir. 
Ayrıca `ayarlar.cfg` dosayasını, GPT-3 API'si isteklerinde kullanmak istediğiniz ayarlarla özelleştirebilirsiniz.

# Ayarlar.cfg
<details>
  <summary><strong>cfg dosyasindaki ayarlarin aciklamalari<strong></summary>

```

- `prompt`: The user's input as a string.
- `engine`: Bu parametre, OpenAI'nin sunucularında barındırılan GPT-3 modelinin hangi sürümünü kullanacağını belirler.
- `temperature`: Bu parametre, modelin çıktısındaki varyasyonu kontrol eder. Daha yüksek bir temperature degeri, daha yaratıcı ve riskli cevaplar üretebilirken, daha düşük bir temperature daha güvenli ve tekrar edilebilir cevaplar üretir.
- `max_tokens`: The maximum number of tokens (words) to generate in the response.
- `top_p`: Bu parametre, modelin olası sonuçları sıralarken kullanacağı olasılık sınırını belirler. Daha yüksek bir Top_p değeri, modelin daha geniş bir yelpazede cevaplar üretmesine izin verir.
- `frequency_penalty`: Bu parametre, modelin belirli kelimeleri veya ifadeleri tekrar etme eğilimini azaltır. Daha yüksek bir frequency penalty, modelin tekrarlı cevapları azaltmasına yol açabilir.
- `presence_penalty`: Bu parametre, modelin belirli kelimeleri veya ifadeleri cevapta kullanma eğilimini azaltır. Daha yüksek bir presence penalty, modelin belirli kelimeleri cevapta kullanma sıklığını azaltmasına yol açabilir.


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


##

## Lisans Bilgileri
# GNU GENEL KAMU LİSANSI
`Sürüm 3, 29 Haziran 2007`

Telif © 2007 Free Software Foundation, Inc. <http://fsf.org/>
Herkes bu programı kopyalayabilir ve dağıtabilir, değiştirebilir ve
programın kaynak kodunu isteyenlere vermek zorundadır. Herkes bu
programı ticari olarak kullanabilir ve hatta bunu özgür olmayan
programların parçası olarak dağıtabilir, ama bu durumda bile
kaynak kodunu vermek zorundadır. 

Daha fazla detay için lisansı inceleyiniz. xd
